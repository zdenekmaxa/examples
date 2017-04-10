function Foo() {
}

var f1 = Object.create(Foo.prototype);
// all false if not otherwise stated
console.log("3: " + (Foo.prototype === Object.getPrototypeOf(f1))); // true
console.log("5: " + (Foo.prototype === f1.__proto__)); // true
// f1.prototype - undefined

Foo.prototype.func = function() { console.log("func called"); }
f1.func();

console.log(f1.prototype); // undefined

