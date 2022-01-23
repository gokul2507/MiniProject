document.querySelector("#excel").addEventListener("change", (e) => {
     document.querySelector(".filename").innerHTML= e.target.files[0].name;
})