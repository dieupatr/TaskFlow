# Dokumentatio der Funktionen von **TaskFlow**

In diesem Teil werden die Bestanteile und Funktionen von 
**TaskFlow** näher beschrieben.



## Laden der Formen Biblothek 

![test](Bilder/Quick_OpenLib.PNG)

    TaskFlowFormLib.drawio
## Die Formen

**Task**

![test](Bilder/FunDoc_Forms.PNG)

**Verzweigung**

![test](Bilder/FuncDoc_Logic.PNG)

**Start/End**

![test](Bilder/FuncDoc_StartEnd.PNG)

******************

## Task_Definitions



    def Print(Objects):

       print(Objects)

    def Input(Objects):

       a=input("a=")

       Objects["in"]=int(a)


## Flow Agent 


    from TaskFlow_QuickFlow import Flow_QuickFlow

    Flow_QuickFlow()


## Konsolen Aufruf


    
    TaskFlowCreator.py Exampel/QuickTaskFlow.drawio QuickFlow