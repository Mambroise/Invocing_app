/*
#============================================================================#
#                    F a c t u r a S i e l i   ( 2 0 2 4 )                   #
#============================================================================#
# File   : static/facturasieli/js/message.js                                 #
# Author : Morice                                   #
#============================================================================#    
*/

document.addEventListener("DOMContentLoaded", function() {
    const messages = document.querySelectorAll('.messages .alert');
    if (messages) {
        messages.forEach(function(message) {
            setTimeout(function() {
                message.classList.add('hide');
            }, 3000); 
            setTimeout(function() {
                message.remove();
            }, 5000); 
        });
    }
});