import datetime

#Pobieranie i zapis daty dzisiejszej
today = datetime.date.today()
print(today)
print("\n*********************************\n")

#Wpisywanie swojej daty urodzenia
birthday = datetime.date(1998, 5, 6)
print(birthday)
print("\n*********************************\n")

#Obliczanie ile dni się przeżyło
howLongAmIAlive = (today - birthday).days
print(howLongAmIAlive)
print("\n*********************************\n")

#Wyświtelanie jaki dzisiaj jest dzień - jako numer w kalendarzu i jako dzień tygodnia (zakres 0 do 6)
print(today.day)
print(today.weekday())
print("\n*********************************\n")

#Wyświetlanie aktualnej daty w formacie (rok, miesiąc, dzień, godzina, minuty, sekundy, milisekundy
print(datetime.datetime.now())
    #A co będzie za 10 godzin?
tDelta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + tDelta)
print("\n*********************************\n")