def InputProductName() :
    Name = str(input('ชื่อสินค้า : '))
    return Name

def InputProductPrice() :
    Price = float(input('ราคาสินค้า : '))
    return Price

def CalSellPrice(Price) :
    sellprice = Price +((Price) * 10 / 100)
    print(f'ชื่อสินค้า {Name} ราคาสินค้า {Price} ราคาขาย {sellprice}')
    return sellprice

Name = InputProductName()
Price = InputProductPrice()
CalSellPrice (Price)

