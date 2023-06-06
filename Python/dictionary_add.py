# πρόσθεση κλειδιού-τιμής σε λεξικό.
# εκτύπωση του λεξικού σε αλφαβητική σειρά


epafes = {
    "yannis" : 3975, 
    "chara" : 1275,
    "athena" : 1832,
    "roula" : 1111
}


name = input("Dose onoma: ")
tel = input("Dose αριθμό:")

epafes[name] = tel

sorted= list(epafes.items())
sorted.sort()

print(dict(sorted))
