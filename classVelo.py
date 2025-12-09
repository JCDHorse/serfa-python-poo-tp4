import random

class Velo:
  __id_velo=[]

  def __init__(self):
    self.__id=self.random_id()
    self.__etat="disponible"
    self.__indice=0

  def get_id(self):
    return self.__id
  
  def get_etat(self):
    return self.__etat
  
  def get_indice(self):
    return self.__indice

  def random_id(self):
    while True:
      random_nb = random.randint(2400, 3000)
      if random_nb not in Velo.__id_velo:
        Velo.__id_velo.append(random_nb)
        return f"V_{random_nb}"
  
  def mettre_en_location(self):
    if self.__etat == "disponible":
      self.__etat = "en_location"
      self.__indice+=1
      return True
    else:
      return False

  def retourner(self):
    if self.__etat == "en_location":
      self.__etat = "disponible"
      return True
    else:
      return False

  def a_reparer(self):
    if self.__etat != "en_reparation":
      self.__etat = "en_reparation"
      self.__indice+=10
      return True
    else:
      return False
  
  def terminer_reparation(self):
    if self.__etat == "en_reparation":
      self.__etat = "disponible"
      return True
    else:
      return False

  def __str__(self):
    return f"Velo(id={self.__id}, etat={self.__etat}, indice={self.__indice})"