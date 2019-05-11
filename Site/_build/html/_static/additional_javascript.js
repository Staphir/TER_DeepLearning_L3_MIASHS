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
    let div_video = document.getElementById("youtube-shift-it");
    if (div_video){
        let width = "500"; let height = "300";
        let allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";
        let frameborder = "0";
        div_video.removeChild(div_video.lastElementChild);

        let iframe = document.createElement("iframe");
        iframe.width = width; iframe.height = height;
        iframe.allow = allow; iframe.frameBorder = frameborder;
        iframe.allowfullscreen = true;
        iframe.src = "https://www.youtube.com/embed/pCwELYqLAGg";

        div_video.appendChild(iframe);
    }
};