var fact = function(n){
  if(n == 1){
    return 1;
  }
  else{
    return n * fact(n - 1);
  }
}

// fact(5)

var fib = function(n){
  if((n == 0) || (n == 1)){
    return n;
  }
  else{
    return fib(n - 1) + fib(n - 2);
  }
}

// fib(4);
