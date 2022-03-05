# # class vroom:
# #     color = "red"
# #     brand= "yolo"                   #Atribute
# # print(vroom.brand)  
    

     

# # class vroom:
# #     brand="yolo"

# # vro1=vroom()
# # vro2= vroom()                   ###instance = objet
# # vro2.brand="haha"
# # print(vro2.brand)
# # print(vro1.brand)
# # vroom.brand= "lol"


# class vroom:
#     cpt=0
#     def __init__(self,Brand):
#         vroom.cpt+=1
#         self.brand= Brand 

# vro1=vroom("haha")
# vro2= vroom("yolo")
# print(vro2.brand)
# print(vro1.brand)
# print(vroom.cpt)

def double(l):
    L=list()
    for i in l:
        L.append(i*2)
    return L

def filtre(l,x):
    L=list()
    i=0 
    j=0
    while i<len(l):
        if l[i]!=x:
            L.append(l[i])
        if l[i]==x and j<1:
            pass
        i+=1
    return L

class Client():
    age=0
    ageMin=0
    ageMax=0
    genre="?"
    genreAim="?"

def ageCorrespond(client1, client2):
    if client1.age>=client2.ageMin  and client1.age<= client2.ageMax:
        if client2.age>=client1.ageMin  and client2.age<= client1.ageMax:
            return True 
        else: 
            return False
    else:
        return False

            
# c1 = Client()
# c1.age = 33
# c1.ageMin = 30
# c1.ageMax = 35
# c2 = Client()
# c2.age = 27
# c2.ageMin = 22
# c2.ageMax = 33
# c3 = Client()
# c3.age = 34
# c3.ageMin = 27
# c3.ageMax = 43
# print(ageCorrespond(c1,c2))
# print(ageCorrespond(c2,c1))
# print(ageCorrespond(c1,c3))
# print(ageCorrespond(c3,c1))
# print(ageCorrespond(c2,c3))
class Client():
    age=0
    ageMin=0
    ageMax=0
    genre="?"
    genreAim="?"
def genreCorrespond(client1, client2):
    if client1.genre in client2.genreAim:
        if client2.genre in client1.genreAim:
            return True
        else: 
            return False
    return False



# c1 = Client()
# c1.genre = 'M'
# c1.genreAim = ['F', '?']
# c2 = Client()
# c2.genre = '?'
# c2.genreAim = ['M', 'F']
# c3 = Client()
# c3.genre = 'F'
# c3.genreAim = ['M']
# print(genreCorrespond(c1,c2))
# print(genreCorrespond(c2,c1))
# print(genreCorrespond(c1,c3))
# print(genreCorrespond(c3,c1))
# print(genreCorrespond(c2,c3))





