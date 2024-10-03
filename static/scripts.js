document.getElementById('add-password-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('/add_password', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        M.toast({html: data.message});
    })
    .catch(error => {
        M.toast({html: 'Error: ' + error.message});
    });
});

document.getElementById('get-password-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('/get_password', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.username && data.password) {
            M.toast({html: 'Username: ' + data.username + '<br>Password: ' + data.password});
        } else {
            M.toast({html: data.message});
        }
    })
    .catch(error => {
        M.toast({html: 'Error: ' + error.message});
    });
});

document.getElementById('totp-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('/generate_totp', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.totp) {
            document.getElementById('totp-result').style.display = 'block';
            document.getElementById('totp-value').textContent = data.totp;
        } else {
            M.toast({html: data.message});
        }
    })
    .catch(error => {
        M.toast({html: 'Error: ' + error.message});
    });
});

// Add animations and transitions
document.querySelectorAll('.card').forEach(card => {
    card.style.opacity = 0;
    card.style.transition = 'opacity 0.5s ease-in-out';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'transform 0.5s ease-in-out';
    setTimeout(() => {
        card.style.opacity = 1;
        card.style.transform = 'translateY(0)';
    }, 100);
});
