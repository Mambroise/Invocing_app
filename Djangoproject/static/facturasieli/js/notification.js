/*
#============================================================================#
#                    F a c t u r a S i e l i   ( 2 0 2 4 )                   #
#============================================================================#
# File   : static/facturasieli/js/notification.js                            #
# Author : Morice                                                            #
#============================================================================#    
*/

/*
    Cette est utilise par l'evenement onclick pour activer les tab quand on clique 
    sur l'un ou l'autre
*/
function activer_tab(id_elt){
    if(id_elt=='nav-notif-received-tab'){
        $( "a#nav-notif-received-tab" ).attr( "aria-selected", true )
        $( "a#nav-notif-received-tab" ).toggleClass("active", true)
        $("div#nav-notif-received").toggleClass("show active", true)

        $( "a#nav-notif-sended-tab" ).attr( "aria-selected", false );
        $( "a#nav-notif-sended-tab" ).toggleClass("active", false);
        $("div#nav-notif-sended").toggleClass("show active", false);
        
        localStorage.setItem('activeSentPage',1);  // Optional: reset page on tab switch
        var currentPageId = localStorage.getItem('activeRecievedPage')
        activer_page(currentPageId)
    }else{
        $( "a#nav-notif-received-tab" ).attr( "aria-selected", false );
        $( "a#nav-notif-received-tab" ).toggleClass("active", false);
        $("div#nav-notif-received").toggleClass("show active", false);
        
        $( "a#nav-notif-sended-tab" ).attr( "aria-selected", true );
        $( "a#nav-notif-sended-tab" ).toggleClass("active", true);
        $("div#nav-notif-sended").toggleClass("show active", true);
        localStorage.setItem('activeRecievedPage',1);  // Optional: reset page on tab switch
        var currentPageId = localStorage.getItem('activeSentPage')
        activer_page(currentPageId)
    }

    // save the active tab id in local storage
    localStorage.setItem('activeTab', id_elt);
}


// Event listener to save the current page in local storage when a pagination button is clicked
$(document).on('click', '.page-link', function() {
    console.log('ca clique sur le bon lien');
    
    var page = $(this).attr('href'); // Get the page number from the button
    var pageValue = $(this).text().trim()
    console.log(page);
    if (page.includes('page_sended')){

        localStorage.setItem('activeSentPage', pageValue); // Store the current page in local storage
    } else {
        localStorage.setItem('activeRecievedPage', pageValue); // Store the current page in local storage
    }
    
});

//load the active object form localstorage if exists
document.addEventListener('DOMContentLoaded', function(){
    const activeTabId = localStorage.getItem('activeTab');
    
    if (activeTabId){
        activer_tab(activeTabId);
    }
});

function tranformTypeNotificationFromIntToString(language, notificationType){

    var result;
    if (language=='fr') {
        switch (notificationType) {
            case 1:
                result = "Facture demandée";
                break;
            case 2:
                result = "Facture soumise";
                break;
            case 3:
                result = "Facture vérifiée";
                break;
            case 4:
                result = "Facture rejetée";
                break;
            case 5:
                result = "Facture payée";
                break;
            case 6:
                result = "Facture Modifiée";
                break;
            case 7:
                result = "Facture supprimée";
                break;
            case 8:
                result = "Intervention modifiée";
                break;
            case 9:
                result = "Interventon supprimée";
                break;
            case 10:
                result = "Création de compte";
                break;
            case 11:
                result = "Modification de compte";
                break;
            default:
                result= "Type de notification inconnu";
        }
    } else if(language=='en') {
        
        switch (notificationType) {
            case 1:
                result = "Invoice Request";
                break;
            case 2:
                result = "Invoice Submitted";
                break;
            case 3:
                result = "Invoice Verified";
                break;
            case 4:
                result = "Invoice Rejected";
                break;
            case 5:
                result = "Invoice Paid";
                break;
            case 6:
                result = "Invoice Modified";
                break;
            case 7:
                result = "Invoice Deleted";
                break;
            case 8:
                result = "Service Modified";
                break;
            case 9:
                result = "Service Deleted";
                break;
            case 10:
                result = "New Account Created";
                break;
            case 11:
                result = "Account modified";
                break;
            default:
                result= "unknown notification type";
        }
    }
    
    return result;
}


function show_modal_notification_received(notificationId, notificationType, language, serviceTitle, companyName, companySiret, send_at) {
    
    var a_close_button = document.getElementsByClassName("is_read")[0];
    var baseUrl = a_close_button.getAttribute("data-url");
    var urlWithNotificationId = baseUrl.replace("0", notificationId);
    a_close_button.setAttribute("href", urlWithNotificationId);

    var modal = document.getElementById("modal_nofification_received");

    var notificationTypeElement = tranformTypeNotificationFromIntToString(language,notificationType);
    
    
    var service = $('td#service')
    var notiftype = $('td#notiftype')
    var company = $('td#company')
    var date = $('td#date')

    // Clear previous content
    service.empty();
    notiftype.empty();
    company.empty();
    date.empty();

    service.append(serviceTitle)
    notiftype.append(notificationTypeElement)
    date.append(send_at)
    company.append(companyName)

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal
    modal.style.display = "block"; 

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}
