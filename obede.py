import obd # Potrzebne biblioteki

DISPLAY_PERIOD = 100 # Czas wyświetlania
TIMER_PERIOD = 500 # Zmienna pomocnicza

SERIAL_PORT_NAME = "COM3" # Ustawienie zmiennej nazwy portu, który chcięlibyśmy, żeby był wybrany
SERIAL_PORT_BAUD = 9600 # Liczba bitów na sekundę w przesyle komunikacji
SERIAL_PORT_TIME_OUT = 60 # Czas, po którym nastąpi poddanie się

ELM_CONNECT_SETTLE_PERIOD = 5 # Czasy do ponownego połączenia
ELM_CONNECT_TRY_COUNT = 5 # Ilość prób do połączenia, póki nie będzie katastrofalnego błędu i nie spali się wszystko



connection = obd.OBD() # auto connect

ports = obd.scan_serial() # Próba automatycznego skanowania portu
print (ports) # Wylistowanie wszystkie porty szeregowe
connection = obd.OBD(ports[0]) 

if obd.OBD(ports[0]) == SERIAL_PORT_NAME:
    connection == SERIAL_PORT_NAME
else:
    print ('Prawdopodonie nie ten port co trzeba :(')

# Czas na wyświetlanie statusów
from obd import OBDStatus

if OBDStatus.NOT_CONNECTED == True: # Czy jest jakiekolwiek połączenie
    print ("Jest polaczenie\n")
else:
    print ("NIE MA polaczenia\n")

if OBDStatus.ELM_CONNECTED == True: # Czy jest polaczenie z adapterem zawierającym kontroler ELM327
    print ("Polaczono z adapterem\n")
else:
    print ("NIE polaczono z adapterem\n")

if OBDStatus.OBD_CONNECTED == True: # Czy jest polaczenie z pojazdem przez OBD, ale zapłon wyłączony
    print ("Polaczono z OBD\n")
else:
    print ("NIE polaczono z OBD\n")

if OBDStatus.CAR_CONNECTED == True: # Czy jest polaczenie z pojazdem przez OBD, ale zapłon włączony
    print ("Polaczono z pojazdem\n")
else:
    print ("NIE polaczono z pojazdem\n")



# Czas na wyświetlanie danych

obroty = connection.query(obd.commands.RPM) # Zwraca obroty z obd





print ("Obroty: ",obroty, " RPM\n\n")



