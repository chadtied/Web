var input_block= document.getElementsByTagName('input');
var btn= document.getElementsByClassName('button')[0];
//var msg = require('./test.js');

btn.addEventListener("click", function(){
  var list= 0;
  var null_list= 0;
  var Sum= 100;
  var average= 0;
  for(var i= 3; i< input_block.length; i+= 2){
    if(input_block[i-1].value!= ""&& input_block[i].value!=""){
      Sum-= Number(input_block[i].value);
    }
    if(i!= input_block.length-1 && input_block[i-1].value!= ""){
        list++;
        if(input_block[i].value== "")
          null_list++;
    }
  }
  if(list> 0&& ){
    average= Math.round((Sum/null_list)*100)/100;
  }
  for(var i= 3; i< input_block.length; i+= 2){
    if(input_block[i].value== ""&& input_block[i-1].value!= ""){
      input_block[i].value= average.toString();
    }
    if(i== input_block.length-1&& list> 0)
        input_block[i].value= "100.0";
}
})
