"""
Demostrates that class attribute initialization happens just
once per class definition at the first instantiation.

The comp class attribute is initialized at class level
and func() does not get called afterwards.

"""


def func():
    print "func called"
    r = "something"
    return r


class MyClass(object):
    comp = func()

    @classmethod
    def class_met(cls):
        return func()
    
    def __init__(self, test_num):
        print "test number: %s (%s)" % (test_num, self.__class__.__name__)

        # "func called" appears just once for class attribute definition
        if test_num == 1:
            print self.comp

        # "func called" appears at every instantiation plus once for
        # class definition
        if test_num == 2:
            print MyClass.class_met()

        # "func called" appears at every instantiation plus once for
        # class definition (the same as above)
        if test_num == 3:
            print self.class_met()
        

print '\n'
print 70 * '1'
m1 = MyClass(1)

print '\n'
print 70 * '1'
m1 = MyClass(1)

print '\n'
print 70 * '1'
m1 = MyClass(1)

print '\n'
print 70 * '2'
m2 = MyClass(2)

print '\n'
print 70 * '3'
m3 = MyClass(3)

