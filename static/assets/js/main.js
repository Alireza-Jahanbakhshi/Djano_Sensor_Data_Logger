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
  console.log("im in")
  $.ajax({
    url: "http://127.0.0.1:8000/api/board/update_board/?led_1=c",
    type: "GET",
    contentType: 'application/json',
    success: function(result){
      console.log(result);
    },
    error:function(error){
      console.log(error);
    }
  })
  console.log("im in2")


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
