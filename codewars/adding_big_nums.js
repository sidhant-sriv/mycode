function add(a, b) {
    if(Number.isSafeInteger(Number(a)) && Number.isSafeInteger(Number(a))){
      return (Number(a) + Number(b)).toString();
    }
    
    a = a.split("");
    b = b.split("");
    // console.log(a, b);
    var carries = 0;
    var result = [];
    
    // assumming they are both same length
    for(var i = a.length -1 ; i >= 0; i--){
      var sum = Number(a[i]) + Number(b[i]) + carries;
      result.unshift(sum % 10);
      if(sum >= 10){
        carries = 1;
      }else{
        carries = 0;
      }
    }
    
    if(sum >= 10){
      result.unshift(1);  // if the sum of first two Numbers is greater or equal to                     // ten then i have carries 1 to unshift
    }
    return result.join("");
  }