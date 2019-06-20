function showHidePassFunc(page) {
  if (page === 'login') {
    let password = document.querySelector(".passwordElement");
    if (password.type === "password") {
      password.type = "text";
    } else {
      password.type = "password";
    }
  } else if (page === 'register') {
    let password = document.querySelector(".passwordElement");
    let password2 = document.querySelector(".passwordElement2");
    if (password.type === "password" && password2.type === 'password') {
      password.type = "text";
      password2.type = "text";
    } else {
      password.type = "password";
      password2.type = "password";
    }
  }
}