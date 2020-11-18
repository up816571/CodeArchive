/*
 * This is index.js
 * Start by modifying the id function to return
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

// draws a stick figure on the canvas
// the stick figure will stand over the point X,Y (default: 100,150)
// facing is a degree in which the stick figure is facing: 0 is to the right, 90 is towards us
function drawStickFigure(el, x, y, facing) {
  var c = el.getContext("2d");

  // set our drawing style
  c.lineWidth = 2;
  c.lineCap = "round";
  c.lineJoin = "round"
  c.strokeStyle = "#000";

  if (x == null) x = 100;
  if (y == null) y = 150;

  // the arms and the legs look the same
  drawLimbs(c, x, y)            // legs
  drawLimbs(c, x, y-40)         // arms

  // body is just a line
  line(c, x, y-40, x, y-80)     // body

  // head is a circle with eyes and a smile
  circle(c, x, y-100, 20)       // head
  drawFace(c, x, y-100, facing) // face


  // helpful functions start here
  function drawLimbs(c, x, y) {
    line(c, x-20, y, x, y-40)
    line(c, x+20, y, x, y-40)
  }

  function drawFace(c, x, y, facing) {
    // if the `facing` parameter is not given, the stick figure will face towards us
    if (facing == null) facing = 90;

    // make sure the `facing` parameter is between 0 and 360
    facing = facing % 360; // that's like the mathematical remainder after a division
    if (facing < 0) facing += 360;

    if (facing > 180) return;  // facing away from us, don't draw a face

    // we'll fake the turning of the face by shifting the eyes and the smile by an offset of up to 10 pixels
    var faceOffset = 0;
    if (facing <= 180) {
      faceOffset = (facing-90)/9;
    }

    circle(c, x-7-faceOffset, y-5, 1)  // 7 is distance from center, 5 is how high the eyes are from the head's center, 1 is eye size
    circle(c, x+7-faceOffset, y-5, 1)

    // decrease the smile size here
    var smileSize = 70; // size of smile in degrees of angle; 360 would be a full circle
    var startAngle = rad(90-smileSize/2-2*faceOffset)
    var endAngle   = rad(90+smileSize/2-2*faceOffset)
    arc(c, x-faceOffset, y, 12, startAngle, endAngle) // 12 is the radius of the smile circle
  }

  // draw a line on canvas context `c`, from point x1,y1 to point x2,y2
  function line(c, x1, y1, x2, y2) {
    c.beginPath();
    c.moveTo(x1,y1);
    c.lineTo(x2,y2);
    c.stroke();
  }

  // draw a circle on canvas context `c`, centered on x,y, with radius r
  // also fill the circle with white (so it's not transparent)
  function circle(c, x, y, r) {
    c.beginPath()
    c.fillStyle="#fff"
    c.arc(x, y, r, 0, 6.3, false); // 6.3 is bigger than 2π so the arc will be a whole circle
    c.fill()
    c.stroke()
  }


  // draw an arc on canvas context `c`, cenetered on x,y, with radius r, from angleStart to angleEnd
  function arc(c, x, y, r, angleStart, angleEnd) {
    c.beginPath();
    c.arc(x, y, r, angleStart, angleEnd, false)
    c.stroke();
  }

  // convert from degrees to radians
  function rad(x) {
    return x * Math.PI / 180;
  }
}

function drawLines(canva) {
  let canv = canva.getContext('2d');
  canv.beginPath();
  canv.moveTo(100,100);
  canv.lineTo(500,100);
  canv.stroke();
  canv.beginPath();
  canv.moveTo(100,200);
  canv.lineTo(300,200);
  canv.stroke();
}

function drawTriangle(canva, x1, y1, x2, y2, x3, y3) {
  let canv = canva.getContext('2d');
  canv.strokeStyle = "red";
  canv.fillStyle = "lime";
  canv.beginPath();
  canv.moveTo(x1, y1);
  canv.lineTo(x2, y2);
  canv.lineTo(x3, y3);
  canv.lineTo(x1, y1);
  canv.fill();
  canv.stroke();
}

function getRandColor() {
  console.log('here');
  let r = 255*Math.random()|0;
  let g = 255*Math.random()|0;
  let b = 255*Math.random()|0;
  return 'rgb(' + r + ',' + g + ',' + b + ')';
}

function drawGrid(canva) {
  let jump = 50;
  let canv = canva.getContext('2d');
  for(let i = 0; i < canva.width; i += jump) {
    canv.strokeStyle = getRandColor() ;
    canv.beginPath();
    canv.moveTo(i, 0);
    canv.lineTo(i, canva.height);
    canv.stroke();
  }
  for(let i = 0; i < canva.height; i += jump) {
    canv.strokeStyle = getRandColor() ;
    canv.beginPath();
    canv.moveTo(0, i);
    canv.lineTo(canva.width, i);
    canv.stroke();
  }
}

function drawCzechFlag(canva) {
  let canv = canva.getContext('2d');
  canv.fillStyle = "blue";
  canv.beginPath();
  canv.moveTo(0,0);
  canv.lineTo(200, 135);
  canv.lineTo(0, 270);
  canv.fill();
  canv.fillStyle = "red";
  canv.beginPath();
  canv.moveTo(0, 270);
  canv.lineTo(400, 270);
  canv.lineTo(400, 135);
  canv.lineTo(200, 135);
  canv.fill();
  canv.fillStyle = "white";
  canv.beginPath();
  canv.moveTo(0, 0);
  canv.lineTo(400, 0);
  canv.lineTo(400, 135);
  canv.lineTo(200, 135);
  canv.fill();
}

function drawSpartacus(canva) {
  drawStickFigure(canva, 100, 200, 90);
  let canv = canva.getContext('2d');
  canv.strokeRect(120, 150, 5, 10);
  canv.strokeRect(117.5, 150, 10, 2.5);
  canv.strokeRect(120, 130, 5, 20);
  canv.beginPath();
  canv.moveTo(120, 130);
  canv.lineTo(125, 130);
  canv.lineTo(122.5, 125);
  canv.lineTo(120, 130);
  canv.fill();
  canv.stroke();
}
