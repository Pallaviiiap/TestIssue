document.getElementById('loginButton').addEventListener('click', function() {
    const button = this;
    button.disabled = true;
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const csrf_token = document.getElementById('csrf_token').value;
    
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}&csrf_token=${encodeURIComponent(csrf_token)}`
    })
    .then(response => response.text())
    .then(html => {
        document.body.innerHTML = html;
    })
    .catch(error => {
        console.error('Error:', error);
    })
    .finally(() => {
        button.disabled = false;
    });
});