// the gist of
// https://www.w3schools.com/js/js_object_prototypes.asp

function Person(first, last) {
    this.firstName = first;
    this.lastName = last;
}

var p1 = new Person("F", "L");
console.log(p1.firstName, p1.lastName);

Person.prototype.greet = function(who) {
    return this.firstName + " " + this.lastName + " greets " + who;
}

console.log(p1.greet("me"));

