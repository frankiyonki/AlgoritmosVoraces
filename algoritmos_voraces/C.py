'''
Se te proporciona un array de números enteros nums. Inicialmente te ubicas en el primer índice del array y cada elemento del array representa la longitud máxima de salto desde esa posición.
Devuelve true si puedes llegar al último índice, o false en caso contrario .
Ejemplo 1:
Entrada -> nums = [2,3,1,1,4]
Salida -> true
Explicación: Salta 1 paso del índice 0 al 1, luego 3 pasos hasta el último
índice.
Ejemplo 2:
Entrada -> nums = [3,2,1,0,4]
Salida -> false
Explicación: Siempre llegarás al índice 3 pase lo que pase. Su longitud máxima de salto es 0, lo que imposibilita alcanzar el último índice.
'''

def can_jump(nums):
  n = len(nums)
  table = [False for i in range(n)]
  
  table[n - 1] = True
  for i in range(n - 2, -1, -1):
    for j in range(1, nums[i] + 1):
      if table[i + j]:
        table[i] = True
        break

  return print(table[0])



can_jump([2,3,1,1,4])

can_jump([3,2,1,0,4])