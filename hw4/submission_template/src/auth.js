function login() {
    var user = document.getElementById('user').value;
    var pass = document.getElementById('pass').value;
    if (user != 'nyc' && pass != 'iheartnyc') {
        alert('Invalid user or pass');
    } else {
        //Redirecting to other page or webste code or you can set your own html page.
        window.history.pushState(null, null, '/nyc_dash');
        // window.history.pushState(
        //     { html: response.html, pageTitle: response.pageTitle },
        //     '',
        //     '/nyc_dash'
        // );
    }
}
//Reset Inputfield code.
function clearFunc() {
    document.getElementById('email').value = '';
    document.getElementById('pwd1').value = '';
}
