CONFIG = {}
print "base.py accessed, CONFIG: %s (id:%s)" % (CONFIG, id(CONFIG))


class MyClass(object):
    """
    Using the class here brings unnecessary complication to the
    example and effect demonstrated.

    """
    @classmethod
    def init(cls):
        global CONFIG
        CONFIG = dict(a=1, b=2)
        print "base.py __init__ CONFIG: %s (id:%s)" % (CONFIG, id(CONFIG))

    @classmethod
    def get_config(cls):
        return CONFIG