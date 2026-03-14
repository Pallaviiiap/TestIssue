document.getElementById('loginButton').addEventListener('click', function() {
    const button = this;
    button.disabled = true;
    
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    
    if (!username || !password) {
        alert('Please fill in both fields with non-whitespace characters.');
        button.disabled = false;
        return;
    }
    
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
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