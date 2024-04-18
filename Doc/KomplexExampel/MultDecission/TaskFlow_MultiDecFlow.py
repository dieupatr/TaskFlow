
from Task_Definitions_MultiDecFlow import *
import pickle


Objects={ }

#Load Arrows
with open('Model_MultiDecFlow'+'/Arrows_MultiDecFlow.pkl', 'rb') as file:   Arrows = pickle.load(file)

#Load Blocks
with open('Model_MultiDecFlow'+'/Blocks_MultiDecFlow.pkl', 'rb') as file:   Blocks = pickle.load(file)

#Load StartBlocks
with open('Model_MultiDecFlow'+'/StartBlocks_MultiDecFlow.pkl', 'rb') as file:   StartBlocks= pickle.load(file)

#Load DecisionBlocks
with open('Model_MultiDecFlow'+'/DecisionBlocks_MultiDecFlow.pkl', 'rb') as file:   DecisionBlocks= pickle.load(file)

Tasks={

       'Input' : lambda Objects : Input(Objects)
,'Fcond' : lambda Objects : Fcond(Objects)
,'PrintX' : lambda Objects : PrintX(Objects)
,'PrintY' : lambda Objects : PrintY(Objects)
,'PrintZ' : lambda Objects : PrintZ(Objects)



       }



# The flow


def Flow_MultiDecFlow():
       
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

                            value=DecisionBlocks[nextId][0]

                            NextIds=DecisionBlocks[nextId][1]

                            State=Tasks[value](Objects)

                            Id=nextId

                            nextId=NextIds[State]
                            
              return Objects


                     
##########################



       