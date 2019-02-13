#CONJUNTOS
#Os elementos não são armazenados em uma ordem específica e confiável;
#Conjuntos não contém elementos repetidos.

#DEFININDO UM CONJUNTO
s = {1, 2, 3, 4}
print (s)
set([1, 2, 3, 4])

#Pertinência
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
1 in a
True
5 in a
False

#Também podemos verificar se um conjunto é um subconjunto de outro:
a = {1, 2, 3, 4}
c = {1, 2}
c.issubset(a)
True
a.issubset(c)
False

# continencia e igualdade
contA = 0
contB = 0
a = {1,4,6,8}
b = {1,4,6,8}
for x in a:
    if x in b:
        contA += 1
for y in b:
    if y in a:
        contB += 1
if len(a) == contA and len(b) == contB:
    print("A esta contido em B e B esta contido em A.")

