import pandas as pd

# dtype str is to read all the data in string mode
# You can do as dtype=str but it will convert all dataframe to string
# To make only specific column, dtype={"id": str}
df = pd.read_csv("hotels.csv", dtype={"id": str})

class Hotel:
    
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # This function is to rewrite a .csv file, index=False it to not add
        # new cell.
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
    

print(df)    
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
        name = input("Enter your name: ")
        hotel.book()
        reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        print(reservation_ticket.generate())
else:
    print("Hotel is not free")