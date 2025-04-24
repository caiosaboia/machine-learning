error = 0.0001
x_inic = 2
def funcao (x):
  return x**2 - 2

def derivada_funcao (x):
  return 2*x

def newton (i):
  x_ant = i
  x_novo = x_ant - (funcao(x_ant) / derivada_funcao(x_ant))
  return x_novo

def teste (x1,x2):
    return x1*x2 

while abs(funcao(x_inic)) > error:
    x_inic = newton(x_inic)

print(f"Raiz aproximada: {x_inic}")
print("Teste da raiz na funcao:",funcao(x_inic))
