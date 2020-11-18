const express = require('express');
const app = express();
const utility = require('../utility/utility');

let storiesArr = [{"id": 1, "author": "Luke Skywalker", "title": "Hello world!",
     "text": "So I decided to join jsbook like everyone else. What does one post here?"}];
let nextIndex = 1;

app.use('/', express.static('webpages', { extensions: ['html'] }));

app.get('/api/stories', function(req, res) {
  let pages = [];
  let currentPage = parseInt(req.query.p);
  let totalPages = Math.ceil(storiesArr.length/10);
  if (currentPage < 1 || !currentPage) currentPage = 1;
  if (currentPage > totalPages) currentPage = totalPages;

  for (let i = currentPage * 10 - 10; i < currentPage * 10 && i < storiesArr.length; i++) {
    pages.push(storiesArr[i]);
  }
  //let pages = storiesArr.slice(currentPage * 10 - 10, storiesArr.length%10);
  //let storyObjects = {"stories": pages, "page": currentPage,"pageCount": totalPages};
  res.json({"stories": pages, "page": currentPage,"pageCount": totalPages});
});

app.get('/api/stories/newest', function(req, res) {
  res.json(storiesArr[0]);
});

app.get('/api/stories/oldest', function(req, res) {
  res.json(storiesArr[storiesArr.length-1]);
});

app.post('/api/stories/', async function(req, res) {
  nextIndex++;
  storiesArr.unshift({"id": nextIndex,
          "author": req.query.author,
          "title": req.query.title,
          "text": req.query.text});
  res.json(storiesArr[0]);
});

app.delete('/api/stories/', async function(req,res) {
  let locationIndex = storiesArr.findIndex(story => story.id == req.query.id);
  if (locationIndex >= 0) {
    storiesArr = utility.removeFromArray(storiesArr, locationIndex);
    res.json(storiesArr);
  } else res.sendStatus(404);
});

app.listen(8080);
