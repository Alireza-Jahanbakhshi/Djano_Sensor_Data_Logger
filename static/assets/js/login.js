const login = document.getElementById("submit-login");
const username = document.getElementById("username");
const password = document.getElementById("password");
const wrong = document.getElementById("wrong-info");


login.addEventListener("click",(e)=>{

  
    $.ajax({
      type: "POST",
      url: "http://sensordatalogger.ir/api/user/login/",
      dataType: 'json',
      data: {"username": username.value , "password" : password.value },
      success: function (){
        location.href = "http://sensordatalogger.ir/"
      },
      error:function(){
        wrong.style.display='flex';
        wrong.style.color = 'red';
      }
      
    });

})