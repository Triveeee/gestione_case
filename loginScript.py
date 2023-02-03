#Zerbo & Muratore
#Script che simula un Login (Username & Password & Captcha)
#Max 3 tentativi
# MySQL
# CONNESSIONE MySQL Connector/Python
# Database smaca
# 
# Select
# Tabella Sito
# IDSito |  longitudine  |  latitudine  |  Comune  | Provincia  |  Riferimento
#
# Visualizzazione riga per riga con fetchall()
#
import os
import maskpass
import mysql.connector                          # Libreria connettore MySQL
from mysql.connector import errorcode    # Errori della libreria
#
# Parametri connessione passati come dizionario
# e utilizzo operatore **
#
parametri = {
 'user': '5ai-zerbo',
 'password': '5ai-zerbo',
 'host': '192.168.5.37',
 'database': '5ai-zerbo'
}
#
connessione = mysql.connector.connect(**parametri)      # Connessione al DBMS
cursore = connessione.cursor()                          # Cursore
#
query = "SELECT Login.username, Login.password FROM Login"           # Tabella Sito
#
cursore.execute(query)      # Esecuzione della query
#
records = cursore.fetchall()  # Fetchall
#
# Visualizzazione della lista che
# contiene il risultato della query
# Visualizzazione records per records,

# Chiusur

print(records)
#----------------------------------------------------------
#Dichiarazione
print("===========================================================")
username = str(input("Insericsci l'username: "))
controllo = username in records[0]
print(controllo)
if(controllo == False):
    print("Utente non esistente!! Riprovare!!!")
    input()
    os.system('clear')

password = maskpass.askpass(prompt="Inserisci password: ", mask="*")

while(password.equals(records[1][records[0].index(username)]) == False AND tent < 3):
    tent = tent + 1
    print("|password sbagliata!!")
    input()
    password = maskpass.askpass(prompt="Inserisci password: ", mask="*")
    
cursore.close()
connessione.close()    
    
    
    
    
    
    