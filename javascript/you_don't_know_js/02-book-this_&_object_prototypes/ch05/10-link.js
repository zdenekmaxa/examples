// links between objects. exists by means of prototypes
// also no use of new and "constructor" functions

var foo = {
	something: function() {
		console.log( "Tell me something good..." );
	}
};

var bar = Object.create( foo );

bar.something(); // Tell me something good...

