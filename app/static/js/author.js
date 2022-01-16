var x = document.getElementsByClassName("addauthor");
var author_count = document.getElementById("no_author")
function getauthors(authors, remove = -1) {
     author_values = [];
     for (let i = 0; i < authors; i++) {
          if (i == remove)
               continue;
          let f_name = document.getElementById("authorf" + (i + 2));
          let m_name = document.getElementById("authorm" + (i + 2));
          let l_name = document.getElementById("authorl" + (i + 2));
          // console.log(i,f_name,m_name,l_name);
          author_values.push([f_name.value, m_name.value, l_name.value]);
     }
     return author_values;
}

function setauthors(authors, aut_list) {
     for (let i = 0; i < authors; i++) {
          let f_name = document.getElementById("authorf" + (i + 2));
          let m_name = document.getElementById("authorm" + (i + 2));
          let l_name = document.getElementById("authorl" + (i + 2));
          // console.log(i,f_name,m_name,l_name);
          f_name.value = aut_list[i][0];
          m_name.value = aut_list[i][1];
          l_name.value = aut_list[i][2];
     }
}
function newele(new_author) {
     return `<div class="subadd">
     <div class="namebox">
     <span class="details">First Name</span>
     <input type="text" name="authorf${new_author}" id="authorf${new_author}" required>
     </div>
     <div class="namebox">
     <span class="details">Middle Name</span>
     <input type="text" name="authorm${new_author}" id="authorm${new_author}">
     </div>
     <div class="namebox">
     <span class="details">Last Name</span>
     <input type="text" name="authorl${new_author}" id="authorl${new_author}" required>
     </div>
     <div class="delete" onclick=deleteauthor(${new_author})><i class="fa-regular fa-trash"></i></div></div>`
}
function addauthor() {
     let authors = x[0].childElementCount;
     let autor_list = getauthors(authors);
     let toadd = newele(authors + 2);
     x[0].innerHTML += toadd;
     author_count.value = parseInt(author_count.value) + 1;
     setauthors(authors, autor_list);
}

function deleteauthor(ele_no) {
     ele_no -= 2
     let authors = x[0].childElementCount;
     let author_list = getauthors(authors, ele_no);
     // console.log(author_list);
     x[0].removeChild(x[0].children[ele_no]);
     author_count.value = parseInt(author_count.value) - 1;
     no_ele = x[0].childElementCount;
     // console.log(ele_no, no_ele);
     while (ele_no < no_ele) {
          present_ele = x[0].children[ele_no];
          present_ele.innerHTML = present_ele.innerHTML.replaceAll((ele_no + 3) + "\"", ele_no + 2 + "\"").replaceAll("deleteauthor(" + (ele_no + 3), "deleteauthor(" + (ele_no + 2));
          ele_no++;
     }
     setauthors(authors - 1, author_list);
}
// console.log("dfg");