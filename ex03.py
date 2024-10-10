#
#
# criando uma classe de teste 
class Teste:
  def __init__(self, A, B, C): # 
    self.a = A  # atributo publico 
    self._b = B #  atributo protegido 
    self.__c = C #  atributo privado 
  
  #get  
  @property
  def b(self): # método get para o atributo b
    print("você ta lendo b")
    return self._b 
  
  @property
  def c(self):
    print("você ta lendo c")
    return self.__c
  
  #set
  @b.setter # método set para o atributo b 
  def b(self, valor):
    if valor < self.c: # self.c é um atributo privado, vai ser acessado por meio de um método get 
      print( "erro")
    else:
      self.b = valor

# 
t1 = Teste(1, 2, 3)
#print(t1.a)
#print(t1._b)
#print(t1.c)
#print(dir(t1))
#print(t1._Teste__c)
t1.b = 1