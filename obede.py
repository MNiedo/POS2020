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

obroty = connection.query(obd.commands.RPM) # Zwraca wartość obrotów z obd (x1)
predkosc = connection.query(obd.commands.SPEED) # Zwraca wartość prędkości z obd (km/h)
stanpaliwa = connection.query(obd.commands.FUEL_STATUS) # Zwraca wartość stanu paliwa (string)
statusczek = connection.query(obd.commands.STATUS) # Zwraca czy były czekendżiny (string)
tempborygo = connection.query(obd.commands.COOLANT_TEMP) # Zwraca wartość temperatury płynu chłodniczego (stopnie celsjusza)
kolektorcis = connection.query(obd.commands.INTAKE_PRESSURE) # Zwraca wartość ciśnienia w kolektorze dolotowym (kPa)
paliwocis = connection.query(obd.commands.FUEL_PRESSURE) # Zwraca wartość ciśnienia paliwa (kPa)
wlottemp = connection.query(obd.commands.INTAKE_TEMP) # Zwraca wartość temperatury na wlocie powietrza (kPa)
maswlotpow = connection.query(obd.commands.MAF)# Zwraca wartość strumienia masy wlotu powietrza (g/s)
czaspracy = connection.query(obd.commands.RUN_TIME) # Zwraca wartość czasu pracy silnika (s)
egrwartosc = connection.query(obd.commands.COMMANDED_EGR) # Zwraca wartość narzuconej EGRowi (%)
egrbledy = connection.query(obd.commands.EGR_ERROR) # Zwraca wartość błędów EGRa (%)
ilepaliwa = connection.query(obd.commands.FUEL_LEVEL) # Zwraca wartość ilości paliwa (UWAGA: %)
ciszew = connection.query(obd.commands.BAROMETRIC_PRESSURE) # Zwraca wartość ciśnienia otoczenia z czujnika barometrycznego (kPa)
napmodkontr = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE) # Zwraca wartość napięcia na module kontrolnym (V)
calobcsil = connection.query(obd.commands.ABSOLUTE_LOAD) # Zwraca wartość całkowitego obciążenia silnika (%)
pedalgazu = connection.query(obd.commands.RELATIVE_ACCEL_POS) # Zwraca wartość relatywnej pozycji pedału gazu (%)
tempoleju = connection.query(obd.commands.OIL_TEMP) # Zwraca wartość temperatury oleju silnikowego (stopnie celsjusza)
czaswtryskpal = connection.query(obd.commands.FUEL_INJECT_TIMING) # Zwraca wartość czasu wtrysku paliwa (stopnie)
spalanie = connection.query(obd.commands.FUEL_RATE) # Zwraca wartość spalania paliwa (UWAGA: l/h)

# Wyświetlanie wartości
print ("Obroty: ",obroty," RPM\n\n")
print ("Prędkosc: ",predkosc," RPM\n\n")
print ("Wartosc stanu paliwa: ",stanpaliwa,"\n\n")
print ("Czy byly czekendziny: ",statusczek,"\n\n")
print ("Temp plynu chlodniczego: ",tempborygo,"°C\n\n")
print ("Cisnienie w kolektorze dolotowym: ",kolektorcis,"kPa\n\n")
print ("Cisnienie paliwa: ",paliwocis,"kPa\n\n")
print ("Temp na wlocie powietrza: ",wlottemp,"°C\n\n")
print ("Masa wlotu powietrza: ",maswlotpow,"g/s\n\n")
print ("Czas pracy silnika :",czaspracy,"s\n\n")
print ("Wartosc EGR: ",egrwartosc,"%\n\n")
print ("Bledy EGR: ",egrbledy,"%\n\n")
print ("Ilosc paliwa: ",ilepaliwa,"%\n\n")
print ("Cisnienie zewnetrzne: ",ciszew,"kPa\n\n")
print ("Napiecie na module kontrolnym: ",napmodkontr,"V\n\n")
print ("Obciazenie silnika: ",calobcsil,"%\n\n")
print ("Pozycja pedalu gazu: ",pedalgazu,"%\n\n")
print ("Temp oleju: ",tempoleju,"°C\n\n")
print ("Wtrysk paliwa: ",czaswtryskpal,"°\n\n")
print ("Spalanie paliwa: ",spalanie,"l/h\n\n")
