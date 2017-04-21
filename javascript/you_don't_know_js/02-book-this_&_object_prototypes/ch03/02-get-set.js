var myObject = {
	// define a getter for `a`
	get a() {
		return 2;
	}
};

console.log(myObject.a);

console.log("via definedProperty");

// get, set descriptors defined not per objecet basis but on
Object.defineProperty(
	myObject,	// target
	"b",		// property name
	{			// descriptor
		// define a getter for `b`
		get: function(){ return this.a * 2 },
		// make sure `b` shows up as an object property
		enumerable: true
        // Invalid property descriptor. Cannot both specify accessors and
        // a value or writable attribute
        // value: "aaa" 
	}
);


console.log(myObject.a);
console.log(myObject.b);

console.log("getter is hardcoded");
myObject.b = 100;
console.log(myObject.b); // still 4

