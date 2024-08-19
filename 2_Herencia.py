class Carrito_rojo:
    def __init__(self,marca,modelo,precio,Npasajeros):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.Npasajeros = Npasajeros

    def Imprimir(self):
        print(f"""
        > Marca = {self.marca}
        > Modelo = {self.modelo}
        > Precio = {self.precio}
        > Numero de pasajeros = {self.Npasajeros}
        """)


class SUV(Carrito_rojo): #así se indica herencia
    def __init__(self,marca,modelo,precio,Npasajeros,tracción,Alta): #todos los atributos
        super().__init__(marca,modelo,precio,Npasajeros)
        self.traccion=tracción
        self.Alta=Alta

    def Imprimir(self):
        super().Imprimir() #acá llamo al método de la clase padre de nombre Imprimir
        print(f"""
        > Tracción = {self.traccion}
        > Npasajeros = {self.Npasajeros}
        """)


carro_1 = SUV("Toyota","Corolla Cross",23000,5,"4x2",False)
carro_1.Imprimir()