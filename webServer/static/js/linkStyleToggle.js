/*
This script is used to toggle the style of one link at the time with an array of links.
Eksample: you have an array of links with an iframe as target. It can be usefull to have
the link coresponding to the content shown in the iframe light up.
*/

// SETTINGS
const defaultClass = "deactive";    // Default class name.
const activeClass = "active";       // Active class name.
const defaultLinkId = "default";    // The element id too activate at start.

// Makes a HTMLCollection of our selected elements.
const HtmlCollection = document.getElementsByClassName(defaultClass);
// Makes an array for our link elements.
const linkArray = [];
/*
Pushes the link elements from HTMLCollection to linkArray.
[WARNING!] Using the elements directly from HTMLCollection causes all sorts of problems.
*/
for (let index = 0; index < HtmlCollection.length; index++) {
    linkArray.push(HtmlCollection[index]);
} 
// Sett selected element to default state.
function clearAll(x){
    x.className = defaultClass;
}
// Setts all elements to default state, then activates the selected element.
function activate(x){
    linkArray.forEach(clearAll);
    x.className = activeClass;
}
// Add event listeners to all the elements.
function setEventListners(x){
    x.addEventListener('click', function(){activate(x);});
}

// Main function.
function main(){
    // Adds event listeners to all elements in the array.
    linkArray.forEach(setEventListners);
    // If a default link is given clicks that link.
    if (defaultLinkId != null){document.getElementById(defaultLinkId).click();}
}
// Fires of main after DOM content is loaded.
document.addEventListener('DOMContentLoaded', main);
