document.onload = function() {
   
   window.resizeTo(550, 850);
   
   
}
function updateTitle(title) {
   document.title = title
}

function createItem2(monitorData, name) {
   
   printnow("createItem2" + monitorData);
   createItem3(monitorData, name);
}
function createItem3(monitorData, name) {
   // var title = document.title;


   // printnow("python title " + name);
   // printnow("js title" + title);

   // if (name == title) {
   //    printnow("if name == window.name");
   // }
   // else if (title == "" && name == "init") {
   //    printnow("if name || window.name");
      
   // }
   // else {
   //    printnow("returned");

   //    return
   // }
   // printnow(monitorData[0])
   // insert row and column, problem?
   var date = new Date().toLocaleTimeString();
   if (monitorData.length == 0) {
      monitorData = ["Monitor Started", 'https://amonitor.org', 'icons/tease.jpg', '$30/3']
   }
   

   // set cell data 
   $('#items').prepend('<div class="parent"> ' + 
                           '<div class="productName">' + 
                              '<h3 id="name" style="position: relative;">' + monitorData[0] + '</h3>' + 
                              '<h2 style="margin-right: 3%; margin-left: auto;">Stock: <span style="color: white; margin-right: 0; margin-left: auto;">N/A</span></h2>' +  
                           '</div> ' + 
                           '<div class="controls"> ' + 
                              '<button class="icon" onclick="test2();"><i class="fas fa-play"></i></button> ' + 
                              '<button class="icon"><i class="fas fa-link"></i></button> ' +
                              '<button class="icon"><i class="far fa-clipboard"></i></button> ' +
                              '<button class="icon"><i class="fas fa-dollar-sign"></i></button> ' + 
                              '<div class="link"> ' + 
                                 '<h4>' + monitorData[1] + '</h4> ' + 
                              '</div> ' + 
                              '<div class="other"> ' + 
                                 '<h2 style="float: left;">Price: <span style="color: white; ">' + monitorData[3] + '</span></h2> ' + 
                                 '<h2 style="margin-left: 58%; ">Time: <span style="color: white;">' + date + '</span></h2> ' + 
                              '</div> ' + 
                           '</div> ' + 
                           '<div class="imagePlace">' + 
                              '<img src="' + monitorData[2] + '"  class="image" > ' + 
                           '</div> ' + 
                        '</div>');
   
   
}

function printnow(data) {
   jQuery.getScript("index.js",function(){
      printnow(data);
      });
}


function setSnackbar2(status){
   
   var element = document.getElementById("snackbar2");
   element.innerHTML = status;
   showSnackbar2();
}
function showSnackbar2() {
   // Get the snackbar DIV
   var x2 = document.getElementById("snackbar2");
   
   // Add the "show" class to DIV
   x2.className = "show";
   
   // After 3 seconds, remove the show class from DIV
   setTimeout(function(){ x2.className = x2.className.replace("show", ""); }, 3000);
   }

function changeName2 (name) {
   document.querySelector('title').textContent = name
}  