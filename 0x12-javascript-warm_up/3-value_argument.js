#!/usr/bin/node
// get arguments passed to the script
const argv = process.argv;

if (!argv[2])
  console.log('No argument');
else
  console.log(argv[2]);
