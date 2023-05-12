from math import sin, cos, tan,radians

grau = float(input("Digite o angulo(º): "))
print(f'O Angulo {grau} possui:')
print(f"Seno:{sin(radians(grau)):.2f}\nCosseno:{cos(radians(grau)):.2f}\nTangente:{tan(radians(grau)):.2f}")
