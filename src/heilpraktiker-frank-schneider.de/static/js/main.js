function toggleNavbar() {
  var n = document.getElementById("navbar-small");
  if (n.className.indexOf("w3-show") == -1) {
    n.className += " w3-show";
  } else {
    n.className = n.className.replace(" w3-show", "");
  }
}
