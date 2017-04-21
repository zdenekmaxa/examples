
console.log("array iterations");
var myArray = [1, 2, 3];

for (var i = 0; i < myArray.length; i++) {
	console.log( myArray[i] );
}


console.log("array iterations directly over values");
var myArray = [ 1, 2, 3 ];

for (var v of myArray) {
	console.log( v );
}

console.log("array iteration via iterator");
var myArray = [ 1, 2, 3 ];
var it = myArray[Symbol.iterator]();

console.log(it.next()); // { value:1, done:false }
console.log(it.next()); // { value:2, done:false }
console.log(it.next()); // { value:3, done:false }
console.log(it.next()); // { value: undefined, done:true }

