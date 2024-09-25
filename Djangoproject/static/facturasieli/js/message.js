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
            }, 6000); 
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const message = document.getElementById('invoice-status');
    const statusDiv = document.getElementById('status-div');
    const data = message.getAttribute('data-meta');

    // reinitialise classes
    resetClasses(message, statusDiv);

    // Définir les classes en fonction du statut
    const statusClasses = {
        '1': { messageClass: 'text-warning', divClass: 'border-warning' },
        '2': { messageClass: 'text-success', divClass: 'border-success' },
        '3': { messageClass: 'text-danger', divClass: 'border-danger' },
        '4': { messageClass: 'text-danger', divClass: 'border-success' }
    };

    // Appliquer les classes si le statut existe dans l'objet
    if (statusClasses[data]) {
        message.classList.add(statusClasses[data].messageClass);
        statusDiv.classList.add(statusClasses[data].divClass);
    }
});

function resetClasses(message, statusDiv) {
    // delete unnecessary classes
    message.className = '';
    statusDiv.className = 'invoice-status';
}
