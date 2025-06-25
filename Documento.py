def requisito_edad():
    """
   @Pide el ingreso de la edad, y analiza si la edad es valida o no.

    @return: Bool
    """
    entrada = False
    while entrada == False:
        edad = int(input("Ingrese la edad del cliente: "))
        if edad >= 25 and edad <= 80:
            edad_1 = True
        elif edad > 80 and edad <= 105:
            print("Lo sentimos, no cumple con los requisitos de edad para alquilar")
            edad_1 = False
        elif edad < 25 and edad >= 0:
            print("Lo sentimos, no cumple con los requisitos de edad para alquilar")
            edad_1 = False
        else:
            print("Edad no es coherente")
        if edad >= 1 and edad <= 105:
            entrada = True
    return edad 

def datos_cliente ():
    """
    @Registra los datos del cliente.

    @return: List
    """
    nombre_apellido  = input ("Ingrese el nombre y apellido del cliente: ")
    nacionalidad = input ("Ingrese la nacionalidad del cliente: ")
    if nacionalidad.lower () == "argentina":
        residente = input ("¿El cliente es residente?, ingrese 1 para si o cualquier otra tecla para no: ")
        if residente == "1":
            domicilio = input ("Ingrese el domicilio del cliente: ")
            hospedaje = ""
            dni_pasaporte = input ("ingrese el numero de documento del cliente: ")
            telefono = input ("Ingrese el numero de telefono del cliente: ")
            residente = -0.10
        else:
            domicilio = input ("Ingrese el domicilio del cliente: ")
            hospedaje = input ("Ingrese la direccion donde se esta hospedando el cliente: ")
            dni_pasaporte = input ("ingrese el numero de documento del cliente: ")
            telefono = input ("Ingrese el numero de telefono del cliente: ")
            como_contactaron = ("¿Como contacto con la agencia?: ")
            residente = 0
        licencia = input ("¿Tiene licencia de conducir?, inngrese 1 para si o cualquier otra tecla para no: ")
    else:
        domicilio = input ("Ingrese el domicilio del cliente: ")
        hospedaje = input ("Ingrese la direccion donde se esta hospedando el cliente: ")
        dni_pasaporte = input ("ingrese el numero de pasaporte del cliente: ")
        telefono = input ("Ingrese el numero de telefono del cliente: ")
        como_contactaron = ("¿Como contactaron con la agencia?: ")
        licencia = input ("¿Tiene licencia de conducir?, inngrese 1 para si o cualquier otra tecla para no: ")
        residente = 0
    if licencia == "1":   
        n_licencia = input ("Ingrese el numero de la licencia del cliente: ")
        mes_vencimiento_licencia = int (input ("Ingrese el mes de vencimietno de la licencia: "))
        año_vencimietno_licencia = int (input ("Ingrese el año de vencimiento de la licencia: "))
        licencia = True
    else:
        licencia = False
        mes_vencimiento_licencia = 0
        año_vencimietno_licencia = 0
    datos = [nombre_apellido, nacionalidad, domicilio, hospedaje, dni_pasaporte, telefono, licencia, mes_vencimiento_licencia, año_vencimietno_licencia, residente]
    return datos

def vencimiento_licencia (mes, mes_vencimiento, año_vencimiento):
    """
    @Registra los datos del cliente.
    @Parameter: mes (Int): Mes actual
    @Parameter: mes_vencimiento (Int): Mes de vencimiento de la licencia
    @Parameter: año_vencimiento (Int): Año de vencimiento de la licencia 

    @return: Bool
    """
    if mes_vencimiento > mes:
        if año_vencimiento >= 2025:
            vencimiento_licencia = True

        else:
             vencimiento_licencia = False
             print("No es posible alquilar porque su licencia esta vencida")

    elif año_vencimiento > 2025: 
        vencimiento_licencia = True
    else:
        vencimiento_licencia = False
        print("No es posible alquilar porque su licencia esta vencida")    
    return vencimiento_licencia

def vip(mes):
    """
    @Comprueba si el cliente tiene vip o no.
    @Parameter: Mes (Int): Mes actual.
   
    @return: Float
    @return: Int
    """   
    t_vip = input(str("Tiene tarjeta VIP? Ingrese 1 para si o cualquier otra tecla para no: "))
    if t_vip == "1":
        num_t_vip = int(input("Ingrese el numero de su tarjeta VIP: "))
        mes_vencimiento = int(input("Ingrese el mes de vencimiento su tarjeta VIP: "))
        año_vencimiento = int(input("Ingrese el año de vencimiento su tarjeta VIP: "))
        if mes_vencimiento >= mes:
            if año_vencimiento >= 2025:
                descuento_vip = -0.20
            else:
                print ("su tarjeta vip esta vencida")
                descuento_vip = 0
        elif año_vencimiento > 2025:
            descuento_vip = -0.20
        else:
            print ("su tarjeta vip esta vencida")
            descuento_vip = 0
    else:
        descuento_vip = 0
        num_t_vip = ""
    return descuento_vip, num_t_vip

def seleccion_vehiculo (region):
    """
    @Selecciona el vehiculo.
    @Parameter: Region (Str): Region del local.
   
    @return: Tuple
    """    
    entrada = False
    while entrada == False:
        if region.lower () == "bariloche" or region.lower () == "san carlos de bariloche":   
            terreno =  input (" ¿Va a transitar por terrenos montañosos o de ripio? Ingrese 1 para si, o cualquier otra tecla para no ")
            if terreno == "1":
                print ("""
                ingrese 1 para wrangler 4x4 = $200.000
                ingrese 2 para frontier 4x4 = $180.000
                ingrese 3 para hilux 4x4 = $130.000
                """)
                vehiculo_select = input ()
                seguro = 20000
            else:
                print ("""
                ingrese 1 para wrangler 4x4 = $200.000
                ningrese 2 para frontier 4x4 = $180.000
                ingrese 3 para hilux 4x4 = $130.000
                ingrese 4 para etios = $40.000
                """)
                print ("""
                ingrese 5 para Cronos = $50.000
                ingrese 6 para C3 = $60.000
                ingrese 7 para corolla cross = $170.000
                ingrese 8 para taos = $145.000
                ingrese 9 para hiace = $180.000
                """)
                vehiculo_select = input()
                seguro = 10000
        else:
            print ("""
            ingrese 1 para wrangler 4x4 = $200.000
            ingrese 2 para frontier 4x4 = $180.000
            ingrese 3 para hilux 4x4 = $130.000
            ingrese 4 para etios = $40.000
            ingrese 5 para Cronos = $50.000
            ingrese 6 para C3 = $60.000
            ingrese 7 para corolla cross = $170.000
            ingrese 8 para taos = $145.000
            ingrese 9 para hiace = $180.000
            """)
            vehiculo_select = input ()
            seguro = 10000
        if int (vehiculo_select) >= 1 and int (vehiculo_select) <= 9:
            entrada = True
        else:
            print ("La opcion ingresada no es correcta, porfavor intente denuevo")
    vehiculo = ("Jeep Wragler", "Nisan Frontier", "Toyota Hilux", "Toyota Etios", "Fiat Cronos", "Citroen C3", "Corolla Cross", "Volskwagen Taos", "Toyota Hiace")
    tipo_vehiculo = vehiculo [int (vehiculo_select) - 1]
    tupla_precio_vehiculo = (200000, 180000, 130000, 40000, 50000, 60000, 170000, 145000, 180000)
    precio_vehiculo = tupla_precio_vehiculo [int (vehiculo_select) - 1]
    import random
    modelo = random.randint (2022, 2025)
    patente = "AA" + str (random.randint (100, 999)) + "CD"
    chasis = "AEM" + str (random.randint (100, 999)) + "RE" + str (random.randint (10, 99))
    motor = random.randint (100000, 999999999999)
    permiso_municipal = "ZJP" + str (random.randint (1000, 9999))
    datos_vehiculo = (tipo_vehiculo, precio_vehiculo, modelo, patente, chasis, motor, permiso_municipal, seguro)
    return datos_vehiculo

def t_alta_t_baja (mes, region):
    """
    @Verifica si es temporada baja.
    @Parameter: mes (Int): Mes actual.
    @Parameter: region (Str): Region del local.

    @return: Float
    """ 
    if region.lower () == "bariloche" or region.lower () == "san carlos de bariloche":
        if (mes >= 3 and mes <= 5) or (mes >= 10 and  mes <= 11):
             descuento_temporada = -0.15
        else:
            descuento_temporada = 0
    else:
        descuento_temporada = 0
    return descuento_temporada

def equipo_invierno (mes, region):
    """
    @Verifica si es necesario equipo de invierno.
    @Parameter: mes (Int): Mes actual.
    @Parameter: region (Str): Region del local.

    @return: int
    """    
    if region.lower () == "bariloche" or region.lower () == "san carlos de bariloche":
        if mes >= 6 and mes <= 9:
            precio_equipo_invierno = 10000
        else:
            precio_equipo_invierno = 0
    else:
        precio_equipo_invierno = 0
    return precio_equipo_invierno

def dias ():
    """
    @Registra la cantidad de dias de alquiler.
    
    @return: Float
    @return: int
    """    
    fin_semana =  input ("Desea alquilar el vehiculo por un fin de semana (Viernes, Sabado, Domingo), presione 1 para si o cualquier otra tecla para no: ")
    entrada = False
    while entrada == False:
        if fin_semana == "1":
            cantidad_dias = 3
            descuento_recargo_dias = 0.05
        else:
            cantidad_dias = int (input ("ingrese la cantidad de dias que desea alquilar el vehiculo: "))
            if cantidad_dias < 7 and cantidad_dias > 0:
                descuento_recargo_dias = 0 
            elif cantidad_dias >= 7 and cantidad_dias < 30:
                descuento_recargo_dias = -0.05
            elif cantidad_dias >= 30:
                descuento_recargo_dias = -0.10
            else:
                print("La cantidad de dias debe ser mayor a 0, porfavor intentelo denuevo")
        if cantidad_dias > 0:
            entrada = True
    return cantidad_dias, descuento_recargo_dias

def zona (region):
    """
    @Evalua la zona por la que se va a transitar y si se agrega un recargo adicional.
    @Parameter: region (Str): Region del local.

    @return: Float
    """  
    if region.lower () == "bariloche" or region.lower () == "san carlos de bariloche":
        zona = input ("¿Va a transitar por Circuito Chico, Cerro Catedra o la Ruta 40?, presione 1 para si o cualquier otra tecla para no: ")
        if zona == "1":
            recargo_por_zona = 0.05
        else:
            recargo_por_zona = 0 
    else:
        recargo_por_zona = 0
    return recargo_por_zona

def calculo_precio_parcial (precio_vehiculo, precio_equipo_invierno, cantidad_dias, seguro):
    """
    @Calcula el precio parcial sin descuentos ni recargos agregados.
    @Parameter: precio_vehiculo (int): Precio del vehiculo alquilado.
    @Parameter: precio_equipo_invierno (Int): Precio del equipo de invierno.
    @Parameter: cantidad_dias (Int): Cantidad de dias alquilado.
    @Parameter: seguro (int): Precio del seguro

    @return: Float
    """  
    precio_parcial = float (cantidad_dias * (precio_vehiculo + precio_equipo_invierno + seguro))
    return precio_parcial

def calculo_de_descuentos_y_recargos (descuento_vip, precio_parcial, descuento_temporada, recargo_por_zona, descuendo_recargo_dias, descuento_residente):
    """
    @Calcula los descuentos y los recargos.
    @Parameter: descuento_vip (Float): Descuento por ser cliente vip.
    @Parameter: precio_parcial (Float): Precio parcial.
    @Parameter: descuento_temporada (Float): Descuento depende la temporada
    @Parameter: recargo_por_zona (Float): Recargo por zona
    @Parameter: descuendo_recargo_dias (Float): Descuento segun los dias de alquiler.
    @Parameter:descuento_residente (Float): Descuentos por ser residente.

    @return: Tuple
    """ 
    if descuento_residente == -0.10 and descuento_vip == -0.20:
        descuento_residente = 0
    else:
        descuento_residente = descuento_residente
    descuentos_y_recargos = (precio_parcial * descuento_vip, precio_parcial * descuento_temporada, precio_parcial * recargo_por_zona, precio_parcial * descuendo_recargo_dias, precio_parcial * descuento_residente)
    return descuentos_y_recargos

def calculo_precio_total (precio_parcial, descuentos_recargos):
    """
    @Calcula el precio total.
    @Parameter: precio_parcial (Float): Precio parcial.
    @Parameter: descuentos_recargos (Tuple): Descuentos y recargos del alquiler.
    
    @return: Float
    """  
    precio_total = precio_parcial
    for i in range (5):
        precio_total += descuentos_recargos [i]
    return precio_total

def calculo_fecha_devolucion (dia, mes, cantidad_dias):
    """
    @Calcula la fecha de devolución.
    @Parameter: dia (Int): Dia actual.
    @Parameter: mes (Int): Mes actual.
    @Parameter: cantidad_dias (Int): Cantidad de dias de alquiler.
    
    @return: Tuple
    """  
    mes_devolucion = mes
    if (cantidad_dias + dia) > 30:
        dia_devolucion = (cantidad_dias + dia) % 30
        mes_devolucion += 1
        if mes_devolucion > 12:
            mes_devolucion = mes_devolucion % 12
            año_devolucion = 2026
        else:
            año_devolucion = 2025
    else:
        dia_devolucion = cantidad_dias + dia
        año_devolucion = 2025
    fecha_devolucion = (dia_devolucion, mes_devolucion, año_devolucion)
    return fecha_devolucion

def cuestionario_forma_pago (precio_total):
    """
    @Registra la forma de pago.
    @Parameter: precio_total (Float): Precio total del alquiler.
    """ 
    entrada = False
    while entrada == True:
        cuota = input ("Para pagar en 1 cuota presione 1, para pagar en 3 cuotas presione 3 (+5%), para pagar en 6 cuotas presione 6 (+10%), para pagar en 12 cuotas presione 12 (+15%): ")
        if cuota == "1":
            pago = precio_total / int(cuota)
            print (f"El monto a pagar es de: ${pago}\nSu pago fue realizado con exito")
        elif cuota == "3":
            pago = (precio_total + precio_total * 0.05) / int(cuota)
            print (f"El monto de la primera cuota es de: ${pago}\nLa primera cuota fue realizada con exito\nQuedan por abonar {int(cuota) - 1} cuotas de: ${pago}")
        elif cuota == "6":
            pago = (precio_total + precio_total * 0.10) / int(cuota)
            print (f"El monto de la primera cuota es de: ${pago}\nLa primera cuota fue realizada con exito\nQuedan por abonar {int(cuota) - 1} cuotas de: ${pago}")
        elif cuota == "12":
            pago = (precio_total + precio_total * 0.15) / int(cuota)
            print (f"El monto de la primera cuota es de: ${pago}\nLa primera cuota fue realizada con exito\nQuedan por abonar {int(cuota) - 1} cuotas de: ${pago}")
        else:
            print ("La opcion ingresada no es valida, porfavor intente denuevo")
        if cuota == "1" or cuota == "3" or cuota == "6" or cuota == "12":
            entrada = True

import random
dia = random.randint (1, 30)
mes =  random.randint (1, 12)

region = input ("ingrese la region donde se encuentra la agencia: ")

nombre_empleado = input ("ingrese el nombre y apellido del empleado que se va a encargar del alquiler del vehiculo: ")

edad = requisito_edad ()

if edad == True:
    datos = datos_cliente ()
    if datos [6] == True:
        v_licencia = vencimiento_licencia (mes, datos [7], datos [8])
        if v_licencia == True:
            descuento_vip, numero_t_vip = vip (mes)

            datos_vehiculo = seleccion_vehiculo (region)

            descuento_temporada = t_alta_t_baja (mes, region)

            precio_equipo_invierno = equipo_invierno (mes, region)

            cantidad_dias, descuento_recargo_dias = dias ()

            recargo_por_zona = zona (region)

            precio_parcial = calculo_precio_parcial (datos_vehiculo [1], precio_equipo_invierno, cantidad_dias, datos_vehiculo [7])

            descuentos_y_recargos = calculo_de_descuentos_y_recargos (descuento_vip, precio_parcial, descuento_temporada, recargo_por_zona, descuento_recargo_dias, datos [9])

            precio_total = calculo_precio_total (precio_parcial, descuentos_y_recargos)

            fecha_devolucion = calculo_fecha_devolucion (dia, mes, cantidad_dias)

            print (f"{dia}/{mes}/2025")
            print (f"Nº de factura: {random.randint (100000, 9999999999)}")
            print (f"Empleado: {nombre_empleado}")
            factura_cliente = ("Nombre y apellido: ", "Nacionalidad: ", "Domicilio: ", "Hospedaje: ", "Nº de DNI o Pasaporte: ", "Nº de telefono: ")
            factura_vehiculo = ("Tipo de vehiculo: ", "Precio: ", "Modelo: ", "Patente: ", "Nº Chasis: ", "Nº Motor: ", "Nº permiso municipal: ", "Precio del seguro: ")
            factura_alquiler = ("Descuento vip: ", "Descuento por temporada baja: ", "Recargo por zona: ", "Descuento/Recargo por la tarifa (Fin de semana, Diaria, Semanal o Mesual: )", "Descuento residente: ")
            print ("\nDatos del cliente: ")
            for i in range (7):
                print (factura_cliente [i], datos [i])
            print ("\nDatos del vehiculo asignado: ")
            for i in range (8):
                print (factura_vehiculo [i], datos_vehiculo [i])
            print ("\nDetalles del alquiler: ")
            print (f"Cantidad de dias: {cantidad_dias}")
            print (f"Fecha de devolucion: {fecha_devolucion [0]}/{fecha_devolucion [1]}/{fecha_devolucion [2]}")
            for i in range (5):
                print (factura_alquiler [i], descuentos_y_recargos [i])
            print (f"Precio total: {precio_total}")
            
            cuestionario_forma_pago (precio_total)
    else:
            print ("No es posible alquilar el vehiculo porque usted no tiene licencia")