
'use strict';


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

    if(selected.value==='GROUPE ELECTROGENE'){
        ge.style.display='block';
        cabine.style.display='none';
        modulaire.style.display='none';
    }
    else if(selected.value==='CABINES AUTONOMES'){
        ge.style.display='none';
        cabine.style.display='block';
        modulaire.style.display='none';
    }
    else if(selected.value==='MODULAIRE'){
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

window.setTimeout(() => {

    document.querySelector('.messages').style.display="none"
    
}, 5000);


function checkdate(){
    let dl=document.querySelector('#dateLivraison');
    let dr=document.querySelector('#dateRetour');
    if (dr.value < dl.value && dr.value != ""){
        alert("La date de retour que vous avez saisie n'est pas valid")
        console.log('vrai')

    }
}
