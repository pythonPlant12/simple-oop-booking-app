import pandas as pd
from fpdf import FPDF
from create_pdf import Pdf

class Product:
    def __init__(self, id_product):
        self.identity_product = id_product

    def buy_product(self):
        name = df.loc[df["id"] == self.identity_product, "name"].squeeze()
        return name
    
    def take_out_from_stock(self):
        value = df.loc[df["id"] == self.identity_product, "in stock"]
        value = value - 1
        df.loc[df["id"] == self.identity_product, "in stock"] = value
        df.to_csv("exercise/articles.csv", index=False)
        print(df)
        
    def check_price(self):
        price = df.loc[df["id"] == self.identity_product, "price"].squeeze()
        return price
    
class Receipt:
    def __init__(self):
        pass
    


t_number = 0

while True:
    df = pd.read_csv("exercise/articles.csv", dtype={"id": str, "in stock": int})
    print(df)
    user_product_id_choise = input("Please, select a product to buy: ")
    
    product_list = []
    for product in df["id"]:
        if product not in product_list:
            product_list.append(product)
    
    if user_product_id_choise in product_list:
        chosen_product = Product(user_product_id_choise)
        t_number = t_number + 1
        name = chosen_product.buy_product()
        chosen_product.take_out_from_stock()
        price = chosen_product.check_price()
        pdf = Pdf(price=price, name=name, t_number=t_number)
        pdf.write()