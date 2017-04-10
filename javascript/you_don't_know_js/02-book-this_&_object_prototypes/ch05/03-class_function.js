console.log(Object.prototype);
console.log("\nprototype on object");
var v = {a: 2, b: 3};
console.log(v.prototype); // undefined, it's only on function object
console.log(v.__proto__); // {} exists

console.log("\nprototype on function");
function Obj() {
};
console.log(Obj.prototype); // Obj {}
console.log(Obj.__proto__);
console.log(Obj.prototype === Obj.__proto__); // false - why?

console.log("\nprototype on function object via new");
var o = new Obj();
console.log(o.prototype); // undefined
console.log(o.__proto__);
console.log(Obj.prototype === o.__proto__);

console.log("\nprototype on object via create");
var o = Object.create(Obj);
console.log(o.prototype);
console.log(o.__proto__);
console.log(o.prototype === o.__proto__); // false
console.log(Obj.prototype === o.prototype); // true
console.log(Obj.prototype === o.__proto__); // false

console.log("\nchange of log output (string operations):\n");

console.log("Object: " + Object.prototype);
var v = {a: 2, b: 3};
console.log("var object prototype: " + v.prototype);
console.log("var object __proto__: " + v.__proto__);
console.log(v.prototype); // undefined, it's only on function object
console.log(v.__proto__); // {} exists

