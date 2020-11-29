# Alvin Xiao Pd. 2
# Partner: Simone Livit Pd. 5


# Parent Class
class Macs:
    def __init__(self, memory, storage, cpu, gpu, ethernet_port, wifi):
        self.memory = memory
        self.storage = storage
        self.cpu = cpu
        self.gpu = gpu
        self.ethernet_port = ethernet_port
        self.wifi = wifi

    def specs(self):
        return "Specs:\n {}\n {}\n {}\n {}\n {}\n {}\n".format(self.memory, self.storage, self.cpu, self.gpu,
                                                      self.ethernet_port, self.wifi)


# Child Class
class MacBookAir(Macs):
    def __init__(self, memory, storage, cpu, gpu, ethernet_port, wifi):
        Macs.__init__(self, memory, storage, cpu, gpu, ethernet_port, wifi)


a1 = MacBookAir("8GB", "256GB", "8-core CPU", "7-core GPU", "No ethernet port", "802.11ax Wi-Fi 6 wireless networking")
a2 = MacBookAir("8GB", "512GB", "8-core CPU", "8-core GPU", "No ethernet port", "802.11ax Wi-Fi 6 wireless networking")


# Child Class
class MacBookPro13(Macs):
    def __init__(self, memory, storage, cpu, gpu, ethernet_port, wifi):
        Macs.__init__(self, memory, storage, cpu, gpu, ethernet_port, wifi)


b1 = MacBookPro13("8GB", "256GB", "8-core CPU", "8-core GPU", "No ethernet port",
                  "802.11ax Wi-Fi 6 wireless networking")
b2 = MacBookPro13("8GB", "512GB", "8-core CPU", '8-core GPU', 'No ethernet port',
                  "802.11ax Wi-Fi 6 wireless networking")
b3 = MacBookPro13("16GB", "512GB", "2.0GHz quad-core 10th-generation Intel Core i5 processor",
                  "Intel Iris Plus Graphics", "No ethernet port", "802.11ax Wi-Fi 6 wireless networking")
b4 = MacBookPro13("16GB", "1TB", "2.0GHz quad-core 10th-generation Intel Core i5 processor",
                  "Intel Iris Plus Graphics", "No ethernet port", "802.11ax Wi-Fi 6 wireless networking")


# Child Class
class MacBookPro16(Macs):
    def __init__(self, memory, storage, cpu, gpu, ethernet_port, wifi):
        Macs.__init__(self, memory, storage, cpu, gpu, ethernet_port, wifi)


c1 = MacBookPro16("16GB of 2666MHz DDR4 memory", "512GB", "2.6GHz 6-core 9th-generation Intel Core i7 processor",
                  "AMD Radeon Pro 5300M with 4GB of GDDR6 memory and automatic graphics switching and Intel UHD Graphics 630",
                  "No ethernet port", "802.11ax Wi-Fi 6 wireless networking")
c2 = MacBookPro16("16GB of 2666MHz DDR4 memory", "1TB", "2.6GHz 6-core 9th-generation Intel Core i7 processor",
                  "AMD Radeon Pro 5300M with 4GB of GDDR6 memory and automatic graphics switching and Intel UHD Graphics 630",
                  "No ethernet port", "802.11ax Wi-Fi 6 wireless networking")


# Child Class
class iMac(Macs):
    def __init__(self, memory, storage, cpu, gpu, ethernet_port, wifi):
        Macs.__init__(self, memory, storage, cpu, gpu, ethernet_port, wifi)


d1 = iMac("8GB of 2133MHz DDR4 memory", "256GB", "2.3GHz dual‑core Intel Core i5", "Intel Iris Plus Graphics 640",
          "No ethernet port", "802.11ac Wi-Fi wireless networking")
d2 = iMac("8GB of 2400MHz DDR4 memory", "256GB", "3.6GHz quad‑core Intel Core i3",
          "Radeon Pro 555X with 2GB of GDDR5 memory", "No ethernet port", "802.11ac Wi-Fi wireless networking")
d3 = iMac("8GB of 2666MHz DDR4 memory", "256GB", "3.0GHz 6-core Intel Core i5",
          "Radeon Pro 560X with 4GB of GDDR5 memory", "No ethernet port", "802.11ac Wi-Fi wireless networking")


# Child Class
class iMacPro(Macs):
    def __init__(self, memory, storage, cpu, gpu, ethernet_port, wifi):
        Macs.__init__(self, memory, storage, cpu, gpu, ethernet_port, wifi)


e1 = iMacPro("32GB", "1TB", "3.0GHz 10-core Intel Xeon W processor",
             "Radeon Pro Vega 56 graphics processor with 8GB of HBM2 memory", "10GB Ethernet Port",
             "802.11ac Wi-Fi wireless networking")


# Child Class
class MacPro(Macs):
    def __init__(self, memory, storage, cpu, gpu, ethernet_port, wifi):
        Macs.__init__(self, memory, storage, cpu, gpu, ethernet_port, wifi)


f1 = MacPro("32GB", "256GB", "3.5GHz 8‑core Intel Xeon W processor", "AMD Radeon Pro 580X with 8GB of GDDR5 memory",
            "Two 10GB Ethernet Ports", "802.11ac Wi-Fi wireless networking")


# Child Class
class MacMini(Macs):
    def __init__(self, memory, storage, cpu, gpu, ethernet_port, wifi):
        Macs.__init__(self, memory, storage, cpu, gpu, ethernet_port, wifi)


g1 = MacMini("8GB", "256GB", "8-core CPU", "8-core GPU", "Gigabit ethernet port",
             "802.11ax Wi-Fi 6 wireless networking")
g2 = MacMini("8GB", "512GB", "8-core CPU", "8-core GPU", "Gigabit ethernet port",
             "802.11ax Wi-Fi 6 wireless networking")
g3 = MacMini("8GB", "256GB", "3.0GHz 6-core Intel Core i5", "Intel UHD Graphics 630",
             "Gigabit ethernet port", "802.11ac Wi-Fi wireless networking")


purchase = 0

while purchase == 0:
    print("Options: Macbook Air, Macbook Pro 13, Macbook Pro 16, iMac, iMac Pro, Mac Pro, Mac Mini")
    item = input("What Mac would you like to buy: ")
    if item == "Macbook Air":
        print("Model 1", end=" ")
        print(MacBookAir.specs(a1))
        print("Model 2", end=" ")
        print(MacBookAir.specs(a2))
        purchase = int(input("Would you like to buy one of these? Print 1 if buying, print 0 if you would like to see the others: "))
        if purchase == 0:
            continue
        else:
            print("Money please, thanks.")

    elif item == "Macbook Pro 13":
        print("Model 1", end=" ")
        print(MacBookPro13.specs(b1))
        print("Model 2", end=" ")
        print(MacBookPro13.specs(b2))
        print("Model 3", end=" ")
        print(MacBookPro13.specs(b3))
        print("Model 4", end=" ")
        print(MacBookPro13.specs(b4))
        purchase = int(input("Would you like to buy one of these? Print 1 if buying, print 0 if you would like to see the others: "))
        if purchase == 0:
            continue
        else:
            print("Money please, thanks.")

    elif item == "Macbook Pro 16":
        print("Model 1", end=" ")
        print(MacBookPro16.specs(c1))
        print("Model 2", end=" ")
        print(MacBookPro16.specs(c2))
        purchase = int(input("Would you like to buy one of these? Print 1 if buying, print 0 if you would like to see the others: "))
        if purchase == 0:
            continue
        else:
            print("Money please, thanks.")

    elif item == "iMac":
        print("Model 1", end=" ")
        print(iMac.specs(d1))
        print("Model 2", end=" ")
        print(iMac.specs(d2))
        print("Model 3", end=" ")
        print(iMac.specs(d3))
        purchase = int(input("Would you like to buy one of these? Print 1 if buying, print 0 if you would like to see the others: "))
        if purchase == 0:
            continue
        else:
            print("Money please, thanks.")

    elif item == "iMacPro":
        print("Model 1", end=" ")
        print(iMacPro.specs(e1))
        purchase = int(input("Would you like to buy one of these? Print 1 if buying, print 0 if you would like to see the others: "))
        if purchase == 0:
            continue
        else:
            print("Money please, thanks.")

    elif item == "Mac Pro":
        print("Model 1", end=" ")
        print(MacPro.specs(f1))
        purchase = int(input("Would you like to buy one of these? Print 1 if buying, print 0 if you would like to see the others: "))
        if purchase == 0:
            continue
        else:
            print("Money please, thanks.")

    elif item == "Mac Mini":
        print("Model 1", end=" ")
        print(MacMini.specs(g1))
        print("Model 2", end=" ")
        print(MacMini.specs(g2))
        print("Model 3", end=" ")
        print(MacMini.specs(g3))
        purchase = int(input("Would you like to buy one of these? Print 1 if buying, print 0 if you would like to see the others: "))
        if purchase == 0:
            continue
        else:
            print("Money please, thanks.")