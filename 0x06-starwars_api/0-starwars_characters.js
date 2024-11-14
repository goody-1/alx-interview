#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first command-line argument
const movieId = process.argv[2];

// Check if movie ID is provided
if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

// URL for the specified movie ID
const url = `https://swapi.dev/api/films/${movieId}/`;

// Helper function to fetch data with `request` and return a Promise
function fetchUrl (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to load data, status code: ${response.statusCode}`));
      } else {
        resolve(body);
      }
    });
  });
}

// Main function to fetch movie and character data in order
async function fetchCharacters () {
  try {
    // Fetch movie data
    const movieData = await fetchUrl(url);

    // Loop through characters in order, awaiting each to print in sequence
    for (const characterUrl of movieData.characters) {
      const characterData = await fetchUrl(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}

fetchCharacters();
