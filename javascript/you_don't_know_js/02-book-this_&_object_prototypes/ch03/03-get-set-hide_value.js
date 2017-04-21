var myObject = {
	// define a getter for `a`
	get a() {
		return this._a_;
        // holding the value in 'a' would result in recursive
        // RangeError: Maximum call stack size exceeded here, thus
        // using a "hidden value"
        // this.a would all itself
	},

	// define a setter for `a`
	set a(val) {
		this._a_ = val;
	}
};

console.log(myObject.a);
myObject.a = "something";
console.log(myObject.a);

