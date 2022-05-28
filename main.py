class Librr:

  def __init__(self):
    self.autor = []
    self.tytul = []
    self.rok = []

  def addbook(self, ksiazka):
    self.rok.append(ksiazka)

  def addmaga(self, egzemplarz):
    temp = list(egzemplarz)


    if temp [0:2] in self.rok:

      self.autor.append(temp[0:2])
      self.tytul.append(temp[0])

    else:
            
      biblioteka.addbook(temp[0:2])
      self.autor.append(temp[0:2])
      self.tytul.append(temp[0])


  def counting(self):
    lista = []
    sort_ing = []


    for ksiazka in self.rok:
      k = self.autor.count(ksiazka)
      ksiazka = [ksiazka[0], ksiazka[1], k]
      lista.append(ksiazka)
      sort_ing = sorted(lista, key = lambda x: x[0])

    
    for obj in sort_ing:
      obj_1 = (obj[0], obj[1], obj[2])
      print(obj_1)
      
biblioteka = Librr()
n = int(input())
for i in range(0,n):
    wejscie = eval(input())
    biblioteka.addmaga(wejscie)

biblioteka.counting()