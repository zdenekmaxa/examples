var anotherObject = {
	a: 2
};

var myObject = Object.create( anotherObject );

console.log(anotherObject.a); // 2
console.log(myObject.a); // 2

anotherObject.hasOwnProperty( "a" ); // true
myObject.hasOwnProperty( "a" ); // false

myObject.a++; // oops, implicit shadowing!
// property is found in the prototype, it's not read-only
// it's added to the own object and shadows the one from prototype

console.log(anotherObject.a); // 2
console.log(myObject.a); // 3

myObject.hasOwnProperty( "a" ); // true

