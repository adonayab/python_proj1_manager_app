function myFunction() {
  var password = document.querySelector(".passwordElement");
  if (password.type === "password") {
    password.type = "text";
  } else {
    password.type = "password";
  }
}