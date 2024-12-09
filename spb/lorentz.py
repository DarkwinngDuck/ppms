import math

temperature = 300
sigma = 400
seebeck = 120

def calculate_Lz(seebeck):
    if seebeck != "":
        result = 0.7426 * (2 + ((math.pi**2 / 3) - 2) /
                          (1 + (2 * math.pi * (math.exp(abs(seebeck) / 86.17333262 - 2) - 
                          1.075 * math.exp(-2)))**(3/2))**(2/3))
        return result
    else:
        return None


def calculate_kappa_e(temperature, sigma, lorentz):
    if temperature != "" and sigma != "" and lorentz != "":
        result = temperature * sigma * lorentz * 0.000001
        return result
    else:
        return None


Lz = calculate_Lz(seebeck)
kappe_e = calculate_kappa_e(temperature, sigma, Lz)

print(Lz)
print(kappe_e)


