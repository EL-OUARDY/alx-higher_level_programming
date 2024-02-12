# JavaScript — Alx Higher Level Programming
0x12. JavaScript - Warm up

## 1. Introduction
JavaScript is a powerful programming language that breathes life into web pages, making them interactive and dynamic. You'll encounter it building websites, mobile apps, and even creating games!

## 2. Variables and Constants:

Variables hold data you can change, while constants store fixed values.

``var:`` Old-school approach, use cautiously due to scoping issues.

``const:`` Declares unchangeable values. Use when data won't change.

``let:`` Modern choice, blocks changes within loops and functions.

```js
let name = "Ouadia";
const age = 26;
age = 27; // Error! 'age' is constant.
```

## 3. Data Types:

JavaScript offers various data types to store different information:
- **Numbers:** 10, 3.14
- **Strings:** "Hello", 'World!' (both quotes work)
- **Booleans:** true, false (represent truth/falsehood)
- **Objects:** Collections of key-value pairs (more on that later)
- **Arrays:** Ordered lists of values (e.g., [1, 2, 3])

## 4. Conditional Statements:

Control the flow of your code with if and else statements:
```js
if (age >= 18) {
  console.log("You are eligible to vote.");
} else {
  console.log("Wait a few years!");
}
```

## 6. Loops:

Repeat code blocks using while and for loops:
```js
// Print numbers from 1 to 5
for (let i = 1; i <= 5; i++) {
  console.log(i);
}

// Keep reading input until user enters "stop"
let userInput = "";
while (userInput !== "stop") {
  userInput = prompt("Enter something (or 'stop' to quit):");
  console.log(userInput);
}
```

## 7. ```break``` and ```continue``` Statements:

- **break:** Exits a loop immediately.
- **continue:** Skips to the next iteration of the loop.

## 8. Functions:

Reusable blocks of code that perform specific tasks:

```js
function greet(name) {
  console.log("Hello, " + name + "!");
}

greet("Ouadia"); // Output: Hello, Ouadia!
```

## 9. Return Statement:

Functions can optionally return a value using the return statement. If none is provided, they return **undefined**.

## 10. Scope:

Where variables are accessible. Use let and const carefully to avoid conflicts.

## 11. Arithmetic Operators:

Perform calculations: `+`, `-`, `*`, `/`, `%` (modulo), etc.

## 12. Dictionaries (Objects):

Store unordered collections of key-value pairs:

```js
let person = {
  name: "Ouadia",
  age: 26,
  country: "Morocco"
};

console.log(person.name); // Output: Ouadia
```
## 13. Importing Files:

Include code from other JavaScript files using import:

```js
import { greet } from "./greetings.js";

greet("World"); // Calls the greet function from greetings.js
```

## Let's connect
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
