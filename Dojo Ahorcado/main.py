import random

def obtener_lista_palabras() -> list:
    with open("palabras.csv", "r", encoding= "utf8") as archivo:
        archivo.readline()
        keys = {
            "Videojuegos": [],
            "Programación": [],
            "Historia": [],
            "Deportes": []
        }
        for linea in archivo:
            categoria, palabra = linea.split(",")
            keys[categoria].append(palabra.strip().lower())
    return keys

def seleccionar_categoria(keys:dict):
    categoria = list(keys.keys())
    categoria_aleatoria = obtener_elemento_aleatorio(categoria)

    return categoria_aleatoria

def seleccionar_palabra(ahorcado:dict,categoria_aleatoria:str):
    # categoria_aleatoria = seleccionar_categoria(ahorcado)
    lista_palabras = ahorcado[categoria_aleatoria]
    palabra_aleatoria = obtener_elemento_aleatorio(lista_palabras)

    return palabra_aleatoria

def obtener_elemento_aleatorio(lista_elementos:list)->any:
    indice_aleatorio = random.randint(0, len(lista_elementos) - 1)
    elemento_aleatoria = lista_elementos[indice_aleatorio]
    return elemento_aleatoria

def iniciar_jugador()->dict:
    jugador={
    'usuario':'',
    'aciertos':0,
    'errores':0,
    'puntuacion final':0,
    }
    return jugador


def actualizar_palabra_oculta(palabra_oculta:str, palabra_resp:str, letra_escrita:str): 
    n = len(palabra_resp)
    bandera=False
    palabra_resp = list(palabra_resp)
    palabra_oculta = list(palabra_oculta  )
    for i in range(n):
        if palabra_resp[i] == letra_escrita:
            palabra_oculta[i]=letra_escrita
            bandera=True
        
    palabra_adivinada = ''.join(palabra_oculta)

    return palabra_adivinada, bandera 




def guardar_puntuacion(usuario:str, puntuacion_final:int)->bool:
    with open('historial.csv','a') as archivo:
        print('se abre doc')
        archivo.write(f"Usuario: {usuario} ({puntuacion_final} puntos) \n")
    return True

def calcular_puntuacion_parcial(usuario:dict, acierto:bool):
    if acierto:
        usuario["aciertos"] += 1
    else:
        usuario["errores"] += 1


def calcular_puntuacion_final(diccionario_juego:dict)-> int:
    aciertos = diccionario_juego["aciertos"]
    errores = diccionario_juego["errores"]
    intentos_restantes = diccionario_juego["intentos_restantes"]

    puntuacion_final = aciertos * 3
    puntuacion_final -= errores
    if intentos_restantes == 0:
        puntuacion_final = 0

    return puntuacion_final
    


def ingresar_nombre_usuario(mensaje:str, mensaje_error:str)->str:
    nombre = input(mensaje)
    while len(nombre) != 3:
        nombre = input(mensaje_error)

    return nombre

def verificar_estado_juego(diccionario_juego:dict, palabra:str)->bool:
    if diccionario_juego["errores"] == 7 or diccionario_juego["aciertos"] == len(palabra):
        return False
    return True

def mostrar_palabra_oculta(palabra_aleatoria:str)->str:
    palabra_oculta = ""
    for i in range(len(palabra_aleatoria)):
        palabra_oculta += "  "
    palabra_oculta = palabra_oculta.strip()
    return palabra_oculta


def traer_palabra_y_categoria(): 
    diccionario_palabras = obtener_lista_palabras()
    categoria = seleccionar_categoria(diccionario_palabras)
    palabra_a_descubrir = seleccionar_palabra(diccionario_palabras,categoria)

    return categoria, palabra_a_descubrir


def jugar_ahorcado()->None:
    #Arranca el juego
    #Aca creamos todas las variables temporales que necesite nuestro juego
    bandera=True
    while bandera:
        verificar_estado_juego()
        #Jugamos
        #Verificamos si la partida sigue o no
        pass
    
    #Pido el nombre del jugador para guardar la puntuación
    calcular_puntuacion_final()
    guardar_puntuacion()


def prueba():
    a = traer_palabra_y_categoria() #palabra y categoria
    jugador = iniciar_jugador() #jugador

    categoria = a[0]
    palabra_a_adivinar = a[1]

    palabra_oculta=mostrar_palabra_oculta(palabra_a_adivinar)
    while verificar_estado_juego(jugador, palabra_a_adivinar):
        # Categoria: Videojuegos
        # Palabra oculta: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


        #Escribe una letra: a

        # Categoria: Videojuegos
        # Palabra oculta: _ a _ a _ _ _ 

        #Escribe una letra: a
        print(palabra_oculta)
        print(f"Categoria: {categoria}\nPalabra oculta: {palabra_oculta}\nPalabra a adivinar: {palabra_a_adivinar}\n") 
        letra_escrita=input("Ingrese una letra")
        

        palabra_oculta, acierto=actualizar_palabra_oculta(palabra_a_adivinar,palabra_oculta,letra_escrita)

        if acierto: 
            print("Acertaste!") 
        else: 
            print('Fallaste.')

        calcular_puntuacion_parcial(jugador, acierto)
        print(jugador) #depurar


prueba()

# print(seleccionar_categoria(diccionario))
# print(seleccionar_palabra(diccionario))
# print(seleccionar_palabra(diccionario))
# print(seleccionar_palabra(diccionario))
# print(seleccionar_palabra(diccionario))