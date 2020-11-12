$(function() {
  $(document).on('click', 'input[type="button"]', function(event) {
   let id = this.id;
   console.log("Se presionó el Boton con Id :"+ id)
   });
 });