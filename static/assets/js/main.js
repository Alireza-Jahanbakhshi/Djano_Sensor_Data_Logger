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
  let color = e.target.value.substring(1);
  $.ajax({
    url: `http://sensordatalogger.ir/api/board/update_board/?led=${color}`,
    type: "GET",
    contentType: 'application/json',
    success: function(result){
      console.log(result);
    },
    error:function(error){
      console.log(error);
    }
  })
});

blueLamp.addEventListener("click", (e) => {
  e.target.classList.toggle("blue-lamp");
  $.ajax({
    url: "http://sensordatalogger.ir/api/board/update_board/?led_1=c",
    type: "GET",
    contentType: 'application/json',
    success: function(result){
      console.log(result);
    },
    error:function(error){
      console.log(error);
    }
  })
});

redLamp.addEventListener("click", (e) => {
  e.target.classList.toggle("red-lamp");
  $.ajax({
    url: "http://sensordatalogger.ir/api/board/update_board/?led_2=c",
    type: "GET",
    contentType: 'application/json',
    success: function(result){
      console.log(result);
    },
    error:function(error){
      console.log(error);
    }
  })
});

greenLamp.addEventListener("click", (e) => {
  e.target.classList.toggle("green-lamp");
  $.ajax({
    url: "http://sensordatalogger.ir/api/board/update_board/?led_3=c",
    type: "GET",
    contentType: 'application/json',
    success: function(result){
      console.log(result);
    },
    error:function(error){
      console.log(error);
    }
  })
});

speakerImg.addEventListener("click", (e) => {
  console.log(`volume: ${speakerImg.dataset.value / 10}`)
  audio.volume = speakerImg.dataset.value / 10;
  audio.play();
});

console.log(temperature.dataset.value)

function setTemperature(amounth) {
  temperature.style.height =
    ((amounth - config.minTemp) / (config.maxTemp - config.minTemp)) * 100 + "%";
  temperature.dataset.value = amounth + units[config.unit];
}

setTemperature(parseInt(temperature.dataset.value));