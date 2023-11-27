'''
Hay n niños haciendo fila. A cada niño se le asigna un valor de hambre dado en un array de n enteros hunger.
Estás regalando caramelos a estos niños sujeto a los siguientes requisitos:
● Cada niño debe tener al menos un caramelo.
● Los niños con un valor de hambre más alto reciben más dulces que sus vecinos.
Devuelve la cantidad mínima de dulces que necesitas para distribuir los dulces a los niños.
Ejemplo 1:
Entrada -> hunger = [1,0,2]
Salida -> 5
Explicación: Puede asignar al primer, segundo y tercer niño 2, 1 y 2
caramelos respectivamente.
Ejemplo 2:
Entrada -> hunger = [1,2,2]
Salida -> 4
Explicación: Puede asignar al primer, segundo y tercer niño 1, 2 y 1
caramelos respectivamente.
'''

def min_candies(hunger):
  n = len(hunger)
  candies = 0

  for i in range(n):
    candies = max(candies, hunger[i])

  for i in range(1, n):
    if hunger[i] > hunger[i - 1] and candies >= hunger[i] - hunger[i - 1]:
      candies += hunger[i] - hunger[i - 1]

  return print(candies+1)


min_candies([1,0,2])
min_candies([1,2,2])

