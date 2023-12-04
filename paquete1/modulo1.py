class Cliente:
    def __init__(self, nombre, mail, anio, interes):
        self.nombre = nombre
        self.mail = mail
        self.anio = anio
        self.interes = interes

    def __str__(self):
        return f"Se ha creado al cliente {self.nombre}"

    def comprar(self, compra, lugar):
        print(f"El cliente {self.nombre} ha comprado {compra} en la tienda {lugar} \nSe le ha mandado un correo con su factura a {self.mail}")

    def intereses(self):
        texto = ""
        for x in self.interes:
            texto = texto + x + ", "
        texto_final = texto[:-2]
        print(f"El cliente {self.nombre} tiene mucho interes en {texto_final}")