# Wi-Fi for Cooperative Vehicular Communication

Vehicular communication is a very popular and important area in the modern world. Several methods and techniques are used for this. Simply vehicular communication systems can be defined as computer networks in which vehicles and roadside units are the communicating nodes, providing each other with information, such as safety warnings and traffic information. In addition vehicular communication has usually developed as a part of intelligent transportation systems (ITS). 

After studying different factors related to this we selected cooperative vehicular communication using WiFi as our project. So we found out different approaches that we can achieve this target. Those are WiFi adhoc, WiFi direct and WiFi beacons. After comparing these approaches we selected WiFi beacons for our project. 

Here we include the vehicle to vehicle(V2V) and vehicle to infrastructure(V2I) communication. Our entire project can be divided into 3 parts. They simulation environment, performance analysis and hardware experiment. In background study we found out the suitability of WiFi beacons for vehicular communications and how we can embed the data inside a beacon frame. In simulation we set up the  WiFi vehicular network  simulation environment. In the performance analysis we simulate the network for different scenarios, evaluate performance metrics, compare with DSRC and identify possible ITS applications. We verify simple scenarios with field experiments in the hardware part.

Omnet++, veins and sumo are used for simulation. Data analysis is done using python and jupyter notebook. Hardware part is done as a proof of concept for simulation using a few WiFi dongles.

In the simulation we simulate several scenarios such as V2V same direction and opposite direction travel and V2I communication. We evaluate performance metrics like packet delivery ratio(PDR), end to end delay and packet inter reception time(PIR) by varying different parameters such as node density, node velocity, beacon frequency, beacon message size and transmit power. After analysing these results we find the suitability of applications under what constraints. 

Our final deliverable of this project is to identify under what constraints, we can use WiFi beacons for ITS applications. Then using the analyzed data we choose the feasibility of WiFi for applications under the categories of critical, non-critical, entertainment and commercial. 
