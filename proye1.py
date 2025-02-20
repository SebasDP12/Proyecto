from datetime import datetime

class FlotaVehiculos:
   

    class Nodo:
       
        def __init__(self, vehiculo):
            self.vehiculo = vehiculo
            self.siguiente = None
            self.anterior = None

    def __init__(self):
        self.inicio = None  

    def registrar_vehiculo(self, vehiculo):
       
        nuevo_nodo = self.Nodo(vehiculo)
        if not self.inicio:
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
        print(f"✅ Vehículo {vehiculo.placa} agregado correctamente.")

    def buscar_vehiculo(self, placa):
   
        actual = self.inicio
        while actual:
            if actual.vehiculo.placa == placa:
                return actual.vehiculo
            actual = actual.siguiente
        return None

    def mostrar_vehiculos(self):
  
        if not self.inicio:
            print("⚠ No hay vehículos registrados.")
            return
        actual = self.inicio
        while actual:
            v = actual.vehiculo
            print(f"[{v.placa}] {v.marca} {v.modelo} - Año: {v.anio} - Kilometraje: {v.kilometraje} km")
            actual = actual.siguiente


class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.historial = None

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        if 6 <= len(placa) <= 8:
            self.__placa = placa
        else:
            raise ValueError("⚠ Error: La placa debe tener entre 6 y 8 caracteres.")

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        anio_actual = datetime.now().year
        if 2000 <= anio <= anio_actual:
            self.__anio = anio
        else:
            raise ValueError("⚠ Error: Año inválido.")

    @property
    def kilometraje(self):
        return self.__kilometraje

    @kilometraje.setter
    def kilometraje(self, kilometraje):
        if kilometraje >= 0:
            self.__kilometraje = kilometraje
        else:
            raise ValueError("⚠ ERROR: El kilometraje no puede ser negativo.")

    def actualizar_kilometraje(self, nuevo_km):

        if nuevo_km >= self.kilometraje:
            self.kilometraje = nuevo_km
            print("✅ Kilometraje actualizado correctamente.")
        else:
            print("⚠ Error: No se puede reducir el kilometraje registrado.")

    def agregar_mantenimiento(self, mantenimiento):
     
        if self.historial is None:
            self.historial = mantenimiento
            mantenimiento.siguiente = mantenimiento 
        else:
            actual = self.historial
            while actual.siguiente != self.historial:
                actual = actual.siguiente
            actual.siguiente = mantenimiento
            mantenimiento.siguiente = self.historial

    def calcular_costo_total(self):
        
        if self.historial is None:
            return 0
        total = 0
        actual = self.historial
        while True:
            total += actual.costo
            actual = actual.siguiente
            if actual == self.historial:
                break
        return total


class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo
        self.siguiente = None

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        try:
            datetime.strptime(fecha, "%d-%m-%Y")
            self.__fecha = fecha
        except ValueError:
            raise ValueError("⚠ Error: Formato de fecha incorrecto (DD-MM-YYYY).")

    @property
    def costo(self):
        return self.__costo

    @costo.setter
    def costo(self, costo):
        if costo < 0:
            raise ValueError("⚠ Error: El costo debe ser positivo.")
        self.__costo = costo


def mostrar_menu():
    print("\n--- 📌 GESTIÓN DE FLOTA ---")
    print("1️⃣ Registrar nuevo vehículo")
    print("2️⃣ Ver lista de vehículos")
    print("3️⃣ Agregar mantenimiento")
    print("4️⃣ Calcular egreso total")
    print("5️⃣ Salir")


flota = FlotaVehiculos()

while True:
    mostrar_menu()
    opcion = input("🛠 Seleccione una opción: ")

    if opcion == "1":
        try:
            vehiculo = Vehiculo(
                input("📌 Placa: "), input("📌 Marca: "), input("📌 Modelo: "), int(input("📌 Año: ")), int(input("📌 Kilometraje: "))
            )
            flota.registrar_vehiculo(vehiculo)
        except ValueError as e:
            print(e)

    elif opcion == "2":
        flota.mostrar_vehiculos()

    elif opcion == "3":
        placa = input("🔍 Ingrese la placa del vehículo: ")
        vehiculo = flota.buscar_vehiculo(placa)
        if vehiculo:
            try:
                mantenimiento = Mantenimiento(
                    input("📆 Fecha (DD-MM-YYYY): "), input("📝 Descripción: "), float(input("💰 Costo: "))
                )
                vehiculo.agregar_mantenimiento(mantenimiento)
                print("✅ Mantenimiento registrado.")
            except ValueError as e:
                print(e)
        else:
            print("⚠ Vehículo no encontrado.")

    elif opcion == "4":
        placa = input("🔍 Ingrese la placa del vehículo: ")
        vehiculo = flota.buscar_vehiculo(placa)
        if vehiculo:
            print(f"💰 Costo total de mantenimientos: {vehiculo.calcular_costo_total()} Q")
        else:
            print("⚠ Vehículo no encontrado.")

    elif opcion == "5":
        print("👋 Saliendo del sistema...")
        break

    else:
        print("⚠ Opción no válida, intente de nuevo.")
