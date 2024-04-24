#!/usr/bin/node
// writes a data to a file //

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (err) {
    if (err) {
      console.log(err);
    }
  });
