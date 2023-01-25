from fpdf import FPDF
import time

time = time.asctime()

class Pdf:
    def __init__(self, price, name, t_number):
        self.price = price
        self.name = name
        self.t_number = t_number
    def write(self):
        text = f"""
Fecha y tiempo: {time}
El número de su ticket: {time}/ Nº {self.t_number},
Usted ha comprado: {self.name}
El precio del producto: {self.price} EUR
"""
        gracias = """
Gracias por comprar en nuestras tiendas!
Le esperamos de nuevo!
"""
        pdf = FPDF()
        pdf.add_page()
        pdf.cell
        
        pdf.image(name="exercise/Visual_Studio_Code_1.35_icon.svg.png",
                  w = 10,
                  type="PNG")
        
        pdf.set_font(family="Times",size=16, style="B")
        pdf.cell(h=6, w=1, txt="", border=0, align=0)
        pdf.set_font(family="Times",size=16, style="B")
        pdf.multi_cell(w=0, h=6, txt=gracias, align="J", border=0)
        pdf.set_font(family="Times",size=12)
        pdf.multi_cell(w=0, h=6, txt=text, align="J", border=1)
        pdf.output(f"exercise/tickets/{self.t_number}.pdf")