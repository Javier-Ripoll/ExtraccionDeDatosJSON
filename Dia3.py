import pandas as pd
def uno():#PRIMERA DIVISÓN 
#LECTURA DE JSON 
    teams = pd.read_json("https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/es.1.clubs.json")
#CONTAR EQUIPOS
    total_teams = len(teams)        
#AÑADIR INFO A UNA LISTA 
    club_info = []
    for equipo in teams['clubs']:
        club_name = equipo['name']
        club_code = equipo['code']
        club_info.append(f"{club_name} : {club_code}\n") 
#SACAR POR PANTALLA TOTAL DE EQUIPOS, NOMBRE Y CÓDIGO   
    print(f'Equipos totales {total_teams}')
    print('Nombre y código de los clubs \n')
    for club in club_info:
        print(club)
#ESCRIBIR EN UN FICHERO TXT
    with open ('PrimeraDivision.txt','w',encoding='utf-8') as fichero:
        fichero.write(f'Equipos totales ---> {total_teams} \n')
        fichero.write(f'Nombre de los clubs y sus códigos\n')
        #Recorremos la lista para escribir una por una en el TXT 
        for x in club_info:
            fichero.write(x)
    return True 
          
def dos():#LIGA ALEMANA
    team_alemania = pd.read_json("https://raw.githubusercontent.com/openfootball/football.json/master/2013-14/at.2.clubs.json")
#Contar equipos totales
    total_teams_alemania = len(team_alemania)
#Agregar a una lista
    club_alemania = []
    for club in team_alemania['clubs']:
        club_name = club['name']
        club_code = club['code']
        club_alemania.append(f"{club_name} : {club_code} \n")
#Sacar por pantalla 
    print(f"Equipos totales---> {total_teams_alemania} \n")
    print("Nombre y código de los clubs \n")
    for equipo in club_alemania:
        print(equipo)
#Creación fichero
    with open('LigaAlemana.txt', 'w',encoding='utf-8') as fichero:
        fichero.write(f"Equipos totales ----> {total_teams_alemania} \n")
        fichero.write("Nombre de los equipos y sus códigos \n")
        for x in club_alemania:
            fichero.write(x)
    return True 

def tres ():#JSON LIGA ITALIANA
#Lectura de JSON    
    team_italia = pd.read_json("https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/it.1.clubs.json")
#contar equipos
    total_teams_italia = len(team_italia)
#Agregar a lista
    club_italia = []
    for club in team_italia['clubs']:
        club_name = club['name']
        club_code = club['code']
        club_italia.append(f"{club_name} : {club_code} \n")
#Mostrar por pantalla
    print(f"Equipos totales ----> {total_teams_italia}")
    print("Nombre y códigos de los clubs \n")
    for x in club_italia:
        print(x)
#Creación de fichero
    with open('LigaItaliana.txt','w',encoding='utf-8') as fichero:
        fichero.write(f"Equipos totales---> {total_teams_italia} \n")
        fichero.write("Nombre de los equipos y sus códigos \n")
        for x in club_italia:
            fichero.write(x)
    return True

def cuatro():#JSON LIGA AUSTRIACA
#Lectura de JSON    
    team_austria = pd.read_json("https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/at.2.clubs.json")
#Contar equipos
    equipos_totales_austria = len(team_austria)
#Añadir a la lista
    club_austrtia = []
    for equipo in team_austria['clubs']:
        club_name = equipo['name']
        club_code = equipo['code']
        club_austrtia.append(f"{club_name} : {club_code} \n")
#Mostrar por pantalla 
    print(f"Equipos totales ---> {equipos_totales_austria} \n")
    print("Nombre y códigos de los clubs \n")
    for x in club_austrtia:
        print(x)
#Creación de fichero 
    with open("LigaAustriaca.txt", "w",encoding="utf-8") as fichero:
        fichero.write(f"Equipos totaleas---> {equipos_totales_austria} \n")
        fichero.write("Nombre de los equipos y sus códigos \n")
        for x in club_austrtia:
            fichero.write(x)
def cinco():#JSON LIGA INGLESA
#Lectura de JSON    
    team_ingleses = pd.read_json("https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/at.2.clubs.json")
#Contar equipos
    equipos_totales_ingleses = len(team_ingleses)
#Añadir a la lista
    club_ingleses = []
    for equipo in team_ingleses['clubs']:
        club_name = equipo['name']
        club_code = equipo['code']
        club_ingleses.append(f"{club_name} : {club_code} \n")
#Mostrar por pantalla 
    print(f"Equipos totales ---> {equipos_totales_ingleses} \n")
    print("Nombre y códigos de los clubs \n")
    for x in club_ingleses:
        print(x)
#Creación de fichero 
    with open("LigaInglesa.txt", "w",encoding="utf-8") as fichero:
        fichero.write(f"Equipos totaleas---> {equipos_totales_ingleses} \n")
        fichero.write("Nombre de los equipos y sus códigos \n")
        for x in club_ingleses:
            fichero.write(x)
def seis():#Json que quiera mediante URL de un usuario
#Creación del input para que el usuario introduzca la URL del JSON deseado
    url_json = input("Introduzca la url del JSON deseado ")
#Lectura del JSON     
    team = pd.read_json(url_json)
#Contar equipos
    total_teams = len(team)

#Añadir a lista
    club_team = []
    for equipo in team['clubs']:
        club_name = equipo['name']
        club_code = equipo['code']
        club_team.append(f"{club_name} : {club_code} \n")
#Mostrar por pantalla 
    print(f"Equipos totales ----> {total_teams} \n")
    print("Nombre y códigos de los clubs \n")
    for x in club_team:
        print(x)
#Creación de fichero
    with open("LigaUsuario.txt","w",encoding="utf-8") as fichero:
        fichero.write(f"Equipos totales ----> {total_teams} \n")
        fichero.write("Nombre de los equipos y sus códigos \n")
        for x in club_team:
            fichero.write(x)

def siete():#Salir
    salida = input("Estas seguros que quieres salir [SI] o [NO] ")
   
    if salida.upper() == "SI":
        return False 
    else:
        return True

def switch(opcion):
    diccionario = {
        "1" : "uno()",
        "2" : "dos()",
        "3" : "tres()",
        "4" : "cuatro()",
        "5" : "cinco()",
        "6" : "seis()",
        "7" : "siete()"
}
    return eval(diccionario.get(opcion))
try:
    while (True):
        print("""
        1) Primera División 2020/21
        2) Liga Alemana
        3) Liga Itialiana
        4) Liga Austríaca
        5) Liga Inglesa
        6) Otra liga (ingresar url)
        7) Salir
        """)
        opcion = input()
        continuar = switch(opcion)
        if continuar == False:
            print("Adiós :) ")
            break
except:
    print("Error")

