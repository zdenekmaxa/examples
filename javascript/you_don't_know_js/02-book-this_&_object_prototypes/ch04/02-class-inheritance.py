# demostrates:
#   -abstraction - abstract Vehicle
#   -inheritance - Vehicle - Car relation, inheritace even on Python level
#       using new style classes (inherited from object)
#   -polymorphism - call to desired drive() method


class Vehicle(object):
    def __init__(self):
        self.engines = 1

    def ignition(self):
        print "turning on my engine"

    def drive(self):
        self.ignition()
        print "steering and moving forward"


class Car(Vehicle):
    def __init__(self):
        self.wheels = 4

    def drive(self):
        # call to drive from base/super class
        super(Car, self).drive()
        print "rolling on %s wheels" % self.wheels


class SpeedBoat(Vehicle):
    def __init__(self):
        self.engines = 2

    def ignition(self):
        print "turning on my %s engines" % self.engines

    def pilot(self):
        super(SpeedBoat, self).drive()
        print "speeding through the water"


car = Car()
sb = SpeedBoat()
print "Car: "
# car.ignition() inherited method
car.drive()  # polymorphic
print "\n"
print "Speedboat: "
# Vehicle drive() calls polymorphic ignition() belonging to SpeedBoat
sb.pilot()

