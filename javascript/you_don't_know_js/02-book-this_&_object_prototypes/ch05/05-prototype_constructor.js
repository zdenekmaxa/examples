function Foo() {
    this.a = 1;
}

f1 = new Foo();
console.log(f1.a);
console.log(f1.b); // undefined
Foo.prototype.b = 2;
console.log(f1.b);
f2 = new Foo();
console.log(f2.b);

console.log("\nconstructor thing");
console.log(Foo.prototype.constructor === Foo); // true
console.log(f1.constructor === Foo); // true
// the constructor is available via prototype
console.log(f1.hasOwnProperty("constructor"));
console.log(f1.prototype); // undefined
console.log(f1.__proto__.hasOwnProperty("constructor"));

console.log("\nprototype sharing");
console.log(f1.__proto__.constructor === Foo);
console.log(f1.__proto__ === f2.__proto__);
console.log(Foo.prototype === f2.__proto__)

// Foo.prototype - access to the prototype
// f1.prototype - undefined but can access it via f1.__proto__

