#!/usr/bin/node

const request = require('request');

// prints the title of a Star Wars movie
// where the episode number matches a given integer
const movieId = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/';
const url = endpoint + movieId;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // parse the json to an object
    const movieObj = JSON.parse(body);
    console.log(movieObj.title);
  }
});
