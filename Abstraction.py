from abc import ABC, abstractmethod
class Mortgage(ABC):
    # Regular method
    def paySlip(self, amount):
        print("Your mortgage amount:", amount)
    # This function tells us to pass in an argument, without knowing how or what kind of data it will be
    # Abstract method
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(Mortgage):
    # Defines the implementation from its parent Mortgage class
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $1000 limit".format(amount))

obj = DebitCardPayment()
obj.paySlip("$1250")
obj.payment("$1250")
