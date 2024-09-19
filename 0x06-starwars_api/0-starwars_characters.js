#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

// Star Wars API URL for the given movie
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the Star Wars API
request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch the movie details. Status Code:', response.statusCode);
    return;
  }

  // Get the characters list from the response body
  const characters = body.characters;

  // For each character, make a request to fetch the name
  characters.forEach((characterUrl) => {
    request(characterUrl, { json: true }, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
        return;
      }

      if (charResponse.statusCode === 200) {
        console.log(charBody.name); // Print the character name
      }
    });
  });
});