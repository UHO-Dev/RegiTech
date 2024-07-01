let ValorInput = document.getElementById("valor");

let ValidValor =  () => {
    if(!(ValorInput.value.length <= 4 && !isNaN(ValorInput.value[ValorInput.value.length-1]))){
      ValorInput.value = ValorInput.value.substring(0,ValorInput.value.length-1)
    }
  }
  
  ValorInput.addEventListener("input", ValidValor)
