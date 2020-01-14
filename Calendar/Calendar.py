import calendar

#Różne rodzaje skrótów dla dni tygodnia (od 1 do 3)
#Dla wartości > 3, zmiana przerw między nazwami
#Dla wartości > 8, całe nazwy dni tygodnia
print(calendar.weekheader(8))
print("\n******************\n")

#Indeks pierwszego dnia tygodnia
print(calendar.firstweekday())
print("\n******************\n")

#Wyświetlanie kalendarza dla stycznia 2020
print(calendar.month(2020, 1))
print("\n******************\n")

#Wypisywanie listy list tygodni, podzielonych na daty poszczególnych dni ("nieistniejące" dni jako "0")
print(calendar.monthcalendar(2020, 1))
print("\n******************\n")

#Wyświetlanie rocznego kalendarza (3 x 4)
print(calendar.calendar(2020))
print("\n******************\n")

#Zmienna zawierające jaki dzień tygodnia wypada w podaną datę (od 0 do 6)
dayOfTheWeek = calendar.weekday(2020, 6, 21)
print(dayOfTheWeek)
print("\n******************\n")

#Wyświetlanie True/False w zależności czy rok jest przestępny czy nie
isLeap = calendar.isleap(2020)
print(isLeap)
print("\n******************\n")

#Wyświetlanie liczby dni przestępnych w następujących latach <2000, 2020)
amountOfLeapDays = calendar.leapdays(2000, 2020)
print(amountOfLeapDays)
print("\n******************\n")
