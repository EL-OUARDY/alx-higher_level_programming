#!/usr/bin/node

const request = require('request');

// prints all characters of a Star Wars movie
const movieId = process.argv[2];
const endpoint = 'https://swapi.dev/api/films/' + movieId;

request.get(endpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // parse the json to an object
    const data = JSON.parse(body);

    const characters = data.characters;

    characters.forEach((character) => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        }
        const characterObj = JSON.parse(body);
        console.log(characterObj.name);
      });
    });
  }
});
