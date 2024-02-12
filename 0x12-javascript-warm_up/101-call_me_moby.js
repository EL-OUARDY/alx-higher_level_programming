#!/usr/bin/node

// define callMeMoby function that calls a function x times
function callMeMoby (x, func) {
  for (let i = 0; i < x; i++) {
    func(); // call argument function
  }
}

// make the function available to the outside
module.exports.callMeMoby = callMeMoby;
