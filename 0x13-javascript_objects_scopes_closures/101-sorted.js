#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (let key in dict) {
  let k = dict[key];
  let v = key;

  if (!(newDict[k] instanceof Array)) {
    newDict[k] = [];
  }
  newDict[k].push(v);
}

// print the new dictionary
console.log(newDict)
