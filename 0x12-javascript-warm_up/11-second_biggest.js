#!/usr/bin/node
const args = process.argv;

// check user input
if (args.length < 4) {
  console.log(0);
} else {
  // remove first items (node args) and convert each array item to integer
  const inputs = args.slice(2).map(Number);

  let biggest = inputs[0];
  let second = inputs[0];

  // loop through inputs array
  inputs.forEach((num) => {
    if (num > biggest) {
      second = biggest;
      biggest = num;
    } else if (num > second && num < biggest) {
      second = num;
    }
  });

  // print second biggest number
  console.log(second);
}
