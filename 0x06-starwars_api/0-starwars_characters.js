#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Movie not found');
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Fetch each character's name in order
  characterUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body);
        console.log(character.name);
      }
    });
  });
});
