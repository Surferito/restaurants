from random import choice
import random
comentarios = ['a', 'b', 'c', 'd']
num_aleatorio = 2
cambiar_comentario = 0
for i in range(4):

    if num_aleatorio > 1:
        valor_comenta = comentarios[cambiar_comentario]
        cambiar_comentario += 1

    print(valor_comenta)
