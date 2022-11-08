 (function() {
  var formulario = document.getElementsByName('formulario')[0],
      elementos = formulario.elements,
      boton = document.getElementById ('btn');

   var validarNombre = function(e){
       if (formulario.nombre.value == 0) {
        alert("completa el campo nombre");
        e.preventDefault();
       }
   };

   var validarRadio = function(e){
      if (formulario.sexo[0].checked == true || formulario.sexo[1].checked == true) {
         } else { alert("completa el campo sexo");
         e.preventDefault();
        }
      };


   var validar = function(e){
       validarNombre(e);
       validarRadio(e);
   }

        

  formulario.addEventListener("submit", validar);
   } ())

   {
    alert("Pimero debes de iniciar sesión en Home/Login");
   }
