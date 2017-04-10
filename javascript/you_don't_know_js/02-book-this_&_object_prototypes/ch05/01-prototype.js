var anotherObject = {
    a: 2
};


// create an object linked to `anotherObject`
var myObject = Object.create(anotherObject);

console.log("prototype: " + (myObject.__proto__ === anotherObject));

for (var k in myObject) {
    console.log("found: " + k);
}
// found: a

console.log("a" in myObject); // true

console.log("added an attribute, enumerates both own and from prototype");
myObject.b = 3;
for (var k in myObject) {
    console.log("found: " + k);
}

console.log("prototype: " + (myObject.__proto__ === anotherObject));



console.log("\nchain of prototypes, properties vs methods:");

var var1 = { var1: function(arg) { console.log("called var1 for " + arg); } }
function Foo1() {}
Foo1.prototype.myFunc = function(arg) { 
    console.log("myFunc called for " + arg);
};
Foo1.prototype.prop = "my prop";
foo2 = Object.create(Foo1.prototype);
foo2.myFunc(1); // method called via prototype
var foo3 = Object.create(foo2);
foo3.myFunc(2);
var foo4 = Object.create(foo3);
foo4.myFunc(3);
console.log(foo4.prop); // property access via prototype
// toString is defined on Object's prototype, just like .create() is
// but calling foo4.create is not possible to call
console.log(foo4.toString());
console.log(foo4.__proto__); // Foo1 {}
console.log(foo4.__proto__.__proto__); // Foo1 {}
console.log(foo4.__proto__.__proto__.__proto__);
console.log(foo4.__proto__.__proto__.__proto__.__proto__); // it's Objects proto
console.log(foo4.__proto__.__proto__.__proto__.__proto__.__proto__); // null

console.log("\var ...");
var child = Object.create(var1);
child.var1("tak");

