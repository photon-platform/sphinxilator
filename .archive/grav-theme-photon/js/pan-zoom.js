//panning on mousemove in section
var elements = document.querySelectorAll(".pan");
for (var i = 0; i < elements.length; i++) {

  elements[i].addEventListener("mousemove", function(e) {
    sW = this.offsetWidth;
    sH = this.offsetHeight;

    x = (110 * e.offsetX / sW);
    x-= x*.05
    y = (110 * e.offsetY / sH);
    y-= y*.05

    cursor = `${x}% ${y}%`;
    // console.log(cursor);
    this.querySelector('img').style.objectPosition = cursor;
  });

  elements[i].addEventListener("mouseleave", function(e) {
    this.querySelector('img').style.objectPosition = "50% 50%";

  });
}
