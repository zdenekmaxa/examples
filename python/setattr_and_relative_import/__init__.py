o = object()
try:
    setattr(o, "attname", "ahoj")
except AttributeError:
    # AttributeError: 'object' object has no attribute 'attname'
    print "AttributeError can't set attribute this way ..."

class O(object):
    pass
o = O()
setattr(o, "attname", "ahoj")
