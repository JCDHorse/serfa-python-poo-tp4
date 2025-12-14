import random
from enum import Enum

class VeloEtat(Enum):
    DISPONIBLE = 0
    LOUEE = 1
    REPARATION = 2

class Velo:
  __id_velo=[]

  @staticmethod
  def random_id():
      while True:
          random_nb = random.randint(2400, 3000)
          if random_nb not in Velo.__id_velo:
              Velo.__id_velo.append(random_nb)
              return f"V_{random_nb}"

  def __init__(self):
    self.__id: str = self.random_id()
    self.__etat: VeloEtat = VeloEtat.DISPONIBLE
    self.__indice: int = 0

  @property
  def id(self) -> str:
    return self.__id

  @property
  def etat(self) -> VeloEtat:
    return self.__etat

  @property
  def indice(self) -> int:
    return self.__indice

  def mettre_en_location(self):
    if self.__etat == VeloEtat.DISPONIBLE:
      self.__etat = VeloEtat.LOUEE
      self.__indice+=1
      return True
    else:
      return False

  def retourner(self):
    if self.__etat == VeloEtat.LOUEE:
      self.__etat = VeloEtat.DISPONIBLE
      return True
    else:
      return False

  def a_reparer(self):
    if self.__etat != VeloEtat.REPARATION:
      self.__etat = VeloEtat.REPARATION
      self.__indice+=10
      return True
    else:
      return False
  
  def terminer_reparation(self):
    if self.__etat == VeloEtat.REPARATION:
      self.__etat = VeloEtat.DISPONIBLE
      return True
    else:
      return False

  def __str__(self):
    return f"Velo(id={self.__id}, etat={self.__etat}, indice={self.__indice})"