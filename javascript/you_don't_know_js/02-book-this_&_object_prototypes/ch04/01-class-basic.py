# to demostrates:
#   - encapsulation
#   - instantiation - constructor

class CoolGuy:  
    def __init__(self, trick):
        self.special_trick = trick

    def show_off(self):
        return "my special trick: " + self.special_trick

guy = CoolGuy("jump")
print guy.show_off()

