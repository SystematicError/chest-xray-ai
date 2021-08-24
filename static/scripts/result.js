document.getElementById("image-preview").src = localStorage["xray"]

fetch(
    "/api/scan-xray",
    {method: "POST",
    body: JSON.stringify(
        {"image": localStorage["xray"]}
)})
.then(response => response.json())
.then(result_data => {
    result = ""
    for (pathology in result_data) {
        result = result + `<strong>${pathology}</strong> - ${(result_data[pathology]*100).toFixed(2)}%<br>`
    }
    
    document.getElementById("data").innerHTML = result
})  