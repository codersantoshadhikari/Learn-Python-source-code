class Customer:
    def __init__(self, id , name , phone ,balance ,CitizenShip):
        self.id = id
        self.name = name
        self.phone = phone
        self.balance = balance
        self.CitizenShip = CitizenShip

        # ### for testing only 
        # c1 = Customer(1 , "bimal" , 1234567890 , 1000 , "3123")
        # print(c1)