const input = document.querySelector("#mysearch");
const tagdiv = document.querySelector(".tags");
const listdiv = document.querySelectorAll(".list");
const tagarr = []
function displaytags() {
     tagdiv.innerHTML = '';
     tagarr.forEach(t => {
          if (t.length > 0) {
               var div = document.createElement('div');
               var close = document.createElement('span');
               close.className = "spanclose"
               close.innerHTML = "X";
               var pa = document.createElement("p");
               pa.innerHTML = t;
               div.className = "tag";
               div.appendChild(pa);
               div.appendChild(close);
               tagdiv.appendChild(div);
          }
     });

}
function display(s) {
     if (s !== "none") {
          s = s.split("-");
          // console.log(s);
          listdiv.forEach(t => {
               t.classList.add("none");
          })
          s.forEach(t => {
               if (t.length > 0) {
                    var temp_d = document.getElementById(t);
                    temp_d.classList.remove("none");
               }
          });
     }
     else {
          listdiv.forEach(t => {
               t.classList.remove("none");
          })
     }
}
document.addEventListener("click", (e) => {
     if (e.target.className == "spanclose") {
          var tindex = tagarr.indexOf(e.target.parentNode.getElementsByTagName('p')[0].innerHTML);
          if (tindex > -1)
               tagarr.splice(tindex, 1);
          e.preventDefault();

          $.ajax({
               type: 'POST',
               url: '',
               data: {
                    tags: tagarr,
               },
               success: function (result) {
                    // console.log(result);
                    display(result)
               },
               error: function (response) {
                    // console.log("some error Occurred");
               }
          })
          tagdiv.removeChild(e.target.parentNode);
     }
})
input.addEventListener("keyup", (e) => {
     if (e.key == "Enter" && e.target.value.length > 0) {
          e.target.value.split(",").forEach(t => {
               if (t.length > 0)
                    tagarr.push(t);
          });
          // console.log(tagarr, tagarr.length)
          e.target.value = '';
          e.preventDefault();
          $.ajax({
               type: 'POST',
               url: '',
               data: {
                    tags: tagarr,
               },
               success: function (result) {
                    display(result);
               },
               error: function (response) {
                    // console.log("some error Occurred");
               }
          })
          displaytags();
     }
})

const icon = document.querySelector('.icon');
const clear = document.querySelector('.clear');
const search = document.querySelector('.search');
icon.onclick = function () {
     search.classList.toggle('active');
}
clear.onclick = function () {
     search.classList.toggle('active');
}