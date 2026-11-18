cen=int(input("enter centimeters:"))
rem=cen
km=cen//100000
cen=cen%100000
meters=cen//100
cen=cen%100
print(f"The {rem} centimeters has {km} kilometers and {meters} meters and {cen} centimeters")