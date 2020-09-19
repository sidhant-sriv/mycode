function rot13(message){
    var arr = message.split('');
    var abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnop'.split('');
    var ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOP'.split('');
    for (var i = 0; i < arr.length; i++){
      var letter = '';
      if (arr[i].match(/[a-z]/)){
        letter = abc.indexOf(arr[i]);
        arr[i] = abc[letter+13];
      }else if (arr[i].match(/[A-Z]/)){
        letter = ABC.indexOf(arr[i]);
        arr[i] = ABC[letter+13];
      }
    }
    return arr.join('');
  }