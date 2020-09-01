// codice per verificare se jquery è attivo
//  if (typeof jQuery == "undefined") {
// 	alert ("Jquery non è installato");
	
//     } else {
//         alert ("Jquery è installato!")
//     }  
 

// codice javascript ricerca
$(document).ready(function(){
  $("#myInput").keyup( function() {
	  
    var value = $(this).val().toLowerCase();
     
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
//codice javascript checkbox
// $(document).ready(function() {
//     $(".checkid").click(function() {
//         var checked = $(this).is(':checked');
//             if (checked == true){
//                 codice = $(this).attr("name")
//                 alert(codice)
//             };
       
//         });
// });