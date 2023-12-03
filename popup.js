// popup.js
document.getElementById('generate').addEventListener('click', function() {
    // Call the backend to generate a password
    fetch('http://localhost:5000/generate_password?length=20')
      .then(response => response.json())
      .then(data => {
        document.getElementById('password').innerText = data.password;
      });
  });