// "Traditional JS Class" `Vehicle`
// parasitic inheritance
// variation of of explicit mixin pattern - is both in some ways explicit and
//      in other ways implicit

function Vehicle() {
    this.wheels = 4;
    this.engines = 1;
};

Vehicle.prototype.ignition = function() {
    console.log( "Turning on my engine." );
};

Vehicle.prototype.drive = function() {
    this.ignition();
    console.log( "Steering and moving forward on " + this.wheels + " wheels");
};

// "Parasitic Class" `Car`
function Car() {
    // first, `car` is a `Vehicle`
    var car = new Vehicle();
    // now, let's modify our `car` to specialize it
    car.wheels = 6;
    // save a privileged reference to `Vehicle::drive()`
    var vehDrive = car.drive;
    // override `Vehicle::drive()`
    car.drive = function() {
        vehDrive.call( this ); // polymorphic call
        console.log("Rolling on all " + this.wheels + " wheels!");
    };
    // constructor behaviour
    return car;
};


// identical behaviour would be without new, car object is returned anyway
// but beware of implicit binding -> see the new example
var myCar = new Car(); 
console.log("Car: " + myCar);
myCar.drive();


