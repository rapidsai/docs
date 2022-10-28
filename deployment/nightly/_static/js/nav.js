document.addEventListener("DOMContentLoaded", function () {
  let sidebar = document.getElementsByClassName("bd-sidebar-primary")[0];
  sidebar.innerHTML =
    `
    <div id="rapids-pydata-container">
        <div class="rapids-home-container">
            <a class="rapids-home-container__home-btn" href="/">Home</a>
        </div>
        <div class="rapids-selector__container rapids-selector--hidden">
            <div class="rapids-selector__selected">deployment</div>
            <div class="rapids-selector__menu" style="height: 65px;">
                <a class="rapids-selector__menu-item rapids-selector__menu-item--selected" href="https://docs.rapids.ai/deployment">deployment</a>
                <a class="rapids-selector__menu-item" href="https://docs.rapids.ai/api">api docs</a>
            </div>
        </div>
        <div id="rapids-selector__container-version" class="rapids-selector__container rapids-selector--hidden">
            <div class="rapids-selector__selected"></div>
            <div class="rapids-selector__menu" style="height: 65px;">
                <a class="rapids-selector__menu-item" href="https://docs.rapids.ai/deployment/nightly">nightly</a>
                <a class="rapids-selector__menu-item" href="https://docs.rapids.ai/deployment/stable">stable</a>
            </div>
        </div>
    </div>
    ` + sidebar.innerHTML;

  let versionSection = document.getElementById(
    "rapids-selector__container-version"
  );
  let selectorSelected = versionSection.getElementsByClassName(
    "rapids-selector__selected"
  )[0];
  if (window.location.href.includes("/deployment/stable")) {
    selectorSelected.innerHTML = "stable";
    versionSection
      .getElementsByClassName("rapids-selector__menu-item")
      .forEach((element) => {
        if (element.innerHTML.includes("stable")) {
          element.classList.add("rapids-selector__menu-item--selected");
        }
      });
  } else if (window.location.href.includes("/deployment/nightly")) {
    selectorSelected.innerHTML = "nightly";
    versionSection
      .getElementsByClassName("rapids-selector__menu-item")
      .forEach((element) => {
        if (element.innerHTML.includes("nightly")) {
          element.classList.add("rapids-selector__menu-item--selected");
        }
      });
  } else {
    selectorSelected.innerHTML = "dev";
    let menu = versionSection.getElementsByClassName(
      "rapids-selector__menu"
    )[0];
    menu.innerHTML =
      menu.innerHTML +
      '<a class="rapids-selector__menu-item rapids-selector__menu-item--selected" href="/">dev</a>';
    menu.style["height"] = "97px";
  }
});
