'''
* Tic-Tac-toe Game
* Project Completed by Brahim Kanouhe, university of Ottawa
'''
def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
   range = 0
   while range < len(tab):
      col = 0
      while col < len(tab[range]):
        tab[range][col] = '-'
        col = col + 1
      range = range + 1


def verifieGagner(tab):
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!"
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''
    gagnant_Ou_MatchNul = False
    gagnant = '-'
    gagnant = testLignes(tab)
    if gagnant == '-' :
      gagnant = testCols(tab)
      if gagnant == '-':
        gagnant = testDiags(tab)
        if gagnant == '-':
          if testMatchNul(tab):
            print("Match nul")
            gagnant_Ou_MatchNul = True
    if gagnant != '-':
      print("Joueur ", gagnant, "a gangne!")
      gagnant_Ou_MatchNul = True
    return gagnant_Ou_MatchNul


def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   gagnant = '-'
   rang = 0
   while rang < len(tab):
      if tab[rang][0] != '-':
        if tab[rang][1] == tab[rang][0] and tab[rang][2] == tab[rang][0]:
          gagnant = tab[rang][0]
          break
      rang = rang + 1
   return gagnant


def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   gagnant = '-'
   col = 0
   while col < len(tab):
      if(tab[0][col] != '-'):
        if( (tab[1][col] == tab[0][col]) and (tab[2][col] == tab[0][col])):
          gagnant = tab[0][col]
          break
      col = col + 1
   return gagnant


def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   gagnant = '-'
   if( tab[1][1] != '-'):
      if( (tab[0][0] == tab[1][1]) and (tab[2][2] == tab[1][1])):
          gagnant = tab[1][1]
      else:
          if((tab[0][2] == tab[1][1]) and (tab[2][0] == tab[1][1])):
             gagnant = tab[1][1]
   return gagnant


def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.
   * Si on ne trouve pas de '-' dans la matrice, retourne True.
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   matchNul = True
   rang = 0
   while rang < len(tab) and matchNul:
      col = 0
      while col < len(tab[rang]) and matchNul:
        if(tab[rang][col] == '-'):
          matchNul = False
          break
        col = col + 1
      rang = rang + 1
   return matchNul



