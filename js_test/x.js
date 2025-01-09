//access canvas and buttons via document
var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d"); //prepare to interact with canvas in 2D

ctx.fillStyle = "00ffff"; //set fill color to cyan

var requestID;

var clear = function(e){
  e.preventDefault();
  ctx.clearRect(0,0,500,500);
};
var radius = 0;
var growing = true;

var drawDot = function(){
  window.cancelAnimationFrame(requestID);
  ctx.clearRect(0,0,c.width,c.height);
  if(growing){
    radius+=1;
  }
  else{
    radius -= 1;
  }
  if(radius == (c.width / 2))
    growing = false;
  else if (radius == 0){
    growing = true;
  }
};
