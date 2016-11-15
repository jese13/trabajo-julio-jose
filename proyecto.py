
def genera():
  L=[1,2.3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
  mi_lista=[]
  while len(mi_lista)<6:
       numero=random.choice(L)
        if not (numero) in L:
          mi_lista.append(numero)
  return mi_lista

    
def comprueba (X,L):
  if X in L:
    return false
  else: 
    return true
 

