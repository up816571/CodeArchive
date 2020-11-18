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
    return "816571";
    // e.g. return "UP654321";
}

function fn() {
    return "Josh";
}

function sn() {
    return "R";
}

// add your functions here
function addTextTo(el, str) {
  el.textContent += str;
}

function replaceText(el, str) {
  el.textContent = str;
}

function moreBears() {
  let animals = document.getElementById('animals');
  animals.src = "http://placebear.com/400/200";
  animals.title = "A BEAR!";
  animals.alt = 'A bear.';
}

function setId(el, str) {
  el.id = str;
  return el;
}

function setClass(el, str) {
  el.className = str;
  return el;
}

function addAClass(el, str) {
  el.classList.add(str);
  return el;
}

function removeAClass(el, str) {
  el.classList.remove(str);
  return el;
}

function newElement(name) {
  return document.createElement(name);
}

function findElementById(ID) {
  return document.getElementById(ID);
}

function findElementByQuery(query) {
  return document.querySelectorAll(query);
}

function reverseList(listToRev) {
  let lists = document.querySelector(listToRev);
  let i = lists.childNodes.length;
  while (i--)
    lists.appendChild(lists.childNodes[i]);
  return lists;
}

function mover(el, destination) {
  let elem = document.querySelector(el);
  let newDestiantion = document.querySelector(destination);
  newDestiantion.appendChild(elem);
}

function filler(theList, stringArray) {
  for(let i = 0; i < stringArray.length; i++) {
    let li = document.createElement('li');
    li.textContent = stringArray[i];
    theList.appendChild(li);
  }
}

function dupe(selector) {
  let element = document.querySelector(selector);
  let dupe = element.cloneNode(true);
  element.parentElement.appendChild(dupe);
}

function removeAll(selector) {
  let elements = document.querySelectorAll(selector);
  for(let i = 0; i <elements.length; i++) {
    elements[i].remove();
  }
}

function getUserData() {
  let name = document.querySelector("#username").value;
  let speed = parseInt(document.querySelector("#speed").value);
  let student = document.querySelector("#student").checked;
  return {name, speed, student}
}
