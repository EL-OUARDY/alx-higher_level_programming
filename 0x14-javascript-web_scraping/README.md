# JavaScript - Web scraping — Alx Higher Level Programming
0x14. JavaScript - Web scraping

```Scripting```
```API```
```JavaScript```

## JSON
``JSON`` (JavaScript Object Notation) is a lightweight data interchange format. It's easy for humans to read and write and easy for machines to parse and generate. 
Here is an example of a JSON:
```json
{
  "name": "El_Ouardy",
  "age": 26,
  "location": "Morocco",
  "languages": ["Python", "JavaScript", "HTML", "CSS"],
  "experience": {
    "role": "Full-Stack Web Developer",
    "years": 3
  }
}
```

## Manipulate a JSON data
Here's how you can manipulate JSON data in JavaScript:
```js
// Parse JSON string to JavaScript object
const jsonData = '{"name": "El_OUARDY", "age": 26}';
const jsonObject = JSON.parse(jsonData);

// Accessing values
console.log(jsonObject.name); // Output: El_OUARDY

// Convert JavaScript object to JSON string
const person = { name: 'EL_OUARDY', age: 26 };
const jsonString = JSON.stringify(person);
console.log(jsonString); // Output: {"name":"EL_OUARDY","age":26}
```

## Using Request and Fetch API
``Request`` and ``Fetch`` APIs are used to make HTTP requests in JavaScript. Fetch is more modern and versatile, while Request is simpler and easier to use in some scenarios. 

Example using Request
```js
const requestURL = "https://example.io/endpoint.json";
const request = new Request(requestURL);

const response = await fetch(request);
const data = await response.json();
```

Here's a basic example of how to use Fetch API:
```js
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Reading and Writing Files with fs Module
In Node.js, the ``fs`` module provides functions for working with the file system. Here's how you can read and write files using fs:
```js
const fs = require('fs');

// Reading a file
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Writing to a file
const content = 'This is the content to write to the file.';
fs.writeFile('example.txt', content, err => {
  if (err) throw err;
  console.log('File written successfully!');
});
```
Remember to handle errors appropriately, especially when working with file operations and network requests.


## Let's connect
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
