function Foo(name) {
	this.name = name;
}

Foo.prototype.myName = function() {
	return this.name;
};

function Bar(name,label) {
	Foo.call(this, name);
	this.label = label;
}

// here, we make a new `Bar.prototype`
// linked to `Foo.prototype`
// creates a "new" object out of thin air, and links that new object's
// internal [[Prototype]] to the object you specify
// (Foo.prototype in this case)

Bar.prototype = Object.create( Foo.prototype );
// text says doen't work like you want, but the result is the same ...
//Bar.prototype = Foo.prototype;
// text says doen't work like you want, but the result is the same ...
// Bar.prototype = new Foo();
// both these methods have side-effects

// Beware! Now `Bar.prototype.constructor` is gone,
// and might need to be manually "fixed" if you're
// in the habit of relying on such properties!

Bar.prototype.myLabel = function() {
	return this.label;
};

var a = new Bar( "a", "obj a" );

// a is Bar
console.log(a.myName()); // "a" but myName() func is "inherited" from Foo
console.log(a.myLabel()); // "obj a"

