/*
#============================================================================#
#                    F a c t u r a S i e l i   ( 2 0 2 4 )                   #
#============================================================================#
# File   : static/facturasieli/js/service.js               #
# Author : Morice                                         #
#============================================================================#    
*/

function active_service_tab(elt_id) {
    if (elt_id=='home-tab') {
        $( "button#home-tab" ).attr( "aria-selected", true );
        $( "button#home-tab" ).toggleClass('active', true);
        $( "div#home-tab-pane" ).toggleClass('show active', true);
        
        $( "button#profile-tab" ).attr( "aria-selected", false );
        $( "button#profile-tab" ).toggleClass('active', false);
        $( "div#profile-tab-pane" ).toggleClass('show active', false);
    }else{
        $( "button#profile-tab" ).attr( "aria-selected", true );
        $( "button#profile-tab" ).toggleClass('active', true);
        $( "div#profile-tab-pane" ).toggleClass('show active', true);

        $( "button#home-tab" ).attr( "aria-selected", false );
        $( "button#home-tab" ).toggleClass('active', false);
        $( "div#home-tab-pane" ).toggleClass('show active', false);

        // save the active tab id in local storage
        localStorage.setItem('active_service', elt_id);
    }
}


document.addEventListener('DOMContentLoaded', function(){
    const activeTabId = localStorage.getItem('active_service');
    
    if (activeTabId) {
        active_service_tab(activeTabId);
    }
});