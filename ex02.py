# autor: Michel
# Data: 09/10/2024

# 

# Criar uma classe em Python chamada Fibonacci que possa 
# ser utilizada para: Gerar uma sequência de Fibonacci 
# até um determinado termo.

# declaração da classe
class Fibonacci:
  
  # método gerar sequencia
  def gerar_sequencia(self, n): # n-número
    if n <= 0:
      return []
    elif n == 1:
      return [0]
    else:
      listaFib = [0, 1]
      while len(listaFib) < n:
        proximoTermo = listaFib[-1] + listaFib[-2]
        listaFib.append(proximoTermo)
      return listaFib
    
  def calculaTermo(self, n):
      if n < 0:
        raise ValueError("Erro: valor negativo!")
      elif n ==0:
        return 0
      elif n ==1:
        return 1
      else:
        return self.calculaTermo(n -1) + self.calculaTermo(n -2)