
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  ouput: process.stdout,
  terminal: false
})

rl.on('hello world', function (hello) {
  console.log(hello)
});

function hello(str){
  return str.split('').reverse().join('')
}
