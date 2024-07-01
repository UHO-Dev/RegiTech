let ciInput = document.getElementById("ci");

let ValidCI =  () => {
    if(!(ciInput.value.length <= 11 && !isNaN(ciInput.value[ciInput.value.length-1]))){
      ciInput.value = ciInput.value.substring(0,ciInput.value.length-1)
    }
  }
  
  ciInput.addEventListener("input", ValidCI)
