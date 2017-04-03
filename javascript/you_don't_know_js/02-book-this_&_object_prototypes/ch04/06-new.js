// constructor function - returns an object
// called with new
function SomeObj() {
    o = { a: 1, b: 2 };
    return o;
}

function Vehicle() {
    this.wheels = 4;
    this.engines = 1;
};


some = new SomeObj();
console.log(some);

console.log("new:");
console.log(new Vehicle());
// engines, wheels are now undefined in the global context
// when called without new
// first, the function as is doen's return anything
console.log(Vehicle());
// and second, the engines and wheels become defined
// in the call-site, global context here, due to default binding
console.log(engines, wheels);

