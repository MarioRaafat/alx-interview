#!/usr/bin/node
const request = require('request');
id = process.argv[2];

if (id === undefined) {
    console.log('Usage: ./0-starwars_characters.js <film_id>');
    process.exit(1);
};

const URL = `https://swapi-api.hbtn.io/api/films/${id}`;

request(URL, {json: true}, (err, res, body) => {
    if (err) {
        console.log(err);
    }


    if (res.statusCode !== 200) {
        console.log('Invalid movie id');
        process.exit(1);
    }

    charactersURLs = body.characters;
    charactersURLs.forEach((url) => {
        request(url, {json: true}, (err, res, body) => {
            if (err) {
                console.log(err);
            }
            console.log(body.name);
        });
    });
});