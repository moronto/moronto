
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
