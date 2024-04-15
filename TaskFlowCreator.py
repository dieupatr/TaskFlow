from LexDrawio import *
import pickle

import os

import sys




# Generate by AI


def create_file(file_path, content=None):
    
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            
            if content:
                file.write(content)  
    else:
        pass








# Generate by AI
# Valid +


def pickle_dict(dictionary, filename):
    
    with open(filename, 'wb') as file:
        pickle.dump(dictionary, file)



# Generate by AI
# Valid +

def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        
    except :
        pass
        

    


def FormatFunctionValue(value):

       value=(value.replace(" ", "")).replace("?","")
       value=value.replace("\n", "")

       return value



def BuildActionsDictonary(Function,DiagrammName, RootFolderName):

       Actions={ }

       File=open(RootFolderName+"/List_Actions_"+DiagrammName+".txt",'w')

       for key in Function:

              try:
                     
                     value=Function[key]
                     Actions[value]=f"{value}(Objects)"
                     Func="def "+value+"(Objects):"+"\n        pass\n\n"
                     File.write(Func)
                     
                     
              except:
                     pass


      
       ActionsString=",".join([ "\'"+key+"\' "+": lambda Objects : "+ Actions[key]+"\n" for key in Actions])

       File.close()

       

       return ActionsString




def CodeDeployFlow(DiagrammName, Filename):

    return f"""
import os


RootPath=""
Command=RootPath+"TaskFlowCreator.py "+"{Filename} "+"{DiagrammName}"

print("Deploy {DiagrammName} ")

os.system(Command)
print("")
print("Complete")

print("")
print("")
input("Press enter to continue")

    """



def CodeTaskDefinitions(DiagrammName,Function):

    Func=""

    for key in Function:

        value=Function[key]

        Func=Func+"def "+value+"(Objects):"+"\n        pass\n\n"


    return f"""

{Func}


    """

        

    



def CodeFlowAgent(DiagrammName):
    return f"""
from TaskFlow_{DiagrammName} import Flow_{DiagrammName}


Flow_{DiagrammName}(   )
print(" ")
print(" ")
input("Press enter to continue")


    """
          



def CodeGeneration(ActionsString, NameObjectList, DiagrammName,RootFolderName):

       return (f"""
from Task_Definitions_{DiagrammName} import *
import pickle


Objects=? §

#Load Arrows
with open('{RootFolderName}'+'/Arrows_{DiagrammName}.pkl', 'rb') as file:   Arrows = pickle.load(file)

#Load Blocks
with open('{RootFolderName}'+'/Blocks_{DiagrammName}.pkl', 'rb') as file:   Blocks = pickle.load(file)

#Load StartBlocks
with open('{RootFolderName}'+'/StartBlocks_{DiagrammName}.pkl', 'rb') as file:   StartBlocks= pickle.load(file)

#Load DecisionBlocks
with open('{RootFolderName}'+'/DecisionBlocks_{DiagrammName}.pkl', 'rb') as file:   DecisionBlocks= pickle.load(file)

Tasks=?

       {ActionsString}


       §



# The flow


def Flow_{DiagrammName}():
       
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



       """.replace("?","{")).replace("§","}")
        



def DefineActionFromDigramm( Diagramm, DiagrammName ):
       Variables={}
       Function={}
       ArrowConection={}
       RelevantBlocks={}
       StartBlocks={}
       Labels={   }
       Decision={ }


       FormTaskFlow=["rounded=1", "shape=process2","shape=note","shape=folder" ]

       for block in Diagramm.blocks:

              value=block.Attr["value"]
              Id=block.Attr["id"]
              Type=block.Attr["style"][0]

              if Type=="rounded=0":
                     
                     Variables[value]=""
                     RelevantBlocks[Id]=(value,"Object")


     
                
              if (Type in FormTaskFlow) or Type=="rhombus" :
                     value=FormatFunctionValue(value)
                     
                     Function[Id]=value

                     if Type=="rhombus":
                         Decision[Id]=value
                         
                     else:
                        RelevantBlocks[Id]=(value,"Task")

   
                  
                #Start end
              if block.Attr["style"][2]=="shape=endState":

                     RelevantBlocks[Id]=(" ","End")


              
              if block.Attr["style"][0]=="sketch=0":

                     StartBlocks[Id]=(" ","Start")

              if Type=="edgeLabel":

                parent=block.Attr["parent"]
                Labels[parent]=value
                

       for arrow in Diagramm.arrows:

              source=arrow.Attr["source"]
              target=arrow.Attr["target"]
              Id=arrow.Attr["id"]

              

              if source in ArrowConection:

                  ArrowLabel=Labels[Id]
                  target_0=ArrowConection[source]
                  target_1=target
                  value=Decision[source]

                  if ArrowLabel=="true":
                      
                      Decision[source]=[ ("True",  target_1), ("False", target_0) ,value]
                      
                  else:
                    
                    Decision[source]=[ ("True",  target_0), ("False", target_1) ,value]
                    
                      
                  
                  
                  continue

              ArrowConection[source]=target

        #Create Folder

       RootFolderName="Model_"+DiagrammName

       create_folder(RootFolderName)
        

       #Save Arrows

       pickle_dict(ArrowConection, RootFolderName+"/Arrows_"+DiagrammName+".pkl")

       #Save Blocks

       pickle_dict(RelevantBlocks, RootFolderName+"/Blocks_"+DiagrammName+".pkl")

       #Save Start block

       pickle_dict(StartBlocks, RootFolderName+"/StartBlocks_"+DiagrammName+".pkl")

       #Save Decision

       pickle_dict(Decision, RootFolderName+"/DecisionBlocks_"+DiagrammName+".pkl")

       
       #Save Object's

       NameObjectList=RootFolderName+"/Objects_"+DiagrammName+".pkl"

       pickle_dict(Variables, NameObjectList)

       #Build Action dictonary

       ActionsString=BuildActionsDictonary(Function,DiagrammName, RootFolderName)

        #Code Flow Agent
       code=CodeFlowAgent(DiagrammName)
       create_file("FlowAgent_"+DiagrammName+".py", code)

       #Code Task definitions
       code=CodeTaskDefinitions(DiagrammName,Function)
       create_file("Task_Definitions_"+DiagrammName+".py", code)

       
       
       

       



       return [ActionsString , NameObjectList,RootFolderName]




def BuildActivationDiagramm(file_path,DiagrammName):

    Diagramm=ParseDiagramsFromXmlFile(file_path)

    Diagramm=Diagramm[DiagrammName]

    

    [ActionsString , NameObjectList,RootFolderName]=DefineActionFromDigramm( Diagramm, DiagrammName )

    Code=CodeGeneration(ActionsString, NameObjectList,DiagrammName,RootFolderName)


    

    File=open("TaskFlow_"+DiagrammName+".py", 'w')

    File.write(Code)

    File.close()

    #Generate Deploy Skript

    CodeDeploySkript=CodeDeployFlow(DiagrammName, file_path)

    create_file("DeployFlow_"+DiagrammName+".py",   CodeDeploySkript)

    

    

  
#############Main###############
     
file_path=sys.argv[1]
DiagrammName=sys.argv[2]
BuildActivationDiagramm(file_path,DiagrammName)













