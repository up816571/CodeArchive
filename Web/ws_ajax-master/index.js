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
    return "UP816571";
    // e.g. return "UP654321";
}

function fn() {
    return "Josh";
}

function sn() {
    return "Ruffle";
}

async function showMessage(el, str) {
	const response = await fetch(str);
	const text = await response.text();
	el.textContent = text;
}

async function showList(el, str) {
  const response = await fetch(str);
	const data = await response.json();

  for (const i of data) {
    const li = document.createElement("li");
    li.textContent = i;
    el.appendChild(li);
  }
}

async function startShowingMessage(el, str) {
  setInterval(function() {showMessage(el,str)}, 1000);
}

async function handleError(el, str) {
  const response = await fetch(str);
  if(response.ok) {
    showMessage(el, str);
  } else {
    el.textContent = 'OH DEAR';
  }
}

function drawBox(canva, str) {
  let canv = canva.getContext("2d");
  window.setInterval(async () => {
    canv.clearRect(0, 0, canv.width, canv.height);
    const response = await fetch(str);
    const data = await response.json();
    canv.strokeRect(data.x, data.y, 20, 20);
  }, 1000);
}
