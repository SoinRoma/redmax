let value = $("#quantity").val();
let totalweight = $("#weight").val();
let total;

$('#increment').on("click", function (event) {
   event.preventDefault();
   value = parseInt($("#quantity").val());
   value = parseInt(value + 1);
   $("#quantity").val(value);
   total = value * totalweight;
   $("#totalWeight").text(total);
});
$('#decrement').on("click", function (event) {
   event.preventDefault();
   if (value > 0) {
      value = parseInt($("#quantity").val());
      value = parseInt(value - 1);
      $("#quantity").val(value);
      total = value * totalweight;
      $("#totalWeight").text(total);
   } else {
      value = 0;
      $("#quantity").val(value);
      total = value * totalweight;
      $("#totalWeight").text(total);
   }
});
$("#packaging").change(function () {

   let cubL = $("#packaging option:selected").data("length");
   let cubW = $("#packaging option:selected").data("width");
   let cubH = $("#packaging option:selected").data("height");
   let weight = $("#packaging option:selected").data("weight");

   if (cubL) {
      $("#cubL").val(cubL);
      $("#cubL").addClass('disabled');
   } else {
      $("#cubL").val("");
      $("#cubL").removeClass('disabled');
   }

   if (cubW) {
      $("#cubW").val(cubW);
      $("#cubW").addClass('disabled');
   } else {
      $("#cubW").val("");
      $("#cubW").removeClass('disabled');
   }

   if (cubH) {
      $("#cubH").val(cubH);
      $("#cubH").addClass('disabled');
   } else {
      $("#cubH").val("");
      $("#cubH").removeClass('disabled');
   }

   if (weight) {
      $("#weight").val(weight);
      $("#weight").addClass('disabled');
   } else {
      $("#weight").val("");
      $("#weight").removeClass('disabled');
   }

});
$("#weight, #quantity").change(function () {
   value = $("#quantity").val();
   totalweight = $("#weight").val();
   total = value * totalweight;

   $("#totalWeight").text(total);
});


// Один из инпутов в модалке должен быть обязательным
document.addEventListener('DOMContentLoaded', function () {
   const inputs = Array.from(
      document.querySelectorAll('input[name=loading_email], input[name=loading_phone]')
   );

   const inputListener = e => {
      inputs
         .filter(i => i !== e.target)
         .forEach(i => (i.required = !e.target.value.length));
   };

   inputs.forEach(i => i.addEventListener('input', inputListener));
});
