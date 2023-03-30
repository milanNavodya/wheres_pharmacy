function showMenu() {
  document.getElementById("dropdown-menu").classList.add("show");
}

function hideMenu() {
  document.getElementById("dropdown-menu").classList.remove("show");
}

function logout() {
  window.location.href = '/logout';
}