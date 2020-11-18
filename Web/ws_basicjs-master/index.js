/*
 * This is index.js
 * Start by modifying the id, fn and sn functions to return
 * information about you, then open index.html to check what
 * else you have to do, adding functions to the end of this
 * file as necessary.
 *
 * NB: all code you write this year shoudl use strict mode, so
 * we've enabled that by default with the first line of code.
 */

'use strict';

function id() {
    return "UP816571";
    // e.g. return "UP654321";
}

function fn() {
    return "Josh";
}

function sn() {
    return "Ruffle";
}

function example() {
    // replace this example with
    // your first function then
    // add more below as necessary.
    return;
}
function add(a , b) {
  return a + b;
};

function subtract(a , b) {
  return a - b;
};

function  checkObject(x) {
  x.checked = true;
}

function checkObjectInside(x) {
  if (x.hasOwnProperty("checked") === true) {
    x.checked = true;
  }
}
