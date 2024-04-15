
from Task_Definitions_HillFlow import *
import pickle


Objects={ }

#Load Arrows
with open('Model_HillFlow'+'/Arrows_HillFlow.pkl', 'rb') as file:   Arrows = pickle.load(file)

#Load Blocks
with open('Model_HillFlow'+'/Blocks_HillFlow.pkl', 'rb') as file:   Blocks = pickle.load(file)

#Load StartBlocks
with open('Model_HillFlow'+'/StartBlocks_HillFlow.pkl', 'rb') as file:   StartBlocks= pickle.load(file)

#Load DecisionBlocks
with open('Model_HillFlow'+'/DecisionBlocks_HillFlow.pkl', 'rb') as file:   DecisionBlocks= pickle.load(file)

Tasks={

       'SetX0' : lambda Objects : SetX0(Objects)
,'defineFx' : lambda Objects : defineFx(Objects)
,'RunHillClimbAlg' : lambda Objects : RunHillClimbAlg(Objects)
,'PrintResult' : lambda Objects : PrintResult(Objects)



       }



# The flow


def Flow_HillFlow():
       
       for StartId in StartBlocks:

              print("StartFlow")
              print("")

              Id=StartId

              while True:

                     if Id in DecisionBlocks:
                            pass
                     else:
                            nextId=Arrows[Id]
              

                     if nextId in Blocks:
                     
                     
                            value=Blocks[nextId][0]
                            Type=Blocks[nextId][1]

                            if Type=="Task":  Tasks[value](Objects)

                            if Type=="End":
                                   print("")
                                   print("Flow Complete")
                                   break
                    
                     
                            Id=nextId


                     elif nextId in DecisionBlocks:

                            value=DecisionBlocks[nextId][2]

                            State=Actions[value](Objects)

                            Id=nextId

                            if State==True :  nextId=DecisionBlocks[nextId][0][1]

                            if State==False :  nextId=DecisionBlocks[nextId][1][1]
                            
              return Objects


                     
##########################



       