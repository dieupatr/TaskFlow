
from Task_Definitions_QuickFlow import *
import pickle


Objects={ }

#Load Arrows
with open('Model_QuickFlow'+'/Arrows_QuickFlow.pkl', 'rb') as file:   Arrows = pickle.load(file)

#Load Blocks
with open('Model_QuickFlow'+'/Blocks_QuickFlow.pkl', 'rb') as file:   Blocks = pickle.load(file)

#Load StartBlocks
with open('Model_QuickFlow'+'/StartBlocks_QuickFlow.pkl', 'rb') as file:   StartBlocks= pickle.load(file)

#Load DecisionBlocks
with open('Model_QuickFlow'+'/DecisionBlocks_QuickFlow.pkl', 'rb') as file:   DecisionBlocks= pickle.load(file)

Tasks={

       'Print' : lambda Objects : Print(Objects)
,'Input' : lambda Objects : Input(Objects)



       }



# The flow


def Flow_QuickFlow():
       
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

                                              

                            #if State==True :  nextId=DecisionBlocks[nextId][0][1]

                           # if State==False :  nextId=DecisionBlocks[nextId][1][1]
                            
              return Objects


                     
##########################



       
