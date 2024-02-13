#!/usr/bin/node

const fs = require('fs');

// get input arguments
const args = process.argv;

if (args.length >= 5) { // check arguments existance
  const file1 = args[2];
  const file2 = args[3];
  const target = args[4];

  // read the contents of the two files
  const content1 = fs.readFileSync(file1, 'utf8');
  const content2 = fs.readFileSync(file2, 'utf8');

  // write the contents to the destination file
  fs.writeFileSync(target, content1 + content2);

} else {
  console.log('Usage: node concat.js <source1> <source2> <target>');
}
