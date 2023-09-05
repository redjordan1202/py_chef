function expand_navbar() {
    dropdown = document.getElementById("navbar-dropdown");
    console.log("clicked")
    if (dropdown.classList.contains("hidden")) {
        dropdown.classList.remove("hidden");
        dropdown.style.display = "flex";
    } else {
        dropdown.classList.add("hidden");
        dropdown.style.display = '';
    }
}

function navbar_set_events() {
    console.log("setting events")
    navbar_expand = document.getElementsByClassName("navbar-expand");
    for (let x of navbar_expand) {
        x.addEventListener("click", expand_navbar);
    }
}
