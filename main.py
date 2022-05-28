class Library:

  def __init__(self):
    self.title = []
    self.autor = []
    self.pub_y = []

  def dodaj_e(self, ksiazka):
    self.pub_y.append(ksiazka)

  def dodaj_e(self, egzemplarz):
    temp = list(egzemplarz)

    if temp [0:2] in self.pub_y:

      self.autor.append(temp[0:2])
      self.title.append(temp[0])

    else:
            
      biblioteka.dodaj_e(temp[0:2])
      self.autor.append(temp[0:2])
      self.title.append(temp[0])

  def zliczanie(self):
    lista = []
    posortowane = []

    for ksiazka in self.pub_y:
      k = self.autor.count(ksiazka)
      ksiazka = [ksiazka[0], ksiazka[1], k]
      lista.append(ksiazka)
      posortowane = sorted(lista, key = lambda x: x[0])
    
    for obj in posortowane:
      obj_1 = (obj[0], obj[1], obj[2])
      print(obj_1)
          
biblioteka = Library()
n = int(input())

for i in range(0,n):
    wejscie = eval(input())
    biblioteka.dodaj_e(wejscie)

biblioteka.zliczanie()