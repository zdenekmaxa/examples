function Foo() {
};

f1 = new Foo();

try {
    f1.bar(1); // raises not a function
}
catch(err) {
    console.log(err);
}

Foo.prototype.bar = function(a) {
    console.log(a);
}

// now it exists, it's been added through prototype
f1.bar(2);

// just undefined on non-existing property
console.log(f1.nonsense); 
// throws error on a non-existing method

