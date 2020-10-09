class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, name, address):
        self.name = name
        self.address = address


new_customer = Customer("Claudia", "123 Highway")