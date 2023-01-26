import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})

df_card = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
        
    def available(self):
        """Checks if the hotel is avaiable"""
        availability = df.loc[df["id"] == self.hotel_id,"available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
    
    
class ReservationTicket:
    
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_name = hotel.hotel_name
    
    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel_name}
        """
        return content
    

class CreditCard:
    def __init__(self, number):
        self.number = number
        
    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_card:
            return True
        else:
            return False
        

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security["number"] == 
                                        self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False
    
    
class Spa:
    def __init__(self, hotel_id, name):
        self.hotel_name = df.loc[df["id"] == hotel_id, "name"].squeeze()
        self.name = name
        
        
class ReservationTicketSpa(Spa):
    def generate(self):
        message = f"""
        Thank you for your SPA reservation!
        Here are your SPA booking data:
        Name: {name}
        Hotel name: {self.hotel_name}
        """
        return message

            
    
    
print(df)    
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
        credit_card = SecureCreditCard(number="12345678123456")
        if credit_card.validate(expiration="12/26", holder= "JOHN SMITH", 
                                cvc="123"):
            if credit_card.authenticate(given_password="mypass"):
                hotel.book()
                name = input("Enter your name: ")
                reservation_ticket = ReservationTicket(customer_name=name, 
                                               hotel_object=hotel)
                print(reservation_ticket.generate())
                spa = Spa(hotel_ID, name)
                book_spa = input("Do you want to book spa ticket?: ")
                message = book_spa.lower()
                if message == "yes":
                    spa_ticket = ReservationTicketSpa(hotel_ID)
                    print(spa_ticket.generate())
                else:
                    print("Ok. Thanks anyway!")
                
            else:
                print("Credit card authentification failed")
        else:
            print("There was a problem with your payment.")

else:
    print("Hotel is not free")