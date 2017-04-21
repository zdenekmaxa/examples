var a = new Array();
console.log(a);

var a = ["a", "b", "c"];
console.log(a);
a.push("d");
console.log(a);
console.log(a[1]);
console.log(a["1"]); // the same

// still array is an object
a.myprop = "something";
console.log(a);
console.log(a.length); // property is not included in length calculation

console.log("property that looks like a number works differently");
a["4"] = "ten";
console.log(a);
console.log(a.length);

console.log("empty positions in between");
a["10"] = "ten";
console.log(a);
console.log(a.length);

