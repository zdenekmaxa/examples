// each object created from calling new Foo() (see Chapter 2) will
// end up (somewhat arbitrarily) [[Prototype]]-linked to
// this "Foo dot prototype" object.
function Foo() {
	// ...
}

var a = new Foo();

console.log(Object.getPrototypeOf( a ) === Foo.prototype); // true
console.log(Foo.prototype === Foo.__proto__); // false
console.log(Foo.prototype === a.__proto__); // true

