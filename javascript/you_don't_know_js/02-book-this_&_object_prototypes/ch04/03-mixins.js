// vastly simplified `mixin(..)` example:
// creating links between objcts
// copy references to everything, duplicated references
function mixin(sourceObj, targetObj) {
     for (var key in sourceObj) {
         // only copy if not already present
         if (!(key in targetObj)) {
             targetObj[key] = sourceObj[key];
         }
     }
     return targetObj;
}

var Vehicle = {
     wheels: 4,
     engines: 1,
     ignition: function() {
         console.log( "Turning on my engine." );
     },
     drive: function() {
         this.ignition();
         console.log("Steering and moving forward, " + this.wheels +
                     " wheels");
     }
};

var Car = mixin( Vehicle, {
     wheels: 6,
     drive: function() {
         // explicit references to the "base" object in the target
         // called explicit pseudopolymorphism, making absolute reference
         // can be done differently in ES6 via relative pseudopolymorphism
         // set the binding to car, not Vehicle, see difference
         Vehicle.drive.call( this );
         // not illustrated properly in the example in the book
         // need references to inside Car object (wheels)
         // [default binding] - won't work as desired, by default would take
         // Vehicle
         // Vehicle.drive(); 
         // explicit pseudopolymorphism should be avoided whereever possible :)
         console.log("Rolling on all " + this.wheels + " wheels!");
     }
} );

console.log("Car: ");
console.log("engines: " + Car.engines); // inherited through mixin
Car.drive();  // calls inherited Vehicle drive ... check with ignition
console.log("\n");
console.log("Vehicle: ");
console.log("engines: " + Vehicle.engines);
Vehicle.drive();

