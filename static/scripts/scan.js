window.image = undefined

document.getElementById("image-upload").onchange = () => {
    image = new Image()

    image.onload = () => {
        document.getElementById("image-preview").src = image.src
        window.image = image.src
    }

    image.onerror = () => {
        document.getElementById("image-preview").src = "/static/images/invalid-image.png"
        window.image = undefined
    }

    image.src = URL.createObjectURL(document.getElementById("image-upload").files[0])
}

function store_image () {
    if (window.image == undefined) {
        alert("Please add a file before submitting.")
    }

    else {
        file = document.getElementById("image-upload").files[0]

        file_reader = new FileReader()
        file_reader.readAsDataURL(file)
        file_reader.onload = () => {
            localStorage["xray"] = file_reader.result
            window.location = "/result"
        }
    }
}