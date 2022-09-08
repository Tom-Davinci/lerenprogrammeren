mensen = int( input("Met hoeveel mensen bent u?") )
minuten = int( input("Hoeveel minuten wilt u in VR?") )
entree = 7.45 * mensen
vr = ( (minuten /5 ) * 0.37) * mensen
kost = round(entree + vr, 3)
print("Dit geweldige dagje-uit met", mensen, "mensen in de Speelhal met", minuten, "minuten VR kost je maar:", kost, "euro")