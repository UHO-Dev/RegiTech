let RAMInput = document.getElementById("capacidad_ram");

let ValidRAM =  () => {
    if(!(RAMInput.value.length <= 5 && !isNaN(RAMInput.value[RAMInput.value.length-1]))){
      RAMInput.value = RAMInput.value.substring(0,RAMInput.value.length-1)
    }
  }
  
RAMInput.addEventListener("input", ValidRAM)
