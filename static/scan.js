window.image = undefined

document.getElementById("image-upload").onchange = () => {
    image = new Image()

    image.onload = () => {
        document.getElementById("image-preview").src = image.src
        window.image = image.src
    }

    image.onerror = () => {
        document.getElementById("image-preview").src = "/static/invalid-image.png"
        window.image = undefined
    }

    image.src = URL.createObjectURL(document.getElementById("image-upload").files[0])
}

function store_image () {
    if (window.image == undefined) {
        alert("Please add a file before submitting.")
    }

    else {
        localStorage["xray"] = window.image
        window.location = "/result"
    }
}