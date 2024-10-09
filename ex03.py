#
#
#
class Teste:
  def __init__(self, A, B, C):
    self.a = A
    self._b = B
    self.__c = C
  
  #get  
  @property
  def b(self):
    print("você ta lendo b")
    return self._b 
  
  @property
  def c(self):
    print("você ta lendo c")
    return self.__c
  
  #set
  @b.setter
  def b(self, valor):
    if valor < self.c:
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