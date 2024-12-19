" Solutions To All Activities "



**" Activity - 1 "**
- Statechart Diagrams: Under statechart_diagrams folder.
- Basic Mode: Code implementations are in src folder.
- requirements.txt is attached.


"How To Run The Files (Simulation)"
- Check requirements.txt with specific version:
pip install -r requirements.txt
- Use Python version 3.13.0.
- Run from run.py. 
- Change the port if needed. 


---"How To Run Unit Tests" 
- Use the command:
python -m unittest discover -s test -p "*_test.py"
- The command can be used to run all the unit tests in one click 





## **Activity - 2**

- PowerPoint slides are available under the `slides` folder.  
- The slides describe the "Stag Hunt" game adapted to the farming robot context, including task allocation and cooperative or competitive dynamics.  
- If viewing in Visual Studio Code, install the `vscode-pdf` extension to access the PDF format of the slides conveniently.  



**"Activity - 3 "**
- Statechart Diagrams - Under statechart_diagrams folder
- Extended Mode : Code implementations under the same src folder as basic :used inheritance under the same file
- Running the Simulation is the same way as Activity - 1 , only the selection of Extended from choices of mode  in  GUI is needed.( mode= extended)



**"Activity - 4 "**
- Powerpoint slides for Novel Mode : Under slides Folder 
- Need to install 'vscode-pdf'  extension if running on vsc to view the pdf format 



**"Activity - 5 "**
- Uploaded via Blackboard 




**"Extra Files"**
- .vscode and settings.json for debugging 




######################################################################################


 **"What I have implemented "** 

The project implements a multi-agent simulation for a robot-assisted farming system. It includes three operational modes: Basic, Extended, and Novel ( Proposal Only). Each mode enhances functionality, focusing on the dynamics of drones and picker robots:

Basic Mode: Features random exploration and basic task assignment.

Extended Mode: Adds coordination improvements and incorporates KPIs, though not fully functional.

Novel Mode: Introduces market-based task allocation, where agents bid for tasks dynamically based on utility scores. (Didnt managed to implement but proposal about implementation presented under slides folder.)



**"Features that are not working "**
- From Extended Mode:  I tried to implement the KPIs for task completion and efficiency , but, I had problems with data collection which broke the system. 



**"Representations"**
The following visual representations are used in the simulation:

Picker Robots: Represented as white circles.

Drones: Represented as cyan arrowheads.

Terrains: Include paths, trees, water, and base areas, differentiated by distinct colors.

Crop Stages: Visualized using different colors to indicate growth stages (e.g., seed, immature, mature).




**"Explanations of Functions"**

General Workflow

Initialization:
The grid and terrain elements (trees, water, crops, paths, and base) are set up.
Agents (drones and picker robots) are initialized and placed on the grid.

Step Function:
All agents execute their respective step methods, updating their state and interacting with the environment.

Task Allocation:
Basic Mode: Tasks are randomly assigned.
Extended Mode: Tasks include additional coordination between agents.
Novel Mode: Tasks are allocated dynamically via an auction system. (No implementation )


Key Functions
Terrain Setup
create_trees(), create_water(), create_crops(), create_path(), create_base():
Generate and place terrain agents on the grid.

Agent Initialization
basic_robot_placement(): Places drones and pickers randomly.
extended_robot_placement(): Places agents with predefined roles and task assignments.
novel_robot_placement(): Assigns tasks via utility-based bidding. ( No implemetation)

Task Allocation
Basic: Random assignment.
Extended: Role-based with  coordination.
