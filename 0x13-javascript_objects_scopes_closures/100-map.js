#!/usr/bin/node

const list = require('./100-data').list;

/*
the new list must be created with each value equal to the value
of the initial list, multipled by the index in the list
*/
const newList = list.map((element, index) => element * index);

// print initial list
console.log(list);

// print new list
console.log(newList);
