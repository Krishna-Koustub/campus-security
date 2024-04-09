document.addEventListener('DOMContentLoaded', function () {
  // Handling navigation clicks
  const navLinks = document.querySelectorAll('nav ul li a');
  navLinks.forEach(link => {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      showSection(targetId);
    });
  });

  // Function to show a specific section
  function showSection(sectionId) {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
      section.classList.remove('show');
      if (section.id === sectionId) {
        section.classList.add('show');
      }
    });
  }

  // Handling form submissions (just console log for demo)
  const loginForm = document.getElementById('loginForm');
  loginForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    console.log('Login:', username, password);
  });

  const signupForm = document.getElementById('signupForm');
  signupForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const newUsername = document.getElementById('newUsername').value;
    const newPassword = document.getElementById('newPassword').value;
    console.log('Signup:', newUsername, newPassword);
  });
});
