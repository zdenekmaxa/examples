"""
Demonstrates importing a value from a module.
Changing that value doesn't take effect in the
client code (user.py) unless explicit re-import
or re-assignment.

"""

from base import CONFIG
from base import MyClass
print "1 user.py: CONFIG: %s (id:%s)" % (CONFIG, id(CONFIG))

# the initialization call does not take an effect in the scope
#  of this module, value remains the same, uninitialized
MyClass.init()

# init call changed reference, CONFIG and base.CONFIG are two
# different values from this point on
print "2 user.py: CONFIG: %s (id:%s)" % (CONFIG, id(CONFIG))

# reimporting, does take an effect, returns true base.CONFIG value
from base import CONFIG
print "3 user.py: CONFIG: %s (id:%s)" % (CONFIG, id(CONFIG))

# and this too, access to the base.CONFIG value
config = MyClass.get_config()
print "4 user.py: CONFIG: %s (id:%s)" % (config, id(CONFIG))