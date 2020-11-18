/*
 * This is index.js
 * Start by modifying the id, fn and sn functions to return
 * information about you, then open index.html to check what
 * else you have to do, adding functions to the end of this
 * file as necessary.
 *
 * NB: all code you write this year should use strict mode, so
 * we've enabled that by default with the first line of code.
 */

'use strict';

function id() {
    return "816571";
    // e.g. return "UP654321";
}

function fn() {
    return "Josh";
}

function sn() {
    return "Ruffle";
}

/**
 * Utility functions for reference that may be used by tests
 * for various reasons.
 */

function exampleAttacher() {
  window.exampleid.addEventListener("click", exampleEventHandler);
}

function exampleEventHandler(event) {
    console.log("This is a", event.type, "event.");
}

// used by snitchAttacher
function snitchUpdater(event) {
  window.snitch.textContent = (event.type == 'mouseover' ? "IN" : "OUT");
}

// used by lovelyParaAttacher
function lovelyToggle() {
    window.thisisalovelyparagraph.classList.toggle("lovely");
}

/**
 * Add your functions here...
 */

function targetTextToConsole(event) {
  console.log(event.target.textContent);
}

function tttcAttacher() {
  window.button0.addEventListener("click", targetTextToConsole);
}

function lovelyParaAttacher() {
  window.thisisalovelyparagraph.addEventListener("click", lovelyToggle);
}

function lovelyButtonAttacher() {
  window.button1.addEventListener("click", lovelyToggle);
}

function conc() {
  let input1 = document.querySelector("#in1").value;
  let input2 = document.querySelector("#in2").value;
  document.querySelector("#out1").textContent =input1+input2;
}

function concatAttacher() {
  window.in1.addEventListener("change", conc);
  window.in2.addEventListener("change", conc);
}

function snitchAttacher() {
  window.mousewatcher.addEventListener('mouseover', snitchUpdater);
  window.mousewatcher.addEventListener('mouseout', snitchUpdater);
}

function reportUpdater(event) {
  let text = 'x: ' + event.screenX + ' y: ' + event.screenY;
  console.log(text);
  document.querySelector('#report').textContent = text;
}

function reportAttacher() {
  window.mousereporter.addEventListener('mousemove', reportUpdater);
}

function idValidationAttacher() {
  window.newid.addEventListener('input', function () {
    let input = document.querySelector('#newid');
    if (input.value.indexOf(' ') === -1) {
      input.classList.remove('invalid');
    } else {
      input.classList.add('invalid');
    }
  });
}
