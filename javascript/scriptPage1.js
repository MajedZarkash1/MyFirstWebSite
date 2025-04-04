
// this funtion to change the color of the backgorund and here the background is the content //

const button = document.querySelector("#content-buton");
let content = document.querySelector("#content");
let colors = ['rgb(171, 171, 171)', 'rgb(252, 252, 252)', 'rgb(228, 235, 241)'];// this is a list  for changing the color //
let currentcolorindex = 0;


function changecolor() {
    content.style.background = colors[currentcolorindex];
    currentcolorindex = [currentcolorindex +1] % colors.length; // this works like a loop//

}

button.addEventListener("click", changecolor);