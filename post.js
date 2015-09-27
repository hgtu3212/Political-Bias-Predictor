var value = $('.textbox').val()
$.ajax({
      type: "POST",
      url: "http://localhost:8000/parse_data",
      data: JSON.stringify(value),
      success: function(msg){
        //success method
      },
      failure: function(msg){
       //failure message
      }
   });