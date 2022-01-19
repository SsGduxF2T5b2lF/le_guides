---

title: Working with Custom Package
author: Lele
date: 2022-01-19
styles:
  style: vim

---

# Working w/ Local Package
Using local package for more manageable development

## Contents

- The why
- The usual
- The cheatsheet

---

# Why

Splitting our source code so it's,
- easier to read, and
- reusable in other source

## Case: a average value of list

### Before
```javascript
let avg = (list) => {
  let length = list.length;
  let sum = 0;
  list.forEach(item => {
    sum += item;
  });
  return sum / length;
}
```

### After
```javascript
let sum = (list) => {
  let sum = 0;
  list.forEach(item => {
    sum += item;
  });
  return sum;
}

let avg = (list) => {
  return sum(list) / list.length;
}
```

This way we can debug / develop BOTH `sum()` and `average()`

---

# Usual Stuffs: NPM Package
```
.
|_ dev/
  |_ apps/
  | |_ package.json
  | |_ .git/
  | |_ ...
  |
  |_ otherApps/
  | |_ package.json
  | |_ .git/
  | |_ ...
  |
  |_ calc/
    |_ avg.js
    |_ sum.js


_
```

- Updating `avg.js`
- Copy pasting `avg.js` to `apps/` and `otherApps/`
- Updating `avg.js`
- Copy pasting `avg.js` to `apps/` and `otherApps/`
- so on..

---

# What if...
```
.
|_ dev/
  |_ apps/
  | |_ package.json
  | |_ .git/
  | |_ ...
  |
  |_ otherApps/
  | |_ package.json
  | |_ .git/
  | |_ ...
  |
  |_ calc/
    |_ avg.js
    |_ sum.js
    |_ package.json
    |_ .git/
    |_ index.js
```

- Updating `avg.js`
- `npm install ../calc` on `apps/` and `otherApps/`
- Updating `avg.js`
- `npm install ../calc` on `apps/` and `otherApps/`
- so on..

---

## Benefit
1. we don't have extra `avg.js` on our apps
2. we can `git blame` on `calc/`

## Requirements
1. At least `calc/` must easy to access
  a. Registry like npm
  b. Repository like github
2. Versioning (optional)
3. Publishing (optional)

---

# Cheatsheet

[THE CHEATSHEET](https://atmos.washington.edu/~nbren12/reports/journal/2018-07-16-NN-conservation/node_modules/npm/html/doc/cli/npm-install.html)

## Install from Registry
```bash
$ npm install react
```

## Install from Repository
```bash
$ npm install <git_url>
```

## Install from Local Directory
```bash
$ npm install directory_with_package.json/
```

---

# Demo: Local Directory

---

# Boilerplate and Helper

What I use

## [TSDX](https://www.npmjs.com/package/tsdx)
- folder structure (index.js, src/, and tests/)
- yarn scripts (test, run, and build)
- styling (linter, I guess)

## [NP](https://www.npmjs.com/package/np)
- Publish to registry
- Semantic Versioning, with tags
- Multiple registry

---

# Future
What would you want for the next?

- Publishing
- Same stuffs but in python

---

# Fin
