let pElement = document.getElementById("target");

pElement.onclick = newStyle


function newStyle() {
          console.log("in function newStyle")
          let newColor = '';
          let newFont = '';
          var element = document.getElementById('target');
          element.style.color = "purple";
          element.style.fontFamily = "impact"
}