'''
Se le proporciona una matriz entera height de longitud n. Hay n líneas verticales dibujadas de manera que los dos puntos finales de la i-ésima línea sean (i, 0) y (i, height[i]).
Encuentre dos líneas que junto con el eje x formen un recipiente, de modo que el recipiente contenga la mayor cantidad de agua.
Devuelve la cantidad máxima de agua que un recipiente puede almacenar.
'''

def max_water(height):
  n = len(height)
  table = [[0 for i in range(n)] for j in range(n)]

  for i in range(n):
    for j in range(i, n):
      table[i][j] = min(height[i], height[j]) * (j - i)

  max_water = 0
  for i in range(n):
    for j in range(i + 1, n):
      max_water = max(max_water, table[i][j])

  print(max_water)


max_water([1, 8, 6, 2, 5, 4, 8, 3, 7])

max_water([1,1])
