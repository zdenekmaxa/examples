# set / get example

class MyObjGetSet(object):
    def __setattr__(self, attr, value):
        print("called with", attr, value)

o = MyObjGetSet()
o.this = "value of this"
try:
    print(o.this)
except AttributeError:
    print("expectantly doesn't exist - was not set")


class MyObjGetSet(object):
    def __setattr__(self, attr, value):
        print("called with", attr, value)
        # works too
        #super().__setattr__(attr, value)
        super(MyObjGetSet, self).__setattr__(attr, value)

o = MyObjGetSet()
o.this = "value of this2"
print(o.this)

