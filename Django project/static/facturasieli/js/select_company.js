/*
#============================================================================#
#                    F a c t u r a S i e l i   ( 2 0 2 4 )                   #
#============================================================================#
# File   : static/facturasieli/notification/js/select_company.js               #
# Author : Morice                                          #
#============================================================================#    
*/

document.addEventListener("DOMContentLoaded", function() {
    var rows = document.querySelectorAll(".clickable-row");
    rows.forEach(function(row) {
        row.addEventListener("click", function() {
            window.location.href = row.dataset.href;
        });
    });
});
