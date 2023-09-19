def InputProductName() :
    ProductName = input('ใส่ชื่อสินค้า : ')
    return ProductName

def InputProductPrice() :
    ProductPrice = float(input('ใส่ราคาสินค้า : '))
    return ProductPrice

def Calvat(ProductName, ProductPrice) :
    vatPrice = ProductPrice * (7 /100)
    print(f'คุณซื้อสินค้า {ProductName} คุณต้องจ่ายสินค้า {ProductPrice} บาท เเละจ่ายภาษี{vatPrice}')

ProductName = InputProductName()
ProductPrice = InputProductPrice()
Calvat(ProductName, ProductPrice)