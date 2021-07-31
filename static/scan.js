function store_image () {
    file = document.getElementById("image-upload").files[0]

    if (file == undefined) {
        alert("Please add a file before submitting.")
    }

    else {
        file_reader = new FileReader()
        file_reader.readAsDataURL(file)
        file_reader.onload = () => {
            localStorage["xray"] = file_reader.result
            window.location = "/result"
        }
    }
}