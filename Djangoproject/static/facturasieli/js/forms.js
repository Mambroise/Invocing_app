/*
#============================================================================#
#                    F a c t u r a S i e l i   ( 2 0 2 4 )                   #
#============================================================================#
# File   : static/facturasieli/js/forms.js                                 #
# Author : Morice                                   #
#============================================================================#    
*/

document.addEventListener('DOMContentLoaded', function() {
    var passwordField = document.querySelector('#id_password1'); 
    
    if (passwordField) {
        passwordField.addEventListener('keyup', showPasswordGuide);
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
        <li style="color: ${specialCharValid ? 'green' : 'red'};">At least one special character</li>
    </ul>`;
}