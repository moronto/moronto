
'use strict';
//start navbar
 // Ajout d'un effet de réduction au scroll

//end navbar


function addLigne(idName){

    let d=document.querySelector(idName);
    let mydiv=d.lastElementChild;
    let g=mydiv.cloneNode(true);
    g.querySelectorAll('input').forEach(input => {
        input.value = '';})
    d.appendChild(g)
}

function deleteLigne(idName){
    let d=document.querySelector(idName);
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




function checkdate(){
    let dl=document.querySelector('#dateLivraison');
    let dr=document.querySelector('#dateRetour');
    if (dr.value < dl.value && dr.value != ""){
        alert("La date de retour que vous avez saisie n'est pas valid")
        console.log('vrai')

    }
}


//JQUERY

$(document).ready(function(){

    $(".messages").animate({
        top:100
    },1000).delay(4000)
   
    $(".messages").animate({
     left:'-10000px'

    },2000) 

    $('#search').on('input',function(){
        var valSearch=$(this).val()
        fetch(`/search/?valSearch=${encodeURIComponent(valSearch)}`).then(data=> console.log(data))
        $.ajax({
            url:'/search/',
            method: 'GET',
            caches:false,
            data: {'valSearch':valSearch},
            success: function(response) {
                const bodyTable=$('#table-body');
                bodyTable.empty();
                response.data.forEach(function(reservation) {

                    const row=`
            <div class="row">
                <div class="col-md-2">${reservation.dateReservation}</div>
                <div class="col-md-2">${reservation.refReservation}</div>
                <div class="col-md-2">${reservation.chargerAffaire}</div>
                <div class="col-md-2">${reservation.client}</div>
                <div class="col-md-2">${reservation.etat}</div>
                <div class="col-md-2 action">
                    
                        <a  href="${reservation.urlDetails}">
                            <i class="fa fa-file  fa-2x text-success "></i>
                        </a>
                        <a  href="${reservation.urlEdit}">
                            <i class='fa fa-edit  fa-2x  text-warning '></i>
                        </a>    
                        <a  href="${reservation.urlDelete}">
                            <i class='fa fa-trash fa-2x  text-danger '></i>
                        </a>
                </div>
            </div>   
                    
                    `
                    bodyTable.append(row)
                    
                });
                 
            }, 
        

        });
   
   
    });

    $('#refMateriel').on('change',function(){
        var valSearch=$(this).val()
        $.ajax({
            url:'/designation/',
            method: 'GET',
            caches:false,
            data: {'valSearch':valSearch},
            success: function(response) {
                const designation=$('#designation');
                const alertAddRef=document.querySelector('.alertAddRef');
                if(response.data.designation===""){
                    alertAddRef.style.display='block';
                }
                else{
                    designation.val(response.data.designation)
                } 
            }, 
        

        });
   
   
    });
   

});


// script for app livraison

//start newlivraison
function selectTrans() {
    const typetrans = document.querySelector('#typeTrans');
    const trans = document.querySelectorAll('.trans');
    const display = typetrans.selectedIndex === 0 ? 'block' : 'none';
    trans.forEach(element => element.style.display = display);
}

$('#no').on('click',function(){
  const div=document.querySelector("#alertAddRef")
  div.style.display='none'
  document.querySelector('#refMateriel').value=""
  document.querySelector('#observations').value=""
 
})


//End newlivraison
