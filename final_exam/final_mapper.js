"use strict";


function createAndAppendImg(mapNumber) {
    let imgElem = document.createElement('img');
    imgElem.id = "map";
    imgElem.alt = "";
    imgElem.src = `images/final_sky${mapNumber}.png`
    document.getElementById('mapContainer').appendChild(imgElem);
};


document.getElementById("viewBtn").addEventListener("click", function () {
    let mapNumber = parseInt(document.getElementById("mapNum").value);
    if (mapNumber < 0 || mapNumber > 23) {
        alert("Invalid number. Please enter a number between 0 and 23.");
        return;
    };
    const imgElem = document.getElementById("map");
    if (imgElem) {
        imgElem.remove();
    };
    createAndAppendImg(mapNumber);
});

let today = new Date();
let strDate = today.toLocaleDateString();
document.getElementById("timeStamp").innerHTML = strDate;
let month = today.getMonth() + 1;
let hour = today.getHours();
let mapNumber = (2 * month + hour) % 24;
createAndAppendImg(mapNumber);