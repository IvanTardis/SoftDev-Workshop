/*
  your PPTASK:

  First, familiarize yourself with the given html file for this work.

      then...

  Test drive each bit of code in this file,
  and insert comments galore, indicating anything
  you discover,
  have questions about,
  or otherwise deem notable.

  Have the given html file open as you work.

  Write with your future self or teammates in mind.

  If you find yourself falling out of flow mode, consult
  - other teams
  - MDN

  A few comments have been pre-filled for you...

  (delete this block comment once you are done)
*/





// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)

// I can see this in teh dev console at the top, with the file and line it's from
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x)
{
    var j=30;
    return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

// The document is index.html, automatically? How did that work
console.log(document);

//create a new node in the tree

// This adds item to list
var addItem = function(text)
{
    // ordered list in html file has tag "thelist"
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

//prune a node from the tree

// removes item from list based on index
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//color selected elements red

// this only works for 1st and 8th elements that don't have a class
// also any ones I add since they have no class too
var red = function()
{
    var items = document.getElementsByTagName("li");
    console.log(items);
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red');
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    console.log(items);
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
    console.log(items);
};


//insert your implementations here for...
// FIB
var fib = function(n){
  if((n == 0) || (n == 1)){
    return n;
  }
  else{
    return fib(n - 1) + fib(n - 2);
  }
}

// FAC
var fact = function(n){
  if(n == 1){
    return 1;
  }
  else{
    return n * fact(n - 1);
  }
}

// GCD
var gcd = function(a,b){
  let holder = a;
  let x = false;
  while(!x){
    x = (a % holder == 0)&&(b % holder == 0);
    holder--;
  }
  holder++;
  return holder;
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    // body
    return retVal;
};

addItem("FACT(5): " + fact(5));
addItem("FIB(6): " + fib(6));
addItem("GCD(18294,2172): " + gcd(18294,2172));
