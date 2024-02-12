#!/usr/bin/node

// define callMeMoby fuction that increments and calls a function
function addMeMaybe (number, func) {
  func(number + 1); // call argument function
}

// make the function available to the outside
module.exports.addMeMaybe = addMeMaybe;
