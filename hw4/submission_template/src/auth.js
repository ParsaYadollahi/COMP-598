function login() {
    var user = document.getElementById('user').value;
    var pass = document.getElementById('pass').value;
    if (user != 'nyc' && pass != 'iheartnyc') {
        alert('Invalid user or pass');
    } else {
        alert(
            'Thank You for Login & You are Redirecting to Campuslife Website'
        );
        //Redirecting to other page or webste code or you can set your own html page.
        window.history = 'https://www.campuslife.co.in';
        window.history.pushState(
            { html: response.html, pageTitle: response.pageTitle },
            '',
            '/nyc_dash'
        );
    }
}
//Reset Inputfield code.
function clearFunc() {
    document.getElementById('email').value = '';
    document.getElementById('pwd1').value = '';
}
