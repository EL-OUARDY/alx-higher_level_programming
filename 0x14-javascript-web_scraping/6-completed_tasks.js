#!/usr/bin/node

const request = require('request');

// computes the number of tasks completed by user id.
const endpoint = process.argv[2];
const result = {};

request.get(endpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // parse the json to an object
    const todos = JSON.parse(body);

    todos.forEach((todo) => {
      if (todo.completed) {
        if (result[todo.userId]) {
          result[todo.userId] += 1; // increment completed tasks
        } else {
          result[todo.userId] = 1; // first task
        }
      }
    });
    console.log(result);
  }
});
