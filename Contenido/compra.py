

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("plantita")
        if not carrito:
            carrito = self.session["plantita"] = {}
        self.carrito=carrito 
    
    def agregar(self, plantita):
        if plantita.idProducto not in self.carrito.keys():
            self.carrito[plantita.idProducto]={
                "producto_id":plantita.idProducto, 
                "nombre": plantita.tituloProducto,
                "precio": str(plantita.precio),
                "descripcion":  plantita.descripcion,
                "categoria": plantita.categoria,
                "cantidad": 1,
                "total": plantita.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==vehiculo.patente:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = plantita.precio
                    value["total"]= value["total"] + plantita.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, plantita):
        id = plantita.idProducto
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,plantita):
        for key, value in self.carrito.items():
            if key == plantita.idProducto:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- plantita.idProducto
                if value["cantidad"] < 1:   
                    self.eliminar(plantita)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
