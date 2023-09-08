# celcius ke fahrenheit :9/5 *(c= +32)
# celcius = 30
celcius = int(input("masukkan derajat celcius :"))
rumus = int ((9/5 * celcius) + 32)
print ("hasilnya :", rumus, "fahrenheit")

# fahrenheit ke celcius : 5/9 * (f= -32)
# fahrenheit = 100
fahrenheit =int(input("masukkan derajat fahrenheit :"))
hasil = int((5/9 * fahrenheit -32))
print ("hasilnya :", hasil, "celcius")

# kelvin ke celcius : c = k-273.5
# kelvin = 25
kelvin = int(input("masukkan derajat kelvin"))
hasil = int(kelvin - 273.15)
print ("hasilnya :", hasil, "kelvin")

