let autocomplete;
let address1Field;
let address2Field;
let autocompleteFrom;
let autocompleteTo;
let fromZip;
let toZip;

function initAutocomplete() {
   address1Field = document.querySelector("#addressFrom");
   address2Field = document.querySelector("#addressTo");

   autocompleteFrom = new google.maps.places.Autocomplete(address1Field, {
      componentRestrictions: {country: ["us", "ca"]},
      fields: ["address_components", "geometry", "place_id"],
      types: ["(regions)"],
   });
   autocompleteTo = new google.maps.places.Autocomplete(address2Field, {
      componentRestrictions: {country: ["us", "ca"]},
      fields: ["address_components", "geometry", "place_id"],
      types: ["(regions)"],
   });

   google.maps.event.addListener(autocompleteFrom, 'place_changed', function () {

      let place = autocompleteFrom.getPlace();
      for (let i = 0; i < place.address_components.length; i++) {
         for (let j = 0; j < place.address_components[i].types.length; j++) {
            if (place.address_components[i].types[j] == "postal_code") {
               fromZip = place.address_components[i].long_name;
               console.log('form: ' + fromZip);
            }
         }
      }
   });
   google.maps.event.addListener(autocompleteTo, 'place_changed', function () {
      let place = autocompleteTo.getPlace();
      for (let i = 0; i < place.address_components.length; i++) {
         for (let j = 0; j < place.address_components[i].types.length; j++) {
            if (place.address_components[i].types[j] == "postal_code") {
               toZip = place.address_components[i].long_name;
               console.log('to: ' + toZip);
            }
         }
      }
   })
}