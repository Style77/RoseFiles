//document.getElementById('toggle-dark-mode').addEventListener('click', async () => {
//  await window.darkMode.toggle()
//})

window.addEventListener('DOMContentLoaded', () => {
    const files = Array.from(document.getElementsByClassName('files'))
    console.log(files)

    files.forEach(file => {
      file.addEventListener('click', function handleClick(event) {
        $('#file-viewer').load(`http://192.168.1.105:8010/${file.innerHTML}`)
      });
    });
})