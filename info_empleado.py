def datos_empleado(nombre, cargo, años):
    if años > 5:
        print(f"el empleado{nombre} trabaja como {cargo},y tiene {años} años de experiencia") 
        print(" es un empleado senior.") 
    else:
        print(f"{nombre} trabaja como {cargo} y tiene {años} años de experiencia.")
        print(" no es empleado senior.") 

nombre = input("Ingrese el nombre del empleado: ")
cargo = input("Ingrese el cargo del empleado: ")
anios_experiencia = int(input("Ingrese los años de experiencia: "))

datos_empleado(nombre, cargo, anios_experiencia)


// prac2 

class NetworkDevice:
    
    def __init__(self, name, ip_address, device_type):
        self.name = name
        self.ip_address = ip_address
        self.device_type = device_type

    def showinfo(self):
        print(f"Dispositivo: {self.name} | IP: {self.ip_address} | Tipo: {self.device_type}")

    def printtest(self):
        print(f"Realizando ping al dispositivo {self.name}")

def crear_dispositivo():
    name = input("Ingrese el nombre del dispositivo: ")
    ip_address = input("Ingrese la dirección IP: ")
    device_type = input("Ingrese el tipo de dispositivo: ")
    return NetworkDevice(name, ip_address, device_type)

dev1 = crear_dispositivo()
dev2 = crear_dispositivo()
dev3 = crear_dispositivo()

for dev in [dev1, dev2, dev3]:
    dev.showinfo()
    dev.printtest()
