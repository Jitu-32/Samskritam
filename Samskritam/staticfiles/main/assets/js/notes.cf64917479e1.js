function openNavNotes() {
  document.getElementById("addnotetext").style.width = "250px";
  document.getElementById("note").style.marginRight = "250px";
}

function closeNavNotes() {
  document.getElementById("addnotetext").style.width = "0";
  document.getElementById("note").style.marginRight = "0";
}


function updatenotes(){
  var s = document.getElementById("lessonnote").value;
  var txt = document.createElement("p");
  txt.innerHTML = s;
  // prompt(txt.innerHTML);
  document.getElementById("appendnote").append(txt);
alert("Done! Note added!");
}
