
from Task_Definitions_Test1 import *
import pickle


Objects={ }

#Load Arrows
with open('Model_Test1'+'/Arrows_Test1.pkl', 'rb') as file:   Arrows = pickle.load(file)

#Load Blocks
with open('Model_Test1'+'/Blocks_Test1.pkl', 'rb') as file:   Blocks = pickle.load(file)

#Load StartBlocks
with open('Model_Test1'+'/StartBlocks_Test1.pkl', 'rb') as file:   StartBlocks= pickle.load(file)

#Load DecisionBlocks
with open('Model_Test1'+'/DecisionBlocks_Test1.pkl', 'rb') as file:   DecisionBlocks= pickle.load(file)

Tasks={

       'Print' : lambda Objects : Print(Objects)
,'Input' : lambda Objects : Input(Objects)



       }



# The flow


def Flow_Test1():
       
       for StartId in StartBlocks:

              print("StartFlow")

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



       