
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// let input = []
// rl.on("line", (line) => {
//     input.push(line.split(' ').map(el => parseInt(el)));
// }).on('close', () => {
//     console.log(input)
//     process.exit();
// });









const readline = require('readline');
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout,
});

let input=[]

rl.on('line', (line)=>{
    input.push(line.split(' ').map(el=>perseInt(el)));
}).on('close', ()=>{
    process.exit();
})




// let n = Number("1")

// let data = [];

// data.push(1);
// data.push(2);
// data.push(3);
// console.log(data.pop())
// console.log(data.shift())

// let str = "asdfqwer"
// let new_str = str.substring(0,3);
// new_str = str.substr(0,5);
// console.log(new_str);


// const arr = [2, 1, 3, 10];
// arr.sort(function(a, b)  {
//   return a - b;
// });


// Math.min(...caseLen)

// const numbers = [1]; 
// numbers.map((number, index, source) => {
//      // number: 요소값 // index: source에서 요소의 index // source: 순회하는 대상 
//     console.log(number); // 1 
//     console.log(index); // 0 
//     console.log(source); // [1] 
//     return number * number; 
// });
