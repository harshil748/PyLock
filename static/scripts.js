document
  .getElementById("add-password-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch("/add_password", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        M.toast({ html: data.message });
      })
      .catch((error) => {
        M.toast({ html: "Error: " + error.message });
      });
  });

document
  .getElementById("get-password-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch("/get_password", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.username && data.password) {
          M.toast({
            html:
              "Username: " + data.username + "<br>Password: " + data.password,
          });
        } else {
          M.toast({ html: data.message });
        }
      })
      .catch((error) => {
        M.toast({ html: "Error: " + error.message });
      });
  });

document.getElementById;
