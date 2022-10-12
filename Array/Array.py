elevnr=1
points=[0]
betyg=0
while elevnr<11:
    betyg=int(input("Poang elev nr " + str(elevnr) + " : "))
    points.append(betyg)
    elevnr+=1
summa = sum(points)
print("\n","="*27, "\n")
print("Summa av elevers poang: ", summa)