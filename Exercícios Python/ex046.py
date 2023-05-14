from time import sleep
from emoji import emojize
print(f'{"Contagem Regressiva":=^30}')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize(':sparkler::sparkler::sparkler: \033[1;34mFeliz Ano Novo\033[m :sparkler::sparkler::sparkler:'))