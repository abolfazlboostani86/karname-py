esm = input("Name daneshjoo: ")
tedad = int(input("Tedad dars ha: "))
dars_ha = []
nomre_ha = []
for i in range(tedad):
    dars = input("Name dars va nomre: ")
    ajza = dars.split()
    dars_ha.append(ajza[0])
    nomre = float(ajza[1])
    while nomre < 0 or nomre > 20:
        print("Nomre eshtebah ast!")
        nomre = float(input("Nomre ra dobare vared konid: "))
    nomre_ha.append(nomre)
miangin = sum(nomre_ha) / tedad
print("Gozarsh Nomarat")
print("Name Daneshjoo:", esm)
for i in range(tedad):
    print("Dars:", dars_ha[i])
    print("Nomre:", nomre_ha[i])
    if nomre_ha[i] >= 10:
        print("Ghabool")
    else:
        print("Mardood")
print("Miangin:", miangin)