const units = {
  Celcius: "°C",
  Fahrenheit: "°F",
};

const config = {
  minTemp: 0,
  maxTemp: 100,
  unit: "Celcius",
};

const temperature = document.querySelector(".temperature");
const dynamicLamp = document.querySelector(".dynamic-lamp");
const speakerImg = document.querySelector(".speaker__img");
const blueLamp = document.getElementById("blue");
const greenLamp = document.getElementById("green");
const redLamp = document.getElementById("red");
const dynamicLampInput = document.getElementById("color-picker");
const audio = document.getElementById("beep");

dynamicLampInput.addEventListener("input", (e) => {
  dynamicLamp.style.background = e.target.value;
  dynamicLamp.style.backgroundImage = `radial-gradient(${e.target.value}, transparent)`;
  dynamicLamp.style.border = `dotted 2px ${e.target.value}`;
  dynamicLamp.style.boxShadow = `0 0 20px #111 inset, 0 0 10px ${e.target.value}`;
});

blueLamp.addEventListener("click", (e) => {
  e.target.classList.toggle("blue-lamp");
  if (blueLamp)
  <script>
    $(document).ready(function(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/board/LED_1=1",
        type: "PUT",
        success: function(result){
          console.log(result);
        },
        error:function(error){
          console.log(error);
        }
      })
    })
  </script>
  else 
  <script>
  $(document).ready(function(){
    $.ajax({
      url: "http://127.0.0.1:8000/api/board/LED_1=0",
      type: "PUT",
      success: function(result){
        console.log(result);
      },
      error:function(error){
        console.log(error);
      }
    })
  })
</script>

});

redLamp.addEventListener("click", (e) => {
  e.target.classList.toggle("red-lamp");
});

greenLamp.addEventListener("click", (e) => {
  e.target.classList.toggle("green-lamp");
});

speakerImg.addEventListener("click", (e) => {
  audio.play();
});

function setTemperature(amounth) {
  temperature.style.height =
    ((amounth - config.minTemp) / (config.maxTemp - config.minTemp)) * 100 + "%";
  temperature.dataset.value = amounth + units[config.unit];
}

setTemperature(30);
