# Web-Script Programming
## Coursework Challenge 2 (ws_cwk2)

Welcome to the second coursework for the Web Script Programming unit.  This folder contains all the challenges that you will try to complete.

This is an individual coursework, so whilst you are allowed to discuss both the challenges _and_ the approaches you might take to tackling them, all work must be your own.

## Pre-requisite

Your VMs have Node.js version 8, so we expect that you will deliver code that is compatible with this version.
In particular, `await`/`async` does not work on older versions of Node.js.

## Preparation

1. Download the zip file from moodle and unpack it as follows:

  ```
  unzip ws_cwk2.zip
  cd ws_cwk2
  ```

2. To download the dependencies (QUnit and Archiver) type:

  ```bash
  npm install
  ```

3. Run the tests by typing:

  ```bash
  npm test
  ```


## Structure

Unit tests are in the same format that you have completed in the preceeding weeks and are specified in `test.js`.  To run the unit tests you should run `npm test` as you have been doing for the server worksheets.  There are unit tests for everything described below.

You **must** only change files in the `artifact` folder, as that is all you will be submitting.

## Preparation / Submission / Upload
When you have completed all the tests to the best of your ability, type:

```shell
npm run zip
```

This will create a zipped submission file titled `artifact_000000.zip` (and it will helpfully automatically use your ID instead of 000000).  This file should be uploaded to the dropbox on moodle.  Zip is the only acceptable file format - DO NOT use any other file compression format!

### Hints
* It is unlikely that you will need to create anything other than `.js` and `.json` files.
* We have built a solution that passes all the tests.  With comments removed the server is 57 lines of code and the utility module is 8 lines.  65 lines total - without trying to compress things - so don't go berserk with the amount you write!
* When all the tests pass, work on the quality, readability, and maintainability of your code.

## What you have to do

* We have created an API for a story-sharing service called JSBook.
* You must create a server which implements this API.
* You will need to create a server and a module in order to pass all the tests – we have provided the appropriate folder structure for you.  
* The server must keep stories in-memory.  Do not write stories to file or database.
* The `server` folder must contain a `package.json` file in which you should manage your dependencies (such as the `express` package).
* The `package.json` file **must not** contain your name as the author; please use your UP student number so we preserve anonymity.

The `webpages/index.html` page (which you do **not** have to edit) will be a client page for the API. Your server should serve this page if you include this code:

```javascript
app.use('/', express.static('webpages', { extensions: ['html'] }));
```

When not running `npm test`, you can start your server from the top-level `ws_cwk2` directory, using this command (assuming you have correctly set the value `main` in `artifact/server/package.json`):

```shell
node artifact/server
```

### The API

The API you must implement has the following end-points:

 * GET on `/api/stories` — return an object in JSON, initially like this:
   ```json
   {
     "stories": [
       {
         "id": 1,
         "author": "Luke Skywalker",
         "title": "Hello world!",
         "text": "So I decided to join jsbook like everyone else. What does one post here?"
       }
     ],
     "page": 1,
     "pageCount": 1
   }
   ```

  - The API should provide results in pages of 10 entries.  
  - A query parameter `p` specifies which page to return, starting with 1. If the `p` parameter is omitted, the default value is 1.
  - If the client asks for `/api/stories?p=1`, they should only get 10 stories, starting from the newest one.
  - If `p=2`, the API must return the second batch of 10 stories.
  - When a page of stories is returned it must be ordered with the most recent story first.
  - If `p` is greater than the last page number, the API must return the last available page.
  - The `page` value is the currently returned page. If the requested page `p` is greater than the last page number, the returned `page` value will indicate the last page number.
  - The `pageCount` value is the number of the last non-empty page.

  For example, if we have stories with IDs from 1 to 30:
  - `p=1` will give us the 10 stories with IDs 30,29,28,27,26,25,24,23,22,21, together with `page=1, pageCount=3`.
  - `p=2` will give us stories with IDs 20,19,18,17,16,15,14,13,12,11, together with `page=2, pageCount=3`.  
  - if we then delete stories 14 and 15, `p=2` will give us stories with IDs 20,19,18,17,16,13,12,11,10,9, together with `page=2, pageCount=3`.  
  - `p=3` would then return only the 8 stories with IDs 8,7,6,5,4,3,2,1, together with `page=3, pageCount=3`.
  - `p=42` would return the same, i.e. the last page of stories, together with `page=3, pageCount=3`.


 * GET on `/api/stories/oldest` — return the oldest story, e.g.
   ```json
   {
     "id": 1,
     "author": "Luke Skywalker",
     "title": "Hello world!",
     "text": "So I decided to join jsbook like everyone else. What does one post here?"
   }
   ```

 * GET on `/api/stories/newest` — return the newest story, otherwise like above

 * POST on `/api/stories` — there will be three query parameters: `author`, `title`, and `text`, containing a new story. When a new story is accepted at `/api/stories`, your server must give it a new ID that is not used by any previous story. The new story must be added to the list of stories (so that it is returned as the newest story on a GET request to `/api/stories`). The response on POST to `/api/stories` should return the new story as JSON, complete with the new ID, for example like this:
   ```json
   {
     "id": 2,
     "author": "Chewbacca",
     "title": "grrrwaaaaaarggggh!",
     "text": "brrwhhhaargh!"
   }
   ```

 * DELETE on `/api/stories` — there will be one query parameters: `id`. If the server has a story with the given ID, it should remove it and the response should be only the 200 status code. No other stories should be affected; in particular, their IDs won't change. If the server did not have a story with the given ID, the response should be the 404 status code.

### Extra task

To implement the deletion functionality, write a `utility` module with a function called `removeFromArray(arr, index)`:
The function will remove an element from an array: it **must not** change the original array, it **must** return a copy of the array without the `index`'th element (starting from 0), so the resulting array is one element shorter than the original array.

## A note on security (the lack of it)
We have not looked at authentication and authorization yet, so this service is completely open to everyone and therefore clearly impractical in the real world — however — it exercises the server-side material we have been looking at in the last 6 weeks.

# Finally
We hope you enjoy this test - we've tried to keep it challenging-enough to cause you some head-scratching, but small-enough to be easily finishable within the time available.

Good luck!
