#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let m = 0; m < num; m++) {
    console.log('C is fun');
  }
}
