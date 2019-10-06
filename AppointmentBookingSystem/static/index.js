function ValidateEmail(mail) 
{
 if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail))
  {
    return (true)
  }
    return (false)
}

function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if ( (charCode > 31 && charCode < 48) || charCode > 57) {
        return false;
    }
    return true;
}

function registerUser(){
    let firstname = document.getElementById('firstname').value.trim()
    let lastname = document.getElementById('lastname').value.trim()
    let email = document.getElementById('email').value.trim()
    email_validation = ValidateEmail(email)
    if (email_validation == false){
        alert('Check your email!');
        return false;
    }
    let password = document.getElementById('password').value.trim()
    let contact = document.getElementById('contact').value.trim()
    let address = document.getElementById('address').value.trim()
    isValid = 1;
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
            if(data.code == 200){
                alert("Registration Successful!")
                setTimeout(
                    ()=> {window.location.href = "/login/"},
                    100
                )
            }
            else if(data.code == 400){
                alert('User already exists!');
                return false;
            }
            else if(data.code == 402){
                alert('Please fill all data!');
                return false;
            }
            else{
                alert("Failed!");
                setTimeout(
                    ()=> {window.location.reload},
                    100
                )
            }
        });
    // }
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
            if(data.isAdmin == 1){
                window.location.href = "/renderServices/"
            }
            else{
                window.location.href = "/renderAllServices/"
            }
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
    let service_id = document.getElementById('serviceId').value;
    // alert("Request sent! You will receive confirmation email when salon will accept your reuqest!");
    $.post(
        "/bookServices/", 
     {
        bookingDate : date,
        serviceId : service_id
    },
    function(data){
        if(data.code == 200){
            alert("Request sent! You will receive confirmation email when salon will accept your reuqest!");
            window.location.href='/renderAllServices/'
        }
        else{
            alert("Failed to book !");
            setTimeout(
                ()=> {window.location.reload},
                100
            )
            
        }
      });  
}