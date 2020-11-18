'use strict';

/* the comments below disable some lint errors */
/* eslint-disable no-inner-declarations */
/* global id,QUnit,test,ok,equal,notEqual,deepEqual */

const fs = require('fs');
const fetch = require('node-fetch');

const root = './artifact/';

const pathServer = root + 'server/';
const pathServerPackage = pathServer + 'package.json';

const pathUtil = root + 'utility/';
const pathUtilPackage = pathUtil + 'package.json';

QUnit.module('Coursework2');


/**
 * Given an assert object and a path, this will cause Qunit
 * to fail if the path is not present.
 */
function testPathExists(assert, path) {
  try {
    fs.accessSync(path, fs.F_OK);
    assert.ok(true, path + ' created');
  } catch (e) {
    assert.ok(false, path + ' is missing - please create it');
  }
}

/**
 * You will be developing both a utility module and a web server,
 * all of your work should exist under a folder called artifact.
 * Create these folders!
 */
QUnit.test(
  'Create folders.',
  (assert) => {
    testPathExists(assert, root);
    testPathExists(assert, pathUtil);
    testPathExists(assert, pathServer);
  },
);


/**
 * In the utility folder, create a package.json file, so that
 * it can be managed by NPM.  The package should be named
 * uupxxxxxx.  That's a 'u' followed by your student ID, all in
 * lower case.  Remember that if you're at the command line and
 * cd to this folder npm test won't work until you cd up a
 * level (because the more local npm test (which is undefined
 * by default) will be chosen).
 */
QUnit.test(
  'Add a package.json to the utility folder.',
  (assert) => {
    const pkg = require(pathUtilPackage); // eslint-disable-line global-require
    assert.equal(
      pkg.name.toLowerCase(),
      'u' + id().toLowerCase(),
      'Utility package name should be uupxxxxxx where xxxxxx is your id number (i.e. u' + id().toLowerCase() + ').',
    );
  },
);


/**
 * In the server folder, create a package.json file, so that
 * it can be started by NPM.  The server should be named
 * supxxxxxx.  That's an 's' followed by your student ID, all in
 * lower case. Your ID should be in `artifact/index.js`.
 */
QUnit.test(
  'Add a package.json to the server folder.',
  (assert) => {
    const pkg = require(pathServerPackage); // eslint-disable-line global-require
    assert.equal(
      pkg.name.toLowerCase(),
      's' + id().toLowerCase(),
      'Server package name should be supxxxxxx where xxxxxx is your id number (i.e. s' + id().toLowerCase() + ').',
    );
    assert.ok(
      pkg.main,
      'You must specify `main` in your server package.json - it should specify which code to run when running the server (e.g. `server.js`).',
    );
  },
);


/**
 * Create a web server with express, with an API as described
 * in the README.
 *
 * The server should respond to requests on `/api/stories`.
 *
 * The web server has to listen on port 8080. Running `npm test`
 * will start the server so it should not be running already.
 *
 * Running the tests starts your web server, but if you want to
 * try it in your browser, you need to start the web server
 * explicitly, with the command `node artifact/server`
 */
const initial = {
  id: 1,
  author: 'Luke Skywalker',
  title: 'Hello world!',
  text: 'So I decided to join jsbook like everyone else. What does one post here?',
};

const stories = [initial];

function pagedStories(p) {
  return {
    page: p,
    pageCount: Math.ceil(stories.length/10),
    stories: stories.slice(p*10-10, p*10),
  };
}

const api = '/api/stories';
const apiN = api + '/newest';
const apiO = api + '/oldest';

test(
  `Initial response to ${api}`,
  async () => {
    try {
      console.log('starting server');
      console.log('if you see EADDRINUSE errors, something is blocking port 8080.');
      console.log('if you see ECONNREFUSED errors, your server is not started on port 8080.');
      require(pathServer); // eslint-disable-line global-require
      deepEqual(
        await getJSONResponse('GET', api),
        pagedStories(1),
        'initially, there should be just one story by Luke Skywalker, copied from the README',
      );
    } catch (e) {
      ok(false, e.message);
    }
  },
);

test(
  `Initial response to ${apiN} and ${apiO}`,
  async () => {
    try {
      deepEqual(
        await getJSONResponse('GET', apiN),
        initial,
        'initially, the newest story should be by Luke Skywalker, copied from the README',
      );
      deepEqual(
        await getJSONResponse('GET', apiO),
        initial,
        'initially, the oldest story should be by Luke Skywalker, copied from the README',
      );
    } catch (e) {
      ok(false, e.message);
    }
  },
);

test(
  'Adding stories',
  async () => {
    try {
      const added = await addNewStory('a', 't1', 't2 t3');
      notEqual(added.id, 1, 'a newly submitted story cannot have the id 1');
      deepEqual(
        await getJSONResponse('GET', apiO),
        initial,
        'after submitting a story, the oldest story should still be by Luke Skywalker',
      );
      deepEqual(
        await getJSONResponse('GET', apiN),
        stories[0],
        'after submitting a story, the newest story must match the submitted data',
      );
      deepEqual(
        await getJSONResponse('GET', api),
        pagedStories(1),
        `after submitting a story, ${api} should list the first page from newest to oldest`,
      );


      // now add 19 more stories
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      await addNewStory();
      equal(stories.length, 21, 'we should have 21 stories now');

      // and check that all are there
      deepEqual(
        await getJSONResponse('GET', api),
        pagedStories(1),
        `after submitting many stories, ${api} should list the first 10 from newest to oldest`,
      );
    } catch (e) {
      ok(false, e.message);
    }
  },
);

test(
  `Paging at ${api}?p`,
  async () => {
    try {
      deepEqual(
        await getJSONResponse('GET', api+'?p=1'),
        pagedStories(1),
        'first page should return newest ten stories',
      );
      deepEqual(
        await getJSONResponse('GET', api+'?p=2'),
        pagedStories(2),
        'second page should return second ten stories',
      );
      deepEqual(
        await getJSONResponse('GET', api+'?p=3'),
        pagedStories(3),
        'third page should return only one story',
      );
      deepEqual(
        await getJSONResponse('GET', api+'?p=4'),
        pagedStories(3),
        'fourth page should return page 3',
      );
      deepEqual(
        await getJSONResponse('GET', api+'?p=42'),
        pagedStories(3),
        'forty-second page should return page 3',
      );
      deepEqual(
        await getJSONResponse('GET', api),
        pagedStories(1),
        'without paging we should get the first page',
      );
    } catch (e) {
      ok(false, e.message);
    }
  },
);

test(
  'Deletion of stories',
  async () => {
    try {
      let deleted = stories.splice(3, 1)[0];
      equal(
        await getResponseStatus('DELETE', api+'?id='+deleted.id),
        200,
        'successful deletion should return 200',
      );
      deepEqual(
        await getJSONResponse('GET', api+'?p=1'),
        pagedStories(1),
        'first page should return newest ten stories',
      );
      deepEqual(
        await getJSONResponse('GET', api+'?p=3'),
        pagedStories(2),
        'third page no longer exists, should return second page',
      );
      deepEqual(
        await getJSONResponse('GET', api),
        pagedStories(1),
        'without paging we should get the first page',
      );
      deepEqual(
        await getJSONResponse('GET', apiN),
        stories[0],
        `after deletion ${apiN} should still show the newest one`,
      );
      deepEqual(
        await getJSONResponse('GET', apiO),
        initial,
        `after deletion ${apiO} should still show the oldest one`,
      );

      // and delete another one
      deleted = stories.splice(stories.length-1, 1)[0];
      equal(
        await getResponseStatus('DELETE', api+'?id='+deleted.id),
        200,
        'successful deletion should return 200',
      );
      deepEqual(
        await getJSONResponse('GET', api+'?p=2'),
        pagedStories(2),
        'second page should return only nine stories',
      );
      deepEqual(
        await getJSONResponse('GET', apiN),
        stories[0],
        `after deletion ${apiN} should still show the newest one`,
      );
      const oldest = await getJSONResponse('GET', apiO);
      notEqual(oldest.id, 1, 'after deleting story with id 1 the oldest story cannot have id 1');
      deepEqual(
        oldest,
        stories[stories.length-1],
        `after deletion ${apiO} should still show the oldest one`,
      );
    } catch (e) {
      ok(false, e.message);
    }
  },
);

test(
  'Deletion of non-existent stories',
  async () => {
    try {
      equal(
        await getResponseStatus('DELETE', api+'?id=1'),
        404,
        'attempt to delete id 1 should return status code 404',
      );
      equal(
        await getResponseStatus('DELETE', api+'?id=nonexistent'),
        404,
        'attempt to delete id `nonexistent` should return status code 404',
      );
    } catch (e) {
      ok(false, e.message);
    }
  },
);

test(
  'Adding stories after deletion',
  async () => {
    try {
      // this will check that IDs don't overlap
      await addNewStory('a', 'b', 'c');

      // delete all stories but one
      // we do this by deleting the first and the last story until only one remains (the middle one)
      while (stories.length > 2) {
        let deleted = stories.shift();
        equal(
          await getResponseStatus('DELETE', api+'?id='+deleted.id), // eslint-disable-line no-await-in-loop
          200,
          'successful deletion should return 200',
        );

        if (stories.length > 2) {
          deleted = stories.pop();
          equal(
            await getResponseStatus('DELETE', api+'?id='+deleted.id), // eslint-disable-line no-await-in-loop
            200,
            'successful deletion should return 200',
          );
        }
      }

      // this will check more that IDs don't overlap
      await addNewStory('d', 'e', 'f');
    } catch (e) {
      ok(false, e.message);
    }
  },
);

test(
  'Delete should be implemented through a utility module',
  () => {
    const util = require(pathUtil); // eslint-disable-line global-require
    ok(
      typeof util.removeFromArray === 'function',
      'Create a function called removeFromArray.',
    );
    equal(
      util.removeFromArray.length,
      2,
      'The removeFromArray function must accept two parameters',
    );

    let original = [Object.assign({}, initial), Object.assign({}, initial), Object.assign({}, initial)];
    original[1].author = 'Obi von Kenobi';
    original[2].author = 'Han Solo';
    original[0].id = 7;
    original[1].id = 35;
    original[2].id = 12;

    let copied;
    equal(original.length, 3, 'Before calling removeFromArray `original` has 3 elements.');
    equal(copied, undefined, 'Before calling removeFromArray `copied` is expected to be undefined.');
    equal(original[0].author, 'Luke Skywalker', 'Before calling removeFromArray `Luke Skywalker` is in position 0.');
    equal(original[1].author, 'Obi von Kenobi', 'Before calling removeFromArray `Obi von Kenobi` is in position 1.');
    equal(original[2].author, 'Han Solo', 'Before calling removeFromArray `Han Solo` is in position 2.');
    copied = util.removeFromArray(original, 1);
    equal(original.length, 3, 'After calling removeFromArray `original` should still have 3 elements.');
    equal(copied.length, 2, 'After calling removeFromArray `copied` should have two elements.');
    equal(copied[1].author, 'Han Solo', 'After calling removeFromArray `Han Solo` is in position 1.');
    original = [42, 'star', { wars: true, trek: false }];
    deepEqual(util.removeFromArray(original, 2), [42, 'star'], 'removeFromArray from a mixed-value array');
    deepEqual(util.removeFromArray(original, 1), [42, { wars: true, trek: false }], 'removeFromArray from a mixed-value array');
    deepEqual(util.removeFromArray([0], 0), [], 'removeFromArray from an array with one element');
  },
);


// wrap fetch in order to set hostname, port, and timeout
function fetchPath(method, path) {
  return fetch(`http://localhost:8080${path}`, { method, timeout: 1000 });
}


// retrieve a JSON response from the given API path
// this will fail if the response status is not 200 OK or if the body is not JSON
// it will also fail in case of timeout or network issues
async function getJSONResponse(method, path) {
  try {
    const response = await fetchPath(method, path);
    equal(response.status, 200, `successful ${method} ${path} should return status code 200`);
    try {
      return await response.json();
    } catch (e) {
      ok(false, `response to ${path} must be JSON`);
    }
  } catch (e) {
    ok(false, `error in ${path}: ${e}`);
  }
  throw new Error('aborting some tests due to the errors above');
}

// retrieve the response status from the given API path
// it will fail in case of timeout or network issues
async function getResponseStatus(method, path) {
  try {
    const response = await fetchPath(method, path);
    return response.status;
  } catch (e) {
    ok(false, `error in ${path}: ${e}`);
  }
  throw new Error('aborting some tests due to the errors above');
}


// helper functions for adding stories
// newExpected creates a story to add, from the provided author,title,text
// addNewStory adds a story, puts it in `stories`, and does basic checks
let i = 1;
function newExpected(author='a', title='t', text='text') {
  i += 1;
  return {
    author: author + i,
    title: title + i,
    text: text + i,
  };
}

const knownIDs = [initial.id];

async function addNewStory(author, title, text) {
  const exp = newExpected(author, title, text);
  const added = await getJSONResponse('POST', `${api}?author=${exp.author}&title=${exp.title}&text=${exp.text}`);
  if (added.id == null) ok(null, 'a newly submitted story must have an ID');
  if (knownIDs.includes(added.id)) ok(false, 'the server must not reuse story IDs after deletion');
  if (added.id != null) {
    exp.id = added.id;
    knownIDs.push(added.id);
  }
  stories.unshift(added);
  deepEqual(
    added,
    exp,
    `a newly submitted story (${i}) must match the submitted data, with a new ID`,
  );
  return exp;
}
