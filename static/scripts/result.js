links = {
    "Atelectasis": "https://www.mayoclinic.org/diseases-conditions/atelectasis/symptoms-causes/syc-20369684",
    "Consolidation": "https://www.healthhype.com/consolidation-in-lung-signs-symptoms-and-causes.html",
    "Infiltration": "https://healthjade.net/lung-infiltrates/",
    "Pneumothorax": "https://www.mayoclinic.org/diseases-conditions/pneumothorax/symptoms-causes/syc-20350367",
    "Edema": "https://www.mayoclinic.org/diseases-conditions/edema/symptoms-causes/syc-20366493",
    "Emphysema": "https://www.mayoclinic.org/diseases-conditions/emphysema/symptoms-causes/syc-20355555",
    "Fibrosis": "https://www.mayoclinic.org/diseases-conditions/pulmonary-fibrosis/symptoms-causes/syc-20353690",
    "Effusion": "https://my.clevelandclinic.org/health/diseases/17373-pleural-effusion-causes-signs--treatment",
    "Pneumonia": "https://www.mayoclinic.org/diseases-conditions/pneumonia/symptoms-causes/syc-20354204",
    "Pleural Thickening": "https://www.mesothelioma.com/asbestos-cancer/pleural-thickening/",
    "Cardiomegaly": "https://www.mayoclinic.org/diseases-conditions/enlarged-heart/symptoms-causes/syc-20355436",
    "Nodule": "https://www.mayoclinic.org/diseases-conditions/thyroid-nodules/symptoms-causes/syc-20355262",
    "Mass": "https://www.verywellhealth.com/lung-mass-possible-causes-and-what-to-expect-2249388",
    "Hernia": "https://www.mayoclinic.org/diseases-conditions/inguinal-hernia/symptoms-causes/syc-20351547",
    "Lung Lesion": "https://www.tandurust.com/respiratory-lung-disease/what-is-a-lung-lesion.html",
    "Fracture": "#",
    "Lung Opacity": "#",
    "Enlarged Cardiomediastinum": "#"
}

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
        if (pathology == "error") {
            result = "<h3>An unexpected error occured!</h3><p>Please submit a bug report in the "
            result += `<a href="">issue tracker</a>, the error message is:</p><code>${result_data["error"]}</code>`
        }

        else {
            link = links[pathology]
            probability = (result_data[pathology]*100).toFixed(2)

            result += `<div class="row"><div class="col"><p><strong><a class="pathology" href="${link}">${pathology}</a></strong> `
            result += `- ${probability}%</div><div class="col"><div class="progress w-30"></p><div class="progress-bar" role="progressbar"`
            result += ` style="width:${probability}%;"></div></div></div></div>`
        }
    }

    document.getElementById("data").innerHTML = result
})  