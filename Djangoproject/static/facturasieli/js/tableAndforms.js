/*
#============================================================================#
#                    F a c t u r a S i e l i   ( 2 0 2 4 )                   #
#============================================================================#
# File   : static/facturasieli/js/tableAndforms.js                                 #
# Author : Morice                                   #
#============================================================================#    
*/

document.addEventListener('DOMContentLoaded', function() {

    var passwordField = document.querySelector('#id_password1'); 
    var otpForm = document.getElementById('otp-form')
    var searchForm = document.getElementById('search-form')

    // clickable table row function
    makeRowsClickable();
    
    // catch the event when user is typing the password to show the guide
    if (passwordField) {
        passwordField.addEventListener('keyup', showPasswordGuide);
    }
    // catch the event when user on page otp validation to autosubmit
    if (otpForm) {
        var otpField = document.querySelector('#id_otp')
        otpField.focus
        otpField.addEventListener('keyup', function(e) {            
            autosubmitionOtp(e,otpForm);
        })
    }

    // catch the event when user is on search company page, creating new ServiceWorker, to autosubmit
    if (searchForm) {
        var searchField = document.querySelector('#id_search')
        searchField.focus()
        searchField.addEventListener('keyup',function() {
            autosubmitSearch(searchForm);
        })
    }
});

function showPasswordGuide() {
    var passwordField = document.querySelector('#id_password1');
    var pwdValue = passwordField.value
    var guide = document.getElementById('pwd-param-guide')
    
    // Regular expressions for validation
    var minLength = /.{10,}/;  // At least 10 characters
    var uppercase = /[A-Z]/;   // At least one uppercase letter
    var lowercase = /[a-z]/;   // At least one lowercase letter
    var number = /[0-9]/;      // At least one digit
    var specialChar = /[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};':"\\|,.<>\/?]+/;  // At least one special character

    //tests
    var minLengthValid = minLength.test(pwdValue)
    var uppercaseValid = uppercase.test(pwdValue)
    var lowercaseValid = lowercase.test(pwdValue)
    var numberValid = number.test(pwdValue)
    var specialCharValid = specialChar.test(pwdValue)

    // Display the password strength guide
    guide.innerHTML = `
    <p>Password must contain:</p>
    <ul>
        <li style="color: ${minLengthValid ? 'green' : 'red'};">At least 10 characters</li>
        <li style="color: ${uppercaseValid ? 'green' : 'red'};">At least one uppercase letter</li>
        <li style="color: ${lowercaseValid ? 'green' : 'red'};">At least one lowercase letter</li>
        <li style="color: ${numberValid ? 'green' : 'red'};">At least one number</li>
        <li style="color: ${specialCharValid ? 'green' : 'red'};">At least one special character @$!%*?&#</li>
    </ul>`;
}

function autosubmitionOtp(e,otpForm) {
    
    var otpField = e.target;
    if (otpField.value.length == 6) {
        setTimeout(() => {
            otpForm.submit() 
        }, 500);
    }
}
// funtion which get company informations from search view thx to ajax and display them in table
function autosubmitSearch(searchForm) {
    var formData = new FormData(searchForm);
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(searchForm.action, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'x-requested-with': 'XMLHttpRequest'
        },
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Form submission error");
        }
        return response.json();  // Nous attendons un JSON en retour
    })
    .then(data => {
        // Remplace le contenu du tableau des résultats avec le HTML
        if (data.table) {
            document.getElementById('company-results').innerHTML = data.table;
            makeRowsClickable();
        }
    })
    .catch(error => console.error('Erreur:', error));
}

// Fonction pour rendre les lignes du tableau cliquables
function makeRowsClickable() {
    var rows = document.querySelectorAll(".clickable-row");
    rows.forEach(function(row) {
        row.addEventListener("click", function() {
            window.location.href = row.dataset.href;
        });
    });
}