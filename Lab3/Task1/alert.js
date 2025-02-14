alert("I'm JavaScript!");

alert('Hello'); alert('World');

alert('Hello');
alert('World');

alert('Hello')
alert('World')

alert(3 +
    1
    + 2);

    alert("Hello");

    [1, 2].forEach(alert);

    alert("Hello")//error

    [1, 2].forEach(alert);

    alert("Hello")[1, 2].forEach(alert);//error

    // This comment occupies a line of its own
alert('Hello');

alert('World'); // This comment follows the statement

/* An example with two messages.
This is a multiline comment.
*/
alert('Hello');
alert('World');

/* Commenting out the code
alert('Hello');
*/
alert('World');

/*
  /* nested comment ?!? */
  */
 alert( 'World' );

 "use strict";

// this code works the modern way
...

alert("some code");
// "use strict" below is ignored--it must be at the top

"use strict";

// strict mode is not activated

'use strict'; <Shift+Enter for a newline>
//  ...your code
<Enter to run>

(function() {
  'use strict';

  // ...your code here...
})()

let message;

let message;

message = 'Hello'; // store the string 'Hello' in the variable named message

let message;
message = 'Hello!';

alert(message); // shows the variable content

let message = 'Hello!'; // define the variable and assign the value

alert(message); // Hello!

let user = 'John', age = 25, message = 'Hello';

let user = 'John';
let age = 25;
let message = 'Hello';

let user = 'John',
  age = 25,
  message = 'Hello';

  let user = 'John'
  , age = 25
  , message = 'Hello';

  var message = 'Hello';

  let message;

message = 'Hello!';

message = 'World!'; // value changed

alert(message);

let hello = 'Hello world!';

let message;

// copy 'Hello world' from hello into message
message = hello;

// now two variables hold the same data
alert(hello); // Hello world!
alert(message); // Hello world!

let message = "This";

// repeated 'let' leads to an error
let message = "That"; // SyntaxError: 'message' has already been declared
So, we should declare a variable once and then refer to it without let.

let userName;
let test123;

let $ = 1; // declared a variable with the name "$"
let _ = 2; // and now a variable with the name "_"

alert($ + _); // 3

let 1a; // cannot start with a digit

let my-name; // hyphens '-' aren't allowed in the name

let имя = '...';
let 我 = '...';

let let = 5; // can't name a variable "let", error!
let return = 5; // also can't name it "return", error!

// note: no "use strict" in this example

num = 5; // the variable "num" is created if it didn't exist

alert(num); // 5

"use strict";

num = 5; // error: num is not defined

const myBirthday = '18.04.1982';

const myBirthday = '18.04.1982';

myBirthday = '01.01.2001'; // error, can't reassign the constant!

const COLOR_RED = "#F00";
const COLOR_GREEN = "#0F0";
const COLOR_BLUE = "#00F";
const COLOR_ORANGE = "#FF7F00";

// ...when we need to pick a color
let color = COLOR_ORANGE;
alert(color); // #FF7F00

const pageLoadTime = /* time taken by a webpage to load */;

let admin, name; // can declare two variables at once

name = "John";

admin = name;

alert( admin ); // "John"

let ourPlanetName = "Earth";

let currentUserName = "John";

const birthday = '18.04.1982';

const age = someCode(birthday);

const BIRTHDAY = '18.04.1982'; // make birthday uppercase?

const AGE = someCode(BIRTHDAY); // make age uppercase?

