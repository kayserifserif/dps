// panel
const checkboxes = document.querySelectorAll("input[type='checkbox']");
let highlights = new Set();
const minimap = document.getElementById("minimap");
let hrs;
// descriptions
const descriptions = document.getElementsByClassName("description");
const chars = document.getElementsByClassName("char");
// back to top
const backToTop = document.getElementById("backToTop");

// keep track of checked checkboxes
for (let checkbox of checkboxes) {
  if (checkbox.checked) {
    checkbox.parentElement.classList.add("checked");
    highlights.add(checkbox.value);
  }
}

// add classes to descriptions
for (let char of chars) {
  char.parentElement.classList.add("has-" + char.classList[1]);
}

// create minimap
for (let desc of descriptions) {
  let hr = document.createElement("hr");
  let [_, ...classes] = desc.classList;
  hr.classList.add("minimapLine", ...classes);
  minimap.appendChild(hr);
}
hrs = document.getElementsByClassName("minimapLine");

// checkbox event listener
for (let checkbox of checkboxes) {
  checkbox.addEventListener("change", event => {
    // update set
    checkbox.parentElement.classList.toggle("checked", checkbox.checked);
    checkbox.checked ? highlights.add(checkbox.value) : highlights.delete(checkbox.value);
    console.log(highlights);
    // fade the spans
    for (let el of document.getElementsByClassName(checkbox.value)) {
      el.classList.toggle("fade", !checkbox.checked);
    }
    // update minimap
    for (let hr of document.querySelectorAll(".minimapLine.has-" + checkbox.value)) {
      let isFade = true;
      for (let hl of highlights) {
        if (hr.classList.contains("has-" + hl)) {
          isFade = false;
          break;
        }
      }
      hr.classList.toggle("hrFade", isFade);
    }
  });
}

// back to top
backToTop.addEventListener("click", () => {
  window.scroll({
    top: 0,
    left: 0,
    behavior: "smooth"
  });
});