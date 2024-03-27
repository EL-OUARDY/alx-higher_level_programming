#!/usr/bin/node

const fs = require('fs');

// Writing to a file
const file = process.argv[2];
const text = process.argv[3];
fs.writeFile(file, text, 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
