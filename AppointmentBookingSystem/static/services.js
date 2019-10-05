function saveService(){
    let name = document.getElementById('name').value
    let price = document.getElementById('price').value
    let imageFile = document.getElementById('imageFile')
    converttobase64(imageFile, function(result) {
        let baseImage = result
        $.post(
            "/storeService/", 
         {
            name : name,
            price : price,
            imageFile : baseImage,
            
        },
        function(data){
            if(data['code'] == 200){
                alert("Service Saved!")
                setTimeout(
                    ()=> {window.location.href = "/renderServices/"},
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
          });   }
        )
    }


    
function converttobase64(element, callback) {
    var result = "";
    var file = element.files[0];
    
    if (typeof(file) == 'undefined') return;
  
    var reader = new FileReader();
  
    reader.onloadend = function() {
  
      result = reader.result;
      callback(result);
    }
  
    reader.readAsDataURL(file);
  }