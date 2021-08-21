// get size on page load
// document.onload = function() {
//     setSnackbar("loaded page, firing function")
//     window.resizeTo(1025, 525);


// }
document.addEventListener('DOMContentLoaded', function() {
    
    window.resizeTo(1025, 525);
    getTable();
}, false);

eel.expose(print)
function printnow(print){
    eel.printnow(print);
}


function browserLoginPython(){

    eel.browserLogin();
    
}
function mirrorPython(){
    
    eel.mirror(806959633674928168);
}
function showSnackbar() {
// Get the snackbar DIV
var x = document.getElementById("snackbar");

// Add the "show" class to DIV
x.className = "show";

// After 3 seconds, remove the show class from DIV
setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

eel.expose(setConnection);
function setConnection(status){
    var element = document.getElementById("setConnection");
    element.innerHTML = status;
}
eel.expose(setSnackbar);
function setSnackbar(status){
    var element = document.getElementById("snackbar");
    element.innerHTML = status;
    showSnackbar();
}
function openCreate() {
document.getElementById("myNav").style.width = "100%";
}

function closeCreate() {
document.getElementById("myNav").style.width = "0%";
}
document.addEventListener("contextmenu", function(e){
e.preventDefault();
}, false);



eel.expose(pullChannels);
function pullChannels(){

    // document.getElementById("pullChannels").disabled = true;
    // document.getElementById('pullChannels').innerText = 'Please Wait . . .';


    $('#server'). empty();
    eel.pullChannels();


    ev = document.createEvent('Event');
    ev.initEvent('change', true, false);
    // el.dispatchEvent(ev);

    
}
eel.expose(updateChannel);
function updateChannel (channel) {

    $('#server').append($('<option>',
    {
        value: channel,
        text : channel
    }));

    // document.getElementById("pullChannels").disabled = false;
    // document.getElementById('pullChannels').innerText = "Refresh Channels"

}
eel.expose

function pullChannels_2 () {

    $('#channel'). empty();
    eel.pullChannels_2();

    ev = document.createEvent('Event');
    ev.initEvent('change', true, false);

}

eel.expose(updateChannels_2);
function updateChannels_2 (channel) {

    $('#channel').append($('<option>',
    {
        value: channel,
        text : channel
    }));
}
    
eel.expose(getServer);
function getServer () {

    var server = document.getElementById("server").value;
    return server

}


var rows = $('#monitors tr').length;

eel.expose(createTask);
function createTask () {

    // get all elements in the task creation page
    var name = document.getElementById("name").value;
    var type = document.getElementById("type").value;
    var server = document.getElementById("server").value;
    var channel = document.getElementById("channel").value;

    // create cells
    var table = document.getElementById("monitors");
    var row = table.insertRow(-1);
    var cell0 = row.insertCell(0);
    var cell1 = row.insertCell(1);
    var cell2 = row.insertCell(2);
    var cell3 = row.insertCell(3);
    var cell4 = row.insertCell(4);
    var cell5 = row.insertCell(5);

    // get rows of table for dynmaic idle active, will delete later
    var rows = $('#monitors tr').length;
    rows = rows - 1;

    var idle = document.getElementById('idle').innerHTML 
    idle++;

    document.getElementById('idle').innerHTML = idle; 
    document.getElementById('total').innerHTML = rows; 

    // insert data into cells
    cell0.innerHTML = name;
    cell1.innerHTML = server;
    cell2.innerHTML = channel;
    cell3.innerHTML = type;
    cell4.innerHTML = "idle";
    cell5.innerHTML = '<button class="action" onclick="startMonitor(' + rows + ');"><i class="fas fa-play"></i></button><button class="action" ><i class="fas fa-stop"></i></i></button><button class="action" ><i class="far fa-edit"></i></button><button class="action" onclick="deleteRow(this);"><i class="fas fa-trash"></i></button>';

    saveTable();
    

}

function deleteRow(row) {
    
    var i = row.parentNode.parentNode.rowIndex;
    document.getElementById("monitors").deleteRow(i);

    var rows = $('#monitors tr').length;
    rows = rows - 1;

    var idle = document.getElementById('idle').innerHTML 
    idle = idle - 1;

    if (rows == 0) {
        document.getElementById('idle').innerHTML = 0; 
        document.getElementById('total').innerHTML = 0;
        document.getElementById('active').innerHTML = 0; 
       
    }
    else {
        document.getElementById('idle').innerHTML = idle; 
        document.getElementById('total').innerHTML = rows;
    }

    localStorage.clear();
    saveTable();

  }




function saveTable () {

    // get number of rows of table
    var rows = document.getElementById("monitors").rows.length;
    // rows--;

    localStorage.clear();

    var data = ""
    
    
    for (i=1; i<rows; i++) {
        // iterate for number of rows

        for (x=0; x<4; x++) {   
            // get data from table
            var table = document.getElementById("monitors").rows[i].cells[x].innerHTML;
            
            
            // add to string
            if (data == "" || data.slice(-1) == "#") {
                data = data + table;
            }
            else {
                data = data + ',' + table;
            }
        }   
        // seperate rows
        data = data + '#'

    }
    // prevents weird table full of nothing
    
    printnow(data)

    while (true) {

        if (data.slice(-1) == '#') {

            printnow("called")
            data = data.substring(0, data.length - 1);

        }
        else {
            break
        }
    } 

    // data = data.replace(/\s+/g, '')
    eel.printnow(data)
    
    localStorage.setItem('tasks', JSON.stringify(data));

    data = ""
}


function getTable() {
    // get data from localstorage and split into array 
    var tasks = JSON.parse(localStorage.getItem('tasks'));

    // checks if tasks is empty
    if (tasks == "") {
        return
    }
    // splits again on #
    const tasks_arr = tasks.split("#");

    var task_number = tasks_arr.length;


 
    // loops for how many tasks there are
    for (i=0; i<task_number; i++) {
    
        task = tasks_arr[i];
        task_arr = task.split(",");

        // get rows for monitor start function
        var rows = $('#monitors tr').length;
      
        
        // get table
        var table = document.getElementById("monitors");
       
        // insert row
        var row = table.insertRow(-1);
        var cell0 = row.insertCell(0);
        var cell1 = row.insertCell(1);
        var cell2 = row.insertCell(2);
        var cell3 = row.insertCell(3);
        var cell4 = row.insertCell(4);
        var cell5 = row.insertCell(5);




        // insert data into cell
        cell0.innerHTML = task_arr[0];
        cell1.innerHTML = task_arr[1];
        cell2.innerHTML = task_arr[2];
        cell3.innerHTML = task_arr[3];
        cell4.innerHTML = "idle";
        cell5.innerHTML = '<button class="action" onclick="startMonitor(' + rows + ');"><i class="fas fa-play"></i></button><button class="action" ><i class="fas fa-stop"></i></i></button><button class="action" ><i class="far fa-edit"></i></button><button class="action" onclick="deleteRow(this);"><i class="fas fa-trash"></i></button>';

    
        
    }

};

var monitor

eel.expose(startMonitor)
function startMonitor(row) {
    setSnackbar("Opening Monitor")
    // eel.monitor_start();
    var data = ""
    
        for (i=0; i < 4; i++) {
            data = document.getElementById("monitors").rows[row].cells[i].innerHTML + ',' + data;
        }

    document.getElementById("monitors").rows[row].cells[4].innerHTML = "initializing"

    // launch monitor
    var launch = "width=550,height=850, menubar=yes, toolbar=yes, channelmode=yes, status=yes, titlebar=yes";

    // create name for monitor
    const title = data.split(",");
    name = title[3];
    server = title[2];
    channel = title[1];

    var title_str = name+' ('+server+','+' #'+channel+')'
    setSnackbar(title_str)
    
    window.open("/monitor.html", title_str, launch);
    
    updateTitle(title_str);
    // call python bacend
    eel.monitor_start(data, title_str);
    
    setStatusMonitor("active", row);

}

eel.expose(setStatusMonitor)
function setStatusMonitor(status, row){

    document.getElementById("monitors").rows[row].cells[4].innerHTML = status

}
eel.expose(setOverview) 
function setOverview() {

    var idle = document.getElementById('idle').innerHTML 
    var active = document.getElementById('active').innerHTML 

    eel.printnow(idle)
    eel.printnow(active)

    idle = idle - 1;
    active++;

    document.getElementById('idle').innerHTML = idle; 
    document.getElementById('active').innerHTML = active; 
    
}



eel.expose(changeName)
function changeName(name) {
    // changeName2(name);
    jQuery.getScript("monitor.js",function(){
        changeName2(name);
        });
    
}
eel.expose(createItem)
function createItem(monitorData, name) {
    jQuery.getScript("monitor.js",function(){
        createItem2(monitorData, name);
        });
    
}
function openInNewTab(url) {
    window.open(url, '_blank').focus();
   }
   
function updateTitle() {
    jQuery.getScript("monitor.js",function(){
        updateTitle(title);
        });

}



