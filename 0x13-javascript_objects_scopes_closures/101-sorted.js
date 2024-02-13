#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const k = dict[key];
  const v = key;

  if (!(newDict[k] instanceof Array)) {
    newDict[k] = [];
  }
  newDict[k].push(v);
}

// print the new dictionary
console.log(newDict);
