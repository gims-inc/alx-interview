#!/usr/bin/node
// script that prints all characters of a Star Wars movie.

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (err, res, body) {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const characterUrls = data.characters;

    const ids = characterUrls.map(url => parseInt(url.split('/').slice(-2, -1)[0]));
    const sortedids = ids.sort((a, b) => a - b);

    sortedids.forEach(id => {
      request(`https://swapi-api.alx-tools.com/api/people/${id}/`, function (err, res, body) {
        if (!err && res.statusCode === 200) {
          const data = JSON.parse(body);
          const charactername = data.name;
          console.log(charactername);
        } else {
          console.log(err);
        }
      });
    });
  } else {
    console.log(`Error: ${err}`);
  }
});
