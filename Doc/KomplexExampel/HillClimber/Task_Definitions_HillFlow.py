

def SetX0(Objects):

        x0=input("x0=")

        Objects["x0"]=float(x0)
        

def defineFx(Objects):

        Objects["Fx"]=lambda x: x**2

        

def RunHillClimbAlg(Objects):

        x0=Objects["x0"]
        y0=Objects["Fx"](x0)

        Objects["Hill"]=y0+1
       

def PrintResult(Objects):

        print(Objects["Hill"])
        
        



    
