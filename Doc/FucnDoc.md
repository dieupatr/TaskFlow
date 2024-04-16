# Dokumentatio der Funktionen von **TaskFlow**

In diesem Teil werden die Bestanteile und Funktionen von 
**TaskFlow** näher beschrieben.




## Formen Biblothek
Die **Formen**, für **TaskFlow**, lassen sich über den folgenden **Befehl** in **Drawio** laden.

<img src="Bilder/Quick_OpenLib.PNG" alt="drawing" 
style="width:220px; height: 400px "/>

Der Name der Biblothek ist :

    TaskFlowFormLib.drawio
<br></br>

## Formen

In **TaskFlow** stehen die folgenden Formen zur verfügung :


* **Task**

Auf diesen kann eine Aufgabe , bestehend aus **Buchstaben** und **Zahlen**, definiert werden. Ein Beispiel wäre [HillClimber](KomplexExampel/HillClimber/README.md)


<img src="Bilder/FunDoc_Forms.PNG" alt="drawing" 
style="width:420px; height: 400px "/>

* **Verzweigung**

Hier wird auch eine Aufgabe definiert, aber diese wird mir **True** oder **False** beantowrte. <br></br>
Für nähere Informationen siehe Beispiel [DecissionTest](KomplexExampel/DecissionTest/README.md).

<img src="Bilder/FuncDoc_Logic.PNG" alt="drawing" 
style="width:220px; height: 200px "/>


**Start/End**
Markiert den Start und Endpunkt eines **Flows** . Jeder **Flow** braucht einen **Start** und **Endpunkt**.
![test](Bilder/FuncDoc_StartEnd.PNG)

******************
<br></br>
# Task_Definitions
Die einzelnen **Task** von jedem **Flow** werden in dem Skript **Task_Definitions** näher beschrieben.
<br></br>

Jeder **Block** in dem Diagramm entsprcht einer Funktion. Die Variable **Objects** ist ein **Dictonary** und global. 


    def Task_1(Objects):
        pass

    def Task_2(Objects):
        pass

Ein **Verzweiguns Block** ist hier die Ausnahme, dieser  braucht zwei 
Rückgabewerte **True** und **False**.

    def Decission(Objects):

        if cond:
            return True
        else:
            return False
<br></br>

## Konsolen Aufruf
Mit dem Folgenden **Befehl** kann ein **Flow** übersetzt werden.

    
    TaskFlowCreator.py [Name].drawio [Tabname]

Als Parameter wird der Name der **Drawio** Datei benötigt und der des Tabs auf welchem das Diagramm liegt.


## Arbeitszyklus für einen **Flow**

Wir gehen hier davon aus, das bereits einmal der obige **Konsolen befehl** ausgeführt wurde.

Ist das der Fall, wurden, bezogen auf das Beispiel in **Quickstart**, die folgenden **Datein** generiert.

![test](Bilder/Quick_AddFiles.PNG)

Die einzelnen **Skripte** haben die folgenden bedeutung

* **FlowAgent_QuickFlow.py** : Mit diesem wird der **Flow** gestartet
* **DeployFlow_QuickFlow.py** : Wenn änderungen im **Editor** vorgenommen wurden überträgt dieses **Skript** diese . 
* **Task_Definitions_QuickFlow.py** : Hier werden die einzelnen **Aufgaben** definiert welche im DIiagramm als **Blöcke** dargestellt sind.
* **TaskFlow_QuickFlow.py** : Hier befindet sich der **Algorithmus** für den **Flow** selbst . In der Regel müssen hier keine änderungen vorgenommen werden.

**************

Der Arbeitsablauf für die änderungen am **Flow** ist der folgenden :

1. Den Flow im **Editor** ändern.
2. Das **DeployFlow_QuickFlow.py** ausführen
3. Den Flow  mit **FlowAgent_QuickFlow.py** starten


<br></br>

Der Arbeitsablauf für änderungen in **Task_Definitions_QuickFlow.py** ist:

1. **Task_Definitions_QuickFlow.py** ändern
2. Den Flow  mit **FlowAgent_QuickFlow.py** starten