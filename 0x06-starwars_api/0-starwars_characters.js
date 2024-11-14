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

    const urlPromises = characterUrl.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });
    Promise.all(urlPromises).then((names) => {
      names.forEach((name) => {
        console.log(name);
      });
    }).catch((err) => {
      console.log(err);
    });
  }
});
