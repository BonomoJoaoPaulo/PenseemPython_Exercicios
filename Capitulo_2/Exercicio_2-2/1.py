from cmath import pi

r = 5 # em que 'r' eh raio

def calcula_volume_esfera(raio):
    volume = raio**3 * pi * (4/3)
    return volume

print(calcula_volume_esfera(r))
