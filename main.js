

const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const windowManager = require('electron-window-manager');

let mainWindow


function createWindow () {
  
  var mainWindow = new BrowserWindow({
    // width: 1000,
    // height: 575,
    backgroundColor: '#000000',
    show: false,
    icon:'web/icons/monitor10.png',
    maximizable: false,
    minWidth: 500,
    minHeight: 500,
    autoHideMenuBar: true,
    center: true,
    // webPreferences: {
    //   devTools: false
    // }

  });

  mainWindow.once('ready-to-show', () => {
    mainWindow.show()
  })


 
  mainWindow.loadURL('http://localhost:8000/auth.html');
  mainWindow.setMenuBarVisibility(false)
  
  mainWindow.on('closed', function () {
    mainWindow = null
  })
}


app.on('ready', createWindow)

app.on('window-all-closed', function () {
  app.quit()
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow()
  }
})

