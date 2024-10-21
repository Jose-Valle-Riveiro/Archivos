import os

class Estudiante:

    def __init__(self):
        self.Carne = ""
        self.Nombre = ""
        self.Color = ""
        self.Carrera = ""

    def CrearEstudiante(self):
        self.Carne = input("INGRESE EL CARNE: ")
        self.Nombre = input("INGRESE EL NOMBRE: ")
        self.Color = input("INGRESE EL COLOR: ")
        self.Carrera = input("INGRESE EL CARRERA: ")

    def EscribirArchivo(self, filename):
        with open(filename,'a') as file:
            file.write(str(self.Carne)+','+ self.Nombre + ',' + str(self.Color)+','+str(self.Carrera)+'|')
        file.close()

class Carrera:
    def __init__(self):
        self.Codigo = ""
        self.Nombre = ""

    def CrearCarrera(self):

        Carreras = LeerCarrera("CARRERAS.txt")
        Name = input("INGRESE EL NOMBRE: ")

        Check = True
        i = 1
        for Carrera in Carreras:
            if(Name == Carrera.Nombre):
               print("ERROR: CARRERA YA EXISTE")
               Check = False
               break
            else:
                i = i + 1

        if(Check == True):
            self.Nombre = Name
            self.Codigo = i


    def EscribirArchivo(self, filename):
 
        with open(filename,'a') as file:
            file.write(str(self.Codigo)+','+ self.Nombre + '|')
        file.close()

def LeerArchivo(filename):

        estudiantes = []
        

        with open(filename) as file:
            contenido = file.read().strip()

            estudiante_info = contenido.split('|')

            for info in estudiante_info:
                if info:
                    atributos = info.split(',')
                    estudiante = Estudiante()
                    estudiante.Carne = atributos[0]
                    estudiante.Nombre = atributos[1]
                    estudiante.Color = atributos[2]
                    estudiante.Carrera = atributos[3]
                    estudiantes.append(estudiante)   
        file.close()

        return estudiantes

def LeerCarrera(filename):
    Carreras = []

    with open(filename) as file:
        contenido = file.read().strip()

        carreras = contenido.split('|')
        
        for carrera in carreras:
            if carrera:
                atributos = carrera.split(',')
                _carrera_ =  Carrera()
                _carrera_.Codigo = atributos[0]
                _carrera_.Nombre = atributos[1]

                Carreras.append(_carrera_)
    file.close()

    return Carreras
      
def imprimir(estudiantes,carreras):

    pass

def AgregarEstudiante():
    pass

def menu():

    print("\nMenú:")
    print("1. Agregar carrera")
    print("2. Agregar estudiante")
    print("3. Mostrar carreras")
    print("4. Mostrar estudiantes")
    print("5. Salir")
    print("\n")



Quedarse = True
while(Quedarse == True):

    menu()
    Choice = int(input("Ingrese una opcion: "))

    os.system('cls')
    match Choice:
        case 1: # AGREGAR CARRERA
            carrera = Carrera()
            carrera.CrearCarrera()

            if carrera.Codigo and carrera.Nombre:
                carrera.EscribirArchivo("CARRERAS.txt")
            
            input('PRESIONE ENTER PARA CERRAR')

        case 2: # AGREGAR ESTUDIANTE
            estudiante = Estudiante()
            estudiante.CrearEstudiante()
            Estudiantes_Lista = LeerArchivo("ARCHIVOS.txt")
            Carreras = LeerCarrera("CARRERAS.txt")
            Check = True
            CheckCarrera = False

            #CHECK CARNE
            for EstudianteRegistrado in Estudiantes_Lista:
                if (int(EstudianteRegistrado.Carne) == int(estudiante.Carne)):
                    print("ERROR: CARNE YA REGISTRADO")
                    Check = False
                    break
            #CHECK CARRERA
            for CarreraRegistrada in Carreras:
                if (int(CarreraRegistrada.Codigo) == int(estudiante.Carrera)):
                    CheckCarrera = True
                    break
            if(CheckCarrera == False):
                print("ERROR: CARRERA NO EXISTE")

            if(Check == True and CheckCarrera == True ):
                estudiante.EscribirArchivo("ARCHIVOS.txt")

            input('PRESIONE ENTER PARA CERRAR')

        case 3: #MOSTRAR CARRERAS
            Carreras = LeerCarrera("CARRERAS.txt")

            for carrera in Carreras:
                print(carrera.Codigo, " | " , carrera.Nombre)
            
            input('PRESIONE ENTER PARA CERRAR')

        case 4: # MOSTRAR ESTUDIANTES
            
            i = 1
            estudiantes = LeerArchivo("ARCHIVOS.txt")
            carreras = LeerCarrera("CARRERAS.txt")
            for estudiante in estudiantes:
                for carrera in carreras:
                    if(estudiante.Carrera == carrera.Codigo):
                        print(i,". ",estudiante.Nombre, "|" , carrera.Nombre , "\n")
                        i = i + 1
                        break

            input('PRESIONE ENTER PARA CERRAR')

        case 5: #SALIR
            Quedarse = False

        case _:
            input("SELECCION INVALIDA: Intente otra")

    os.system('cls')



