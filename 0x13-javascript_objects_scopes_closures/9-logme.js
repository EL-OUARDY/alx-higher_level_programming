#!/usr/bin/node

function logMe (item) {
  // initialize the static variable inside a closure
  let counter = 0;

  // define the function that will access and modify the static variable
  function innerLogMe(item) {
    console.log(`${counter}: ${item}`);
    counter++;
  };

  // return the inner function so it can be called and accessed externally
  return innerLogMe;
}

module.exports.logMe = logMe() // create an instance of logMe
