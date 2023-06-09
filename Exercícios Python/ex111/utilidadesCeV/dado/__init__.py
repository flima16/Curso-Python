def leiaDinheiro(msg):
   while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha():
            print(f'\033[1;31mERRO: "{n}" é um preço inválido!\033[m')
        else:
            return float(n)
