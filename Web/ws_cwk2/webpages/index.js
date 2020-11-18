window.addEventListener('load', initialize);

function initialize() {
  loadStories();

  // set up event handlers
  // submit button
  document.getElementById('submit').addEventListener('click', submitNewStory);

  // handle remembering of user name
  document.getElementById('username').addEventListener('change', saveUserName);
  document.getElementById('username').value = localStorage.username || '';

  // hash change happens when we click a link to go to the next page
  window.addEventListener('hashchange', loadStories);
}

async function loadStories() {
  const url = '/api/stories?p=' + encodeURIComponent(getCurrentPageNumber());

  const response = await fetch(url);
  if (response.ok) {
    putStoriesInPage(await response.json());
  } else {
    console.error('error getting stories', response.status, response.statusText);
    document.querySelector('body > main').innerHTML = 'sorry, something went wrong...';
  }
}

// retrieve the current page number from the hash fragment of the URL
function getCurrentPageNumber() {
  if (window.location.hash === '' || window.location.hash == null) return 1;

  let page = +window.location.hash.substring(1);
  if (Number.isNaN(page)) page = 1;

  return page;
}

function putStoriesInPage(pageOfStories) {
  const templateEl = document.getElementById('story-template');

  // clear out stories after the template
  while (templateEl.nextElementSibling && templateEl.nextElementSibling.classList.contains('story')) {
    templateEl.nextElementSibling.remove();
  }

  // set page indicator and next/prev links
  const page = pageOfStories.page;
  window.location.hash = '#' + page;

  const prevPageEl = document.getElementById('prevpage');
  const nextPageEl = document.getElementById('nextpage');
  const currPageEl = document.getElementById('currpage');
  const pageCountEl = document.getElementById('pagecount');

  prevPageEl.classList.remove('disabled');
  prevPageEl.href = '#' + (page-1);
  nextPageEl.classList.remove('disabled');
  nextPageEl.href = '#' + (page+1);
  currPageEl.textContent = page;
  pageCountEl.textContent = pageOfStories.pageCount;

  if (page >= pageOfStories.pageCount) {
    nextPageEl.classList.add('disabled');
    delete nextPageEl.href;
  } else if (page <= 1) {
    prevPageEl.classList.add('disabled');
    delete prevPageEl.href;
  }

  // add the actual stories
  const addNextBefore = templateEl.nextElementSibling;

  pageOfStories.stories.forEach((story) => {
    const storyEl = document.importNode(templateEl.content, true);
    storyEl.querySelector('.author').textContent = story.author || 'Anonymous';
    storyEl.querySelector('.title').textContent = story.title || '';
    storyEl.querySelector('.text').textContent = story.text || '';
    storyEl.querySelector('.delete').addEventListener('click', deleteStory);
    storyEl.querySelector('.delete').dataset.id = story.id;
    templateEl.parentElement.insertBefore(storyEl, addNextBefore);
  });
}

async function deleteStory(ev) {
  if (ev.target.dataset.id) {
    ev.target.parentElement.classList.add('deleting');
    const url = '/api/stories?id=' + encodeURIComponent(ev.target.dataset.id);
    await delay(500); // simulate slow network
    await fetch(url, { method: 'DELETE' });
    loadStories();
  }
}

async function submitNewStory() {
  const authorEl = document.getElementById('username');
  const titleEl = document.getElementById('title');
  const textEl = document.getElementById('text');

  if (!authorEl.checkValidity() ||
      !titleEl.checkValidity() ||
      !textEl.checkValidity()) {
    document.body.classList.add('error');
    return;
  }

  const submitButton = document.getElementById('submit');
  submitButton.textContent = 'submitting';
  submitButton.disabled = true;

  document.body.classList.remove('error');

  let url = '/api/stories';

  url += '?author=' + encodeURIComponent(authorEl.value);
  url += '&title=' + encodeURIComponent(titleEl.value);
  url += '&text=' + encodeURIComponent(textEl.value);

  await delay(500); // simulate slow network
  const response = await fetch(url, { method: 'POST' });

  submitButton.disabled = false;
  submitButton.textContent = 'submit';

  if (response.ok) {
    storySubmitted();
  } else {
    console.error('error posting a story', response.status, response.statusText);
    document.getElementById('submit').textContent = 'error, try again?';
  }
}

function storySubmitted() {
  document.getElementById('title').value = '';
  document.getElementById('text').value = '';
  document.getElementById('title').focus();

  // reload the stories or go to the first page, which will reload the stories
  if (window.location.hash === '#1') {
    loadStories();
  } else {
    window.location.hash = '#1';
  }
}

function saveUserName() {
  localStorage.username = document.getElementById('username').value;
}

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
