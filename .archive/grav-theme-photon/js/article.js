// collect listing articles
// var articles = document.querySelectorAll(".showcase article, .welcome article, .featured article, .index main article, .archive main article")
var articles = document.querySelectorAll(".excerpt")

// set click event for search
articles.forEach( article => {
  if (article.dataset.url) {
    article.addEventListener("click", function(e) {
      location.href = article.dataset.url;
    })
  }
})

/////////////////////////////////////////////
var figure = document.querySelector("body > main > article > figure")
if(figure) {
  // console.log("set figure: " + figure.classList.contains("fc")  );
  if(!document.querySelector("body.calendar")){
    figure.addEventListener("click", modalFigure );
  }
}
function modalFigure(e) {
  figure.classList.toggle("modal");
}


/////////////////////////////////////////////
var gallery = document.querySelector("body > main > article > .gallery")
var galleryPanel
var galleryFigures

if(gallery) {
  galleryPanel = gallery.querySelector(".panel")
  galleryFigures = gallery.querySelectorAll("figure");
  gallery.addEventListener("click", modalGallery );
  // galleryPanel.addEventListener("click", modalGallery );
  galleryFigures.forEach( figure => {
      figure.addEventListener("mouseenter", mouseoverGalleryFigure );
  })
}

function modalGallery() {
  gallery.classList.toggle("modal");
}

function mouseoverGalleryFigure(e) {
  galleryPanel.style.background = 'white url(' + e.target.dataset.image + ')';
  galleryPanel.style.backgroundSize = 'contain';
  galleryPanel.style.backgroundRepeat = 'no-repeat';
  galleryPanel.style.backgroundPosition = 'center';
}


/////////////////////////////////////////////
var collection = document.querySelector(".collection")
function toggleCollection() {
  collection.classList.toggle("modal");
}

function collectionExpand(event) {
  event.target.parentElement.parentElement.parentElement.classList.toggle("expand");
  console.log(event.target.checked);
  // if (event.target.checked) {
    // alert('checked');
  // } else {
    // alert('not checked');
  // }
}

var collections = document.querySelectorAll(".collection");
collections.forEach( collection => {
  var expand = collection.querySelector(".expand");
  expand.addEventListener("change", collectionExpand );
})
