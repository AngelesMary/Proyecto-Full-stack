
document.querySelector('.campo span').addEventListener('click', e => {
    const passwordInput = document.querySelector('#password');
    if (e.target.classList.contains('show')) {
        e.target.classList.remove('show');
        e.target.textContent = 'Ocultar';
        passwordInput.type = 'text';
    } else {
        e.target.classList.add('show');
        e.target.textContent = 'Mostrar';
        passwordInput.type = 'password';
    }
});
 
 
 
 (function() {
  var formulario = document.getElementsByName('formulario')[0],
      elementos = formulario.elements,
      boton = document.getElementById ('btn');

   var validarNombre = function(e){
       if (formulario.nombre.value == 0) {
        alert("complete el campo");
        e.preventDefault();
       }
   };

   var validarRadio = function(e){
      if (formulario.sexo[0].checked == true || formulario.sexo[1].checked == true) {
         } else { alert("complete el campo");
         e.preventDefault();
        }
      };

      var validarText = function(e){
        if (formulario.text.value == 0) {
         alert("complete el campo");
         e.preventDefault();
        }
    };

   var validar = function(e){
       validarNombre(e);
       validarRadio(e);
       validarText(e);
   }

        

  formulario.addEventListener("submit", validar);
   } ())

   
   
    
    
    
       
       

   
 
