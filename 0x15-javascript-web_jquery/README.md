# JavaScript - Web jQuery — Alx Higher Level Programming
0x15. JavaScript - Web jQuery

```Front-end```
```JavaScript```

## What is jQuery?
``jQuery`` is a fast, small, and feature-rich JavaScript library. It simplifies things like HTML document traversal and manipulation, event handling, animation, and Ajax interactions for rapid web development.

## Selectors
jQuery allows you to select HTML elements using **CSS-style** selectors. You can target elements by their tag name, class, ID, attributes, or relationships.

Examples:
```js
// Select all paragraphs
$("p");

// Select elements with class "example"
$(".example");

// Select element with ID "header"
$("#header");
```

## Get and Set Content
You can easily get and set content within HTML elements using jQuery methods like text() and html().

Example:
```js
// Get text content of an element
var text = $("#myElement").text();

// Set HTML content of an element
$("#myElement").html("<p>New content</p>");
```

## Modify an HTML Element Style
jQuery allows you to modify CSS styles of HTML elements using the css() method.

Example:
```js
// Modify background color
$("#myElement").css("background-color", "red");

// Modify font size
$("#myElement").css("font-size", "20px");
```

## Modify the DOM
You can easily manipulate the ``DOM`` (Document Object Model) using jQuery methods like append(), prepend(), after(), and before().

Example:
```js
// Append a new paragraph
$("#container").append("<p>New paragraph</p>");

// Prepend a new paragraph
$("#container").prepend("<p>New paragraph</p>");
```

## Listen/Bind to DOM Events
jQuery provides methods like on() and click() to listen for DOM events such as clicks, keypresses, and mouse movements.

Example:
```js
// Listen for click event
$("#myButton").click(function() {
  alert("Button clicked!");
});

// Listen for keypress event
$("#myInput").on("keypress", function() {
  console.log("Key pressed!");
});
```

## jQuery Ajax
jQuery simplifies asynchronous HTTP requests (Ajax) with methods like \$.ajax(), \$.get(), and \$.post().

Example:
```js
// Ajax GET request
$.get("example.php", function(data) {
  console.log("Data received:", data);
});

// Ajax POST request
$.post("submit.php", { name: "EL-OUARDY", age: 26 }, function(data) {
  console.log("Response:", data);
});
```

## jQuery ready
In jQuery, the **ready()** method is used to execute code when the DOM (Document Object Model) is fully loaded. It ensures that your code runs only after the DOM is ready to be manipulated, which is essential for preventing issues with accessing elements that haven't yet been created.

```js
$(document).ready(function() {
  // Your code here
  console.log("DOM is ready!");

  // You can manipulate DOM elements here
});
```

Alternatively, you can use a shorthand version of ready() by passing a function directly to the jQuery object:

```js
$(function() {
  // Your code here
  console.log("DOM is ready!");

  // You can manipulate DOM elements here
});
```

## Contact Me
**Email:** ouadia@elouardy.com \
**Twitter:** https://twitter.com/_ELOUARDY
