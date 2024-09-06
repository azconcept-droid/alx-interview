#!/usr/bin/node
/*
  script that prints all characters of a Star Wars movie
*/
const args = process.argv;
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = args[2] - 1;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;

    const characterUrl = results[movieId].characters;

    const length = results[movieId].characters.length;

    for (let i = 0; i < length; i++) {
      request(characterUrl[i], (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          const name = JSON.parse(body).name;

          console.log(name);
        }
      });
    }
  }
});
