
(function(){
var box=document.getElementById("q"),res=document.getElementById("results");
if(!box||!res)return;
var IDX=null;
box.addEventListener("input",function(){
  var q=box.value.trim().toLowerCase();
  if(q.length<2){res.innerHTML="";return;}
  function go(){
    var hits=IDX.filter(function(e){return (e.t+" "+e.s+" "+e.x).toLowerCase().indexOf(q)>=0;}).slice(0,12);
    res.innerHTML=hits.map(function(h){return '<a href="'+ROOT+h.u+'">'+h.t+'<small>'+h.s+'</small></a>';}).join("");
  }
  if(IDX){go();}else{fetch(ROOT+"search.json").then(function(r){return r.json();}).then(function(j){IDX=j;go();});}
});
})();
