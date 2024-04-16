# TaskFlow

In diesem Projekt geht es um das Übersetzen von Abläufen, die als 
Diagramm in **Drawio** vorliegen, in ein Ausführbares **Programmm**.

## Inhaltverzeichniss

1. [Quickstart](##Quickstart)
2. [Funktion Dokumentation](Doc/FucnDoc.md)
3. [Komplexere Besipiele](Doc/FucnDoc.md)


## Quickstart

Bilder
<br></br>
![test](Doc/Bilder/Quick_AddFiles.PNG)

![test](Doc/Bilder/Quick_Flow.PNG)

![test](Doc/Bilder/Quick_Folder.PNG)

![test](Doc/Bilder/Quick_OpenLib.PNG)



    TaskFlowFormLib.drawio

****************************

    TaskFlowCreator.py Exampel/QuickTaskFlow.drawio QuickFlow

******************************


    def Print(Objects):

       print(Objects)

    def Input(Objects):

       a=input("a=")

       Objects["in"]=int(a)

**************************************

    from TaskFlow_QuickFlow import Flow_QuickFlow

    Flow_QuickFlow()

******************************

    StartFlow
    a=6
    {'in': 6}
    Flow Complete