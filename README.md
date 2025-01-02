# PyLock - Password Manager

## Project Description
PyLock is a password manager that allows users to securely store and retrieve their passwords. It uses encryption to ensure that the stored passwords are safe and protected.

## Technologies Used
- Python
- Flask
- Cryptography
- Materialize CSS

## How to Run the Project
1. Clone the repository:
   ```
   git clone https://github.com/harshil748/PyLock.git
   ```
2. Navigate to the project directory:
   ```
   cd PyLock
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```
   python main.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000` to access the password manager.

## Usage Instructions
### Adding a Password
1. Open the password manager in your web browser.
2. Fill in the "Service", "Username", and "Password" fields in the "Add Password" form.
3. Click the "Add Password" button.
4. A message will appear indicating that the password has been added successfully.

### Retrieving a Password
1. Open the password manager in your web browser.
2. Fill in the "Service" field in the "Retrieve Password" form.
3. Click the "Get Password" button.
4. A message will appear displaying the username and password for the specified service.

### Generating a TOTP
1. Open the password manager in your web browser.
2. Click the "Generate TOTP" button to navigate to the TOTP generation page.
3. Fill in the "Service" field in the "Generate TOTP" form.
4. Click the "Generate TOTP" button.
5. The TOTP for the specified service will be displayed.

## Requirements Elicitation
To understand the requirements for PyLock, we used several techniques including design interviews, record reviews, brainstorming sessions, questionnaires, and observation. For more details, please refer to the [Requirements Elicitation Document](requirements_elicitation.md).

## Future Improvements and Contributions
- Add user authentication to enhance security.
- Implement password strength validation.
- Add support for password categories and tags.
- Improve the user interface and user experience.

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request or open an issue.
