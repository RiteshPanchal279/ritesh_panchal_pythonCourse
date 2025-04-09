// Write a program that reads the JSON object and dynamically creates an HTML
// page to display the user's information with the below following details:
// ● A heading displaying "User Information"
// ● A section to display user details (Name, Age, Email)
// ● Takes a JSON object containing user information.
// ● Dynamically creates HTML elements to display the user's name, age, and email.
// ● Appends the created elements to the HTML page.
// Use an external stylesheet or bootstrap for styling.

const user = {
   name: "Ritesh Panchal",
   age: 21,
   email: "riteshp@example.com"
 };
 
 // Get the container
 const container = document.getElementById("user-info");
 
 // Create and append user details
 const nameEl = document.createElement("p");
 nameEl.innerHTML = `<strong>Name:</strong> ${user.name}`;
 nameEl.classList.add("mb-2");
 
 const ageEl = document.createElement("p");
 ageEl.innerHTML = `<strong>Age:</strong> ${user.age}`;
 ageEl.classList.add("mb-2");
 
 const emailEl = document.createElement("p");
 emailEl.innerHTML = `<strong>Email:</strong> ${user.email}`;
 emailEl.classList.add("mb-0");
 
 // Append to container
 container.appendChild(nameEl);
 container.appendChild(ageEl);
 container.appendChild(emailEl);