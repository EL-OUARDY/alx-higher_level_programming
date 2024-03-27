#!/usr/bin/node

const request = require('request');

// rints the number of movies
// where the character “Wedge Antilles” is present
const endpoint = process.argv[2];
characterId = 18;
let count = 0;
request.get(endpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // parse the json to an object
    data = JSON.parse(body);

    data.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });

    console.log(count);
  }
});
