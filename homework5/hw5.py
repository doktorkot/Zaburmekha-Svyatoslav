class bluetoothdevice:
    def __init__(self, brand, model, max_volume, bassboost):
        self.brand = brand
        self.model = model
        self.max_volume = max_volume
        self.bassboost = bassboost
    def conect(self, connect_link):
        self.bluetoothDevice1 = connect_link

blueD1 = bluetoothdevice("JBL","partybox310",1000,"yes")

blueD2 = bluetoothdevice("JBL","Charge4",300,"no")

blueD1.conect(blueD2)
print(blueD1.bluetoothDevice1.max_volume)