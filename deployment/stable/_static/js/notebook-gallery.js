document.addEventListener("DOMContentLoaded", function () {
  var setURLFilters = function (filters) {
    var newAdditionalURL = "";
    var tempArray = window.location.href.split("?");
    var baseURL = tempArray[0];
    var additionalURL = tempArray[1];
    var temp = "";
    if (additionalURL) {
      tempArray = additionalURL.split("&");
      for (var i = 0; i < tempArray.length; i++) {
        if (tempArray[i].split("=")[0] != "filters") {
          newAdditionalURL += temp + tempArray[i];
          temp = "&";
        }
      }
    }
    if (filters.length) {
      newAdditionalURL += temp + "filters=" + filters.join(",");
    }
    if (newAdditionalURL) {
      window.history.replaceState("", "", baseURL + "?" + newAdditionalURL);
    } else {
      window.history.replaceState("", "", baseURL);
    }
  };

  var getUrlFilters = function () {
    let search = new URLSearchParams(window.location.search);
    let filters = search.get("filters");
    if (filters) {
      return filters.split(",");
    }
  };

  var tagFilterListener = function () {
    // Get filter checkbox status
    filterTagRoots = []; // Which sections are we filtering on
    filterTags = []; // Which tags are being selected
    Array.from(document.getElementsByClassName("tag-filter")).forEach(
      (checkbox) => {
        if (checkbox.checked) {
          let tag = checkbox.getAttribute("id");
          filterTags.push(checkbox.getAttribute("id"));
          let root = tag.split("/")[0];
          if (!filterTagRoots.includes(root)) {
            filterTagRoots.push(root);
          }
        }
      }
    );

    setURLFilters(filterTags);

    // Iterate notebook cards
    Array.from(document.getElementsByClassName("sd-col")).forEach(
      (notebook) => {
        let isFiltered = false;

        // Get tags from the card
        let tags = [];
        Array.from(notebook.getElementsByClassName("sd-badge")).forEach(
          (tag) => {
            tags.push(tag.getAttribute("aria-label"));
          }
        );

        // Iterate each of the sections we are filtering on
        filterTagRoots.forEach((rootTag) => {
          // If a notebook has no tags with the current root tag then it is definitely filtered
          if (
            !tags.some((tag) => {
              return tag.startsWith(rootTag);
            })
          ) {
            isFiltered = true;
          } else {
            // Get filter tags with the current root we are testing
            let tagsWithRoot = [];
            filterTags.forEach((filteredTag) => {
              if (filteredTag.startsWith(rootTag)) {
                tagsWithRoot.push(filteredTag);
              }
            });

            // If the notebook tags and filter tags don't intersect it is filtered
            if (!tags.some((item) => tagsWithRoot.includes(item))) {
              isFiltered = true;
            }
          }
        });

        // Show/hide the card
        if (isFiltered) {
          notebook.setAttribute("style", "display:none !important");
        } else {
          notebook.setAttribute("style", "display:flex");
        }
      }
    );
  };

  // Add listener for resetting the filters
  let resetButton = document.getElementById("resetfilters");
  if (resetButton != undefined) {
    resetButton.addEventListener(
      "click",
      function () {
        Array.from(document.getElementsByClassName("tag-filter")).forEach(
          (checkbox) => {
            checkbox.checked = false;
          }
        );
        tagFilterListener();
      },
      false
    );
  }

  // Add listeners to all checkboxes for triggering filtering
  Array.from(document.getElementsByClassName("tag-filter")).forEach(
    (checkbox) => {
      checkbox.addEventListener("change", tagFilterListener, false);
    }
  );

  // Simplify tags and add class for styling
  // It's not possible to control these attributes in Sphinx otherwise we would
  Array.from(document.getElementsByClassName("sd-badge")).forEach((tag) => {
    tag.setAttribute("aria-label", tag.innerHTML);
    try {
      tag
        .getAttribute("aria-label")
        .split("/")
        .forEach((subtag) => tag.classList.add(`tag-${subtag}`));
    } catch (err) {}

    if (tag.innerHTML.includes("/")) {
      tag.innerHTML = tag.innerHTML.split("/").slice(1).join("/");
    }
  });

  // Set checkboxes initial state
  var initFilters = getUrlFilters();
  if (initFilters) {
    Array.from(document.getElementsByClassName("tag-filter")).forEach(
      (checkbox) => {
        if (initFilters.includes(checkbox.id)) {
          checkbox.checked = true;
        }
      }
    );
    tagFilterListener();
  }
});
