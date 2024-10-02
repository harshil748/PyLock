document.getElementById('add-password-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('/add_password', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        alert('Error: ' + error.message);
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
            alert('Username: ' + data.username + '\nPassword: ' + data.password);
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        alert('Error: ' + error.message);
    });
});
