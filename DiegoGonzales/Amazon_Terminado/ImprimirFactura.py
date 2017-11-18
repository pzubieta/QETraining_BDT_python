class ImprimirFactura:

    def __init__(self):
        self.listPrintFactura = []
        self.nameCliente = ""
        self.cont = 0

    def add_Producto_to_Factura(self, producto):
        self.listPrintFactura.append(producto)

    def length_Factura(self):
        return len(self.listPrintFactura)

    def delete_Factura(self, index):
        self.listPrintFactura.remove(self.listPrintFactura[index])

    def clear_Factura(self):
        self.listPrintFactura.clear()

    def get_FacturaByIndex(self, index):
        return self.listPrintFactura[index]

    def print_Factura(self, nameCliente):
        self.nameCliente = nameCliente
        print("Factura #:", self.cont, " Name:", self.nameCliente)
        print("------------------------------------------")
        print(" NAME   - PRECIO/Uni - CANTIDAD - SubTOTAL")
        print("------------------------------------------")
        cadena = str(self.listPrintFactura[self.cont])
        print(cadena)
        self.suma = 0
        for i in range(len(cadena)):
            if cadena[i] == "=":
                i # solo pa q no me salga error
                #self.suma = self.suma + int(cadena[i+4] + cadena[i+5])
        print("------------------------------------------")
        #print("Total:______________________________", self.suma, "Bs")
        self.cont = self.cont + 1