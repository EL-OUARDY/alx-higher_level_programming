#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const endpoint = `https://swapi.dev/api/films/${movieId}/`;
let charactersList = [];

// prints all characters of a Star Wars movie
request(endpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);
  charactersList = data.characters;
  printCharacterName();
});

function printCharacterName(index = 0) {
  if (index < charactersList.length) {
    request(charactersList[index], (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printCharacterName(++index);
    });
  }
};
