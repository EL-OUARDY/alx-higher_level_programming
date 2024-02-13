# JavaScript | Objects, Scopes and Closures — Alx Higher Level Programming
0x13. JavaScript - Objects, Scopes and Closures

## Creating Objects in JavaScript
There are several ways to create objects in JavaScript:

**Object literal notation:**
```js
let obj = { key: value };
```
**Constructor function:**
```js
function Person(name) {
  this.name = name;
}

let person = new Person('John');
```
**Object.create() method:**
```js
let obj = Object.create(null);
obj.key = value;
```

## `this` Keyword
In JavaScript, ``this`` refers to the current execution context. It typically represents the object that owns the method being executed.

Example:
```js
let obj = {
  name: 'El_Ouardy',
  greet: function() {
    console.log('Hello, ' + this.name);
  }
};

obj.greet(); // Output: Hello, El_Ouardy
```

## Importance of Variable Type and Scope
Variable type and scope are important because they determine how variables can be accessed and manipulated within a program. Understanding them helps prevent unexpected behavior and bugs.

## Closure
A closure is a function that has access to its own scope, as well as the scope in which it was created (enclosing scope). It allows functions to retain access to variables from the enclosing scope even after the outer function has finished executing.

```js
function outerFunction() {
  let outerVar = 'I am outer';
  
  function innerFunction() {
    console.log(outerVar);
  }

  return innerFunction;
}

let closure = outerFunction();
closure(); // Output: I am outer
```

## Prototype
In JavaScript, each object has a prototype from which it inherits properties and methods. The prototype chain allows objects to inherit features from other objects.

## Object-Oriented JavaScript
JavaScript supports object-oriented programming (OOP) paradigms, allowing the creation of objects with properties and methods. OOP in JavaScript is prototype-based rather than class-based.

## Inheriting an Object from Another
In JavaScript, you can inherit properties and methods from one object to another using prototypes or constructor functions.

Example:
```js
function Animal(name) {
  this.name = name;
}

Animal.prototype.sound = function() {
  console.log(this.name + ' makes a sound');
};

function Dog(name, breed) {
  Animal.call(this, name);
  this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

let myDog = new Dog('Buddy', 'Labrador');
myDog.sound(); // Output: Buddy makes a sound
```

## Let's connect
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
