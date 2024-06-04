/*
#============================================================================#
#                    F a c t u r a S i e l i   ( 2 0 2 4 )                   #
#============================================================================#
# File   : static/facturasieli/notification/js/notification.js               #
# Author : Arnaud DJIM-ASSEl RIBAR                                           #
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
        
    }else{
        $( "a#nav-notif-received-tab" ).attr( "aria-selected", false );
        $( "a#nav-notif-received-tab" ).toggleClass("active", false);
        $("div#nav-notif-received").toggleClass("show active", false);

        $( "a#nav-notif-sended-tab" ).attr( "aria-selected", true );
        $( "a#nav-notif-sended-tab" ).toggleClass("active", true);
        $("div#nav-notif-sended").toggleClass("show active", true);
    }

}

function  extract_date(send_at){
    var  dateNotif = new Date(send_at);
    
    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    };
    date_result = dateNotif.toLocaleDateString('fr-FR');
    return date_result

}

function tranformTypeNotificationFromIntToString(notificationType){
    var result;
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
        default:
            result= "Type de notification inconnu";
    }
    return result;
}

function createElementTRTypeNotification(typeNotification){
    const trType = document.createElement("tr");

    const thScope =  document.createElement("th");
    thScope.setAttribute("scope", "row");
    const tdTypeKey = document.createElement("td");
    const tdTypeValue = document.createElement("td");

    tdTypeKey.append("Type de notification");
    tdTypeValue.append(typeNotification);

    trType.appendChild(thScope);
    trType.appendChild(tdTypeKey);
    trType.appendChild(tdTypeValue);

    return trType;
}

function createElementTRDateReceptionNotification(send_at){
    const dateReceptionNotif = extract_date(send_at);
    const trDateReception = document.createElement("tr");

    const thScope =  document.createElement("th");
    thScope.setAttribute("scope", "row");

    const tdDateKey = document.createElement("td");
    const tdDateValue = document.createElement("td");

    const pDate = document.createElement("p");
    const pHeure = document.createElement("p");
    pDate.append(dateReceptionNotif);

    tdDateKey.append("Réçue le : ");
    tdDateValue.appendChild(pDate);

    trDateReception.appendChild(thScope);
    trDateReception.appendChild(tdDateKey);
    trDateReception.appendChild(tdDateValue);

    return trDateReception;
}

function createEleementTRServiceTitle(serviceTitle){
    const trService = document.createElement("tr");

    const thScope =  document.createElement("th");
    thScope.setAttribute("scope", "row");
    const tdServiceKey = document.createElement("td");
    const tdServiceValue = document.createElement("td");

    tdServiceKey.append("Titre du service");
    tdServiceValue.append(serviceTitle);

    trService.appendChild(thScope);
    trService.appendChild(tdServiceKey);
    trService.appendChild(tdServiceValue);
    return trService;
}

function createElementTREmeteur(companyName, companySiret){
    const trEmetteur = document.createElement("tr");

    const thScope =  document.createElement("th");
    thScope.setAttribute("scope", "row");

    const tdEmetteurKey = document.createElement("td");
    const tdEmetteurValue = document.createElement("td");

    sirentContent = "- Siret : " + companySiret;
    companyNameContent = "- Nom de l'entreprise : " + companyName;
    const pSiret = document.createElement("p");
    const pCompanyName = document.createElement("p");
    pSiret.append(sirentContent);
    pCompanyName.append(companyNameContent);

    tdEmetteurKey.append("Emmeteur");
    tdEmetteurValue.appendChild(pCompanyName);
    tdEmetteurValue.appendChild(pSiret);

    trEmetteur.appendChild(thScope);
    trEmetteur.appendChild(tdEmetteurKey);
    trEmetteur.appendChild(tdEmetteurValue);

    return trEmetteur;
}

function show_modal_notification_received(notificationType, serviceTitle, companyName, companySiret, send_at) {
    var dateReceptionNotification = extract_date(send_at);

    var spanType = document.createElement("span");
    var spanService = document.createElement("span");
    var spanEmetteur = document.createElement("span");
    var spanDateRecetionNotification = document.createElement("span");
    // Get the modal
    var modal = document.getElementById("modal_nofification_received");
    //notif_received_infos
    var table_information = document.getElementById("table_notif_received_infos");
    table_information.appendChild(spanType);
    table_information.appendChild(spanService);
    table_information.appendChild(spanEmetteur);
    table_information.appendChild(spanDateRecetionNotification)

    var notificationTypeElement =createElementTRTypeNotification(
        tranformTypeNotificationFromIntToString(notificationType)
        );

    var serviceTitleElement = createEleementTRServiceTitle(serviceTitle);
    
    var emetteurElement = createElementTREmeteur(companyName, companySiret);

    var dateRecetionNotificationElement = createElementTRDateReceptionNotification(send_at);

    spanType.replaceWith(notificationTypeElement);
    spanService.replaceWith(serviceTitleElement);
    spanEmetteur.replaceWith(emetteurElement);
    spanDateRecetionNotification.replaceWith(dateRecetionNotificationElement);
    

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal
    modal.style.display = "block"; 

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
        notificationTypeElement.replaceWith(spanType);
        serviceTitleElement.replaceWith(spanService);
        emetteurElement.replaceWith(spanEmetteur);
        dateRecetionNotificationElement.replaceWith(spanDateRecetionNotification);

    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            
            notificationTypeElement.replaceWith(spanType);
            serviceTitleElement.replaceWith(spanService);
            emetteurElement.replaceWith(spanEmetteur);
            dateRecetionNotificationElement.replaceWith(spanDateRecetionNotification);
        }
    }
}
