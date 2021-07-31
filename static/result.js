function fetch_data () {
    fetch(
        "/api/scan-xray",
        {method: "POST",
         body: JSON.stringify(
         {"image": localStorage["xray"]}
         )})
    .then(response => response.text())
    .then(text => document.getElementById("data").innerHTML = text)
}