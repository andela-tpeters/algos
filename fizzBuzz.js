function fizzBuzz(number) {
  if(number % 15 == 0) {
    return 'FizzBuzz';
  } else if(number % 3 == 0) {
    return 'Fizz';
  } else if(number % 5 == 0) {
    return 'Buzz';
  }

  
}

console.log(fizzBuzz(15));
console.log(fizzBuzz(45));
console.log(fizzBuzz(90));