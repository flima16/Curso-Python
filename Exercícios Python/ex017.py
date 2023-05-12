from math import hypot

cat1 = int(input('Cateto Oposto: '))
cat2 = int(input('Cateto Adjacente: '))
print(f'O comprimento da hipotenusa de catetos {cat1}cm e {cat2}cm é igual a {hypot(cat1,cat2):.2f}cm')