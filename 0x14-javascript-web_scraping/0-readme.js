#!/usr/bin/node

const fs = require('fs');

// Reading from a file
const file = process.argv[2];
fs.readFile(file, 'utf8', (err, data) => {
  if (err)
    console.log(err);
  else
    console.log(data);
});
