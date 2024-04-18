

def Input(Objects):

        x=input("x=")
        y=input("y=")
        Objects["x"]=float(x)
        Objects["y"]=float(y)

        
        

def Fcond(Objects):

        x=Objects["x"]
        y=Objects["y"]

    

        if x>y:  return "true"

        elif y==3:
                return "default"
        else:
                return "false"


def PrintX(Objects):

        print("true")
        

def PrintY(Objects):
        
        print("false")
        
def PrintZ(Objects):
        
        print("default")



    
