productos = {
    '8475HD': ['Hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['Hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    'GF75HD': [749990,2], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}

def mostrar_menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

def stock_marca(marca):
    encontrados = False
    print(f"Resultados para marca {marca}:")
    for clave, datos in productos.items():
        if marca == datos[0]:
            stock_disponible = stock[clave][1]
            print("---------------------")
            print(f"Marca: {marca}\nModelo: {clave}\nStock disponible: {stock_disponible}\n---------------------\n")
            encontrados = True
    return encontrados

def buscar_precio(p_min, p_max):
    encontrados = False
    resultados = []
    print(f"\nResultados para el rango {p_min} - {p_max}:")
    for clave, datos in stock.items():
        if p_min <= datos[0] <= p_max and datos[1] > 0:
            marca = productos[clave][0]
            resultados.append([marca, clave])
    resultados.sort()
    for items in resultados:
        marca = items[0]
        modelo = items[1]
        print("---------------------")
        print(f"{marca}--{modelo}\n---------------------\n")
        encontrados = True
    return encontrados

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        print("Precio actualizado!")
        return True
    else:
        return False

def main():
    print("Bienvenido a Pybooks. Empresa líder en venta de notebooks.")
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese la opción elegida: "))
        except ValueError:
            print("Debe ingresar número enteros.")
        if opcion == 1:
            marca = input("Ingrese la marca a buscar: ").capitalize()
            if not stock_marca(marca):
                print("No hay coincidencias.")
        elif opcion == 2:
            while True:   
                try:
                    p_min = int(input("Ingrese precio mínimo para rango."))
                    p_max = int(input("Ingrese precio máximo para rango."))
                except ValueError:
                    print("Debe ingresar valores enteros.")
                    continue
                if not buscar_precio(p_min, p_max):
                    print("No existen productos en el rango buscado.")
                    continue
                break
        elif opcion == 3:
            while True:
                modelo = input("Ingrese el modelo a actualizar el precio: ")
                try:
                    p = int(input("Ingrese precio actualizado: "))
                except ValueError:
                    print("Debe ingresar valores enteros.")
                if not actualizar_precio(modelo, p):
                    print("El modelo no existe!")
                repetir = input("Desea actualizar el precio de otro modelo? (si/no)").lower()
                if repetir != "si":
                    break
        elif opcion == 4:
            print("Programa terminado.")
            break
        else:
            print("Ingrese una opción válida!")
                
main()