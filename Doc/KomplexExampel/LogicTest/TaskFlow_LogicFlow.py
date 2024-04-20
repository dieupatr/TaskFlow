
from Task_Definitions_LogicFlow import *
import pickle


Objects={ }

#Load Goto
with open('Model_LogicFlow'+'/Goto_LogicFlow.pkl', 'rb') as file:   GotoBlock = pickle.load(file)

#Load Arrows
with open('Model_LogicFlow'+'/Arrows_LogicFlow.pkl', 'rb') as file:   Arrows = pickle.load(file)

#Load Blocks
with open('Model_LogicFlow'+'/Blocks_LogicFlow.pkl', 'rb') as file:   Blocks = pickle.load(file)

#Load StartBlocks
with open('Model_LogicFlow'+'/StartBlocks_LogicFlow.pkl', 'rb') as file:   StartBlocks= pickle.load(file)

#Load DecisionBlocks
with open('Model_LogicFlow'+'/DecisionBlocks_LogicFlow.pkl', 'rb') as file:   DecisionBlocks= pickle.load(file)

Tasks={

       'PrintX' : lambda Objects : PrintX(Objects)



       }



# The flow


def Flow_LogicFlow():
       
       for StartId in StartBlocks:

              print("StartFlow")
              print("")

              Id=StartId

              while True:

                     if (Id in DecisionBlocks) or (Id in GotoBlock):
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

 
                     elif  nextId in GotoBlock:

                            Id=nextId

                            nextId=GotoBlock[Id]           
                    
                            
              return Objects


                     
##########################



       