#!/usr/bin/node
// get arguments count
const argsCount = process.argv.length;

// argv always contains two items!
if (argsCount === 2) {
  console.log('No argument');
} else if (argsCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
