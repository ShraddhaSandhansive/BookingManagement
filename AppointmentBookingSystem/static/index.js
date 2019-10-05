function registerUser(){
    let firstname = document.getElementById('firstname').value
    let lastname = document.getElementById('lastname').value
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value
    let contact = document.getElementById('contact').value
    let address = document.getElementById('address').value

    $.post(
        "/storeUser/", 
     {
        firstname : firstname,
        lastname : lastname,
        email : email,
        password : password,
        contact : contact,
        address : address

    },
    function(data){
        if(data['code'] == 200){
            alert("Registration Successful!")
            setTimeout(
                ()=> {window.location.href = "/login/"},
                100
            )
        }
        else{
            alert("Failed!");
            setTimeout(
                ()=> {window.location.reload},
                100
            )
            
        }
      });   
}

function login(){
    let password = document.getElementById('password').value
    let username = document.getElementById('username').value
    
    $.post(
        "/loginUser/", 
     {
        username : username,
        password : password

    },
    function(data){
        if(data.code == 200){
            alert(data.msg)
        }
        else{
            alert("Check Username or Password!");
            setTimeout(
                ()=> {window.location.reload},
                100
            )
            
        }
      });   

}

function bookService(){
    let date = moment($('#datetimepicker1').data('date')).format('DD/MM/YYYY HH:mm');
    let service_id = document.getElementById('service').value;
    $.post(
        "/loginUser/", 
     {
        username : username,
        password : password

    },
    function(data){
        if(data.code == 200){
            alert(data.msg)
        }
        else{
            alert("Check Username or Password!");
            setTimeout(
                ()=> {window.location.reload},
                100
            )
            
        }
      });  
}