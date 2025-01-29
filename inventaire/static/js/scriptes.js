
'use strict';

document.body.style.backgroundColor='red'

function addLigne(){

    let d=document.querySelector("#detailReservation");
    let mydiv=d.lastElementChild;
    let g=mydiv.cloneNode(true);
    d.appendChild(g)
}

function deletLigne(){
    let d=document.querySelector("#detailReservation");
    if(d.children.length===1) {
        
 
        return 

    }else{

        d.lastElementChild.remove();
    }
}


function displayBlocs(){
    let ge=document.querySelector("#GE");
    let cabine=document.querySelector("#cabine");
    let modulaire=document.querySelector("#modulaire");
    let selected=document.querySelector('#cat')

    if(selected.value==='1'){
        ge.style.display='block';
        cabine.style.display='none';
        modulaire.style.display='none';
    }
    else if(selected.value==='2'){
        ge.style.display='none';
        cabine.style.display='block';
        modulaire.style.display='none';
    }
    else if(selected.value==='3'){
        ge.style.display='none';
        cabine.style.display='none';
        modulaire.style.display='block';
    }
    else{
        ge.style.display='none';
        cabine.style.display='none';
        modulaire.style.display='none';
    }
    
}
