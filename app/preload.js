// All of the Node.js APIs are available in the preload process.
// It has the same sandbox as a Chrome extension.

const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('darkMode', {
  toggle: () => ipcRenderer.invoke('dark-mode:toggle'),
  system: () => ipcRenderer.invoke('dark-mode:system')
})

window.addEventListener('DOMContentLoaded', () => {

  const audio_ext = ["mp3", "wav"]
  const fs = require('fs')
  const path = require('path');

  var config = fs.readFileSync('../host_config', 'utf8')
  config = config.split('\n')

  let host_path = config[0].replace(/\\/g, "\\\\").replace(/(\r\n|\n|\r)/gm, "")
  let host_ip = config[1].replace(/(\r\n|\n|\r)/gm, "")
  let host_port = config[2].replace(/(\r\n|\n|\r)/gm, "")

   function createDirElement(dir_name) {
      const parentElem = document.createElement("p")
      const elem = document.createElement("ul")
      elem.className = "directory"

      elem.appendChild(document.createTextNode(dir_name))

      parentElem.appendChild(elem)
      document.getElementById("files").appendChild(parentElem)
   }

   function createFileInDir(file_name, parent_name) {
    var uls = document.getElementsByTagName("ul");

    for(var i=0;i<uls.length;i++){

        if(uls[i].innerHTML == parent_name){
        var parent = uls[i].parentNode;
        break;
        }
    }
    const parentElem = document.createElement("p")
    const ul = document.createElement("li")
    const elem = document.createElement("a")

    elem.className = "files"
    elem.appendChild(document.createTextNode(`${parent_name}/${file_name}`))

    ul.appendChild(elem)
    parentElem.appendChild(ul)
    parent.appendChild(parentElem)
   }

   function createFileElement(file_name) {
      const parentElem = document.createElement("p")
      const elem = document.createElement("a")
      elem.className = "files"
      const path = `http://${host_ip}:${host_port}/${file_name}`

      elem.appendChild(document.createTextNode(file_name))

      parentElem.appendChild(elem)
      document.getElementById("files").appendChild(parentElem)
   }

   entries = fs.readdirSync(host_path)
   entries.forEach(file => {
      f = `${host_path}\\${file}`
      if (fs.lstatSync(f).isDirectory() ) {
        createDirElement(file)
        dirEntries = fs.readdirSync(f)
        dirEntries.forEach(dfile => {
           createFileInDir(dfile, file)
        })
      } else {
        createFileElement(file)
      }
   })

})
