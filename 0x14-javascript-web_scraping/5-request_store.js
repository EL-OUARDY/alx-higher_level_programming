#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// gets the contents of a webpage and stores it in a file
const url = process.argv[2];
const filename = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // save response body to file
    fs.writeFile(filename, body, 'utf-8', err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
