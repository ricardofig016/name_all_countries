function sendInputToServer(inputValue) {
  function update_country_display_names(country_names) {
    var countryElements = document.getElementsByClassName("country-p");
    console.log(countryElements.length, country_names.length);
    for (let i = 0; i < country_names.length; i++) {
      countryElements[i].textContent = country_names[i];
    }

    document.getElementById("input").value = "";
  }

  fetch("/process_input", {
    method: "POST",
    body: JSON.stringify({ input_value: inputValue }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.modified) {
        update_country_display_names(data.countries);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

document.getElementById("input").addEventListener("input", function (event) {
  var inputValue = event.target.value;
  sendInputToServer(inputValue);
});
