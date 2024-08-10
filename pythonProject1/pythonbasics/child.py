from oops import calcu
class child(calcu):
    num2 = 200

    def completedata(self):

        return self.num + self.num2

obj = child()
print(obj.completedata())


