// works as explained in the book
function Foo() { /* .. */ };

Foo.prototype = { /* .. */ }; // create a new prototype object

var a1 = new Foo();
console.log(a1.constructor === Foo); // false!
console.log(a1.constructor === Object); // true!

// a1 has no .constructor property, so it delegates up the [[Prototype]]
// chain to Foo.prototype. But that object doesn't have a .constructor
// either (like the default Foo.prototype object would have had!), so it
// keeps delegating, this time up to Object.prototype, the top of the
// delegation chain. That object indeed has a .constructor on it, which
// points to the built-in Object(..) function

console.log("modified");

// this doen't ...
// like if "after the constructor call" the prototype would be preserved?
function Faa() { /* .. */ };

var a2 = new Faa();
console.log(a2.constructor === Faa); // true

Faa.prototype = { /* .. */ }; // create a new prototype object

console.log(a2.constructor === Faa); // false! - was overwritten
// the look up stops at Object which has constructor which points to itself
console.log(a2.constructor === Object); // true!

