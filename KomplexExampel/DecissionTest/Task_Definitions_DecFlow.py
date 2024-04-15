


def Inputx0(Objects):

       x0=input("x0= ")
       Objects["x0"]=float(x0)

def SetFx(Objects):

       Objects["fx"]=lambda x : x**2 
        

def Fcond(Objects):
       
       x=Objects["x0"]
       y=Objects["fx"](x)
       Objects["y"]=y
       
       if y>=x :
              return True
       else:
              return False
       
def PrintX(Objects):
       print(Objects["x0"])
       

def PrintY(Objects):
       print(Objects["y"])


    
