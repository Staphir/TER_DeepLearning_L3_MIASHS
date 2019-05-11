window.onload=function(){

// -----------ajout biblio et à propos en bas de page----------------
    let sourcelink = document.getElementById("sourcelink");
// Bibliographie
    let aBiblio = document.createElement("a");
    let aBiblioText = document.createTextNode(" | Bibliographie");
    aBiblio.appendChild(aBiblioText);
    aBiblio.id = "sidebarBibliographie";
    aBiblio.class = "sidebarFixedLinks";
    aBiblio.href = "bibliographie.html";
    sourcelink.appendChild(aBiblio);

// A propos
    let aProp = document.createElement("a");
    let aPropText = document.createTextNode(" | A propos");
    aProp.appendChild(aPropText);
    aProp.id = "sidebarPropos";
    aProp.class = "sidebarFixedLinks";
    aProp.href = "a_propos.html";
    sourcelink.appendChild(aProp);


//------ajout video youtube du shift it dans la page notre programme-------
    let div_video = document.getElementById("exemple-du-shift-it-sur-android");
    if (div_video) {
        let width = "500";
        let height = "300";
        let src = "../../pictures/ShiftItAndroid.mp4";
        // div_video.removeChild(div_video.lastElementChild);

        let video = document.createElement("video");
        video.width = width;
        video.height = height;
        video.align = "center";
        video.autoplay = true;
        video.loop = true;

        let source = document.createElement("source");
        source.src = src;
        source.type = "video/mp4";
        video.appendChild(source);

        div_video.replaceChild(video, div_video.children[0]);

    }
};