from code.visualisation import plot as plot
from code.classes import classes as classs
from code.functions import astardelete as astardelete                     
from code.algorithms import Astar2 as Astar
import copy
import matplotlib.pyplot as plt
import time
import csv



if __name__ == '__main__':
    start_time = time.time()
    # Create netlist by loading file in class
    netlist = classs.Netlist("data/netlist_1.csv").netlist

    # Create list for gate coordinates
    gate_coordinates = classs.Gate_coordinate("data/pritn_1.csv").gate_coordinates

    gate_connections = {}





    """
    # TODO
        geef de begin en eindgate mee
        alle gate_coordinaten
        geef een lijst mee met coordinaten waar al draad ligt
    """ 
    ax = plot.make_grid(8, 16)
    # string_gates = [] 
    blocked = []
    allwires = []


    for gate_coordinate in gate_coordinates: 
        # blocked.append(Astar.Node(gate_coordinate[0], gate_coordinate[1], gate_coordinate[2]).set_blocked())
        blocked.append(str(gate_coordinate))
        plot.set_gate(gate_coordinate, ax)

    distances = {}
    # for net in netlist: 
    #     start = gate_coordinates[int(net.gate_1) - 1]
    #     goal = gate_coordinates[int(net.gate_2) - 1]

    for item in netlist:
        gate_start = int(item.gate_1)
        gate_end = int(item.gate_2)

        # Create tuple for gates that have to be connected
        connected_gate = (gate_start, gate_end)

        coordinate_start = gate_coordinates[gate_start - 1]
        coordinate_end = gate_coordinates[gate_end - 1]

        x_coordinate_1 = int(coordinate_start[0])
        y_coordinate_1 = int(coordinate_start[1])

        x_coordinate_2 = int(coordinate_end[0])
        y_coordinate_2 = int(coordinate_end[1])

        # Calculate total shortest distance between gates
        total_dist = abs(x_coordinate_1 - x_coordinate_2) + abs(y_coordinate_1 - y_coordinate_2)

        distances.update({connected_gate: total_dist})

    # Sort connections from smallest to largest distance in dictionary
    distances = list(distances.items())
    for max_number in range(len(distances)-1, -1, -1):
        swapped = False
        for count in range(max_number):
            if distances[count][1] > distances[count + 1][1]:
                distances[count], distances[count + 1] = distances[count + 1], distances[count]
                swapped = True
        if not swapped:
            break

    # grid = Astar.make_grid(gate_coordinates)

    # for gate_crd in gate_coordinates:
    #     grid[tuple(gate_crd)] = False

    # for chips in distances:
        # gate_start = int(chips[0][0])
        # gate_end = int(chips[0][1])

        # connected_gate = (gate_start, gate_end)

        # coordinate_begin = gate_coordinates[gate_start - 1]
        # coordinate_end = gate_coordinates[gate_end - 1]

        # grid[tuple(coordinate_begin)] = True
        # grid[tuple(coordinate_end)] = True

        # # print(grid)
        
        # a_star_path = Astar.a_star(tuple(coordinate_begin), tuple(coordinate_end), grid)
        # if not a_star_path:
        #     for crd in a_star_path: 
        #         grid[crd] = False

        # end_time_3 = time.time()
        # print(a_star_path)
        
        # gate_connections.update({connected_gate: a_star_path})
        # start_time = time.time()
    grid = Astar.make_grid()


    start = (1, 1, 0)
    end = (1, 5, 0)
    search = Astar.a_star(start, end, grid)
    for crd in search:
        grid[crd] = False
    print(search)
    gate_connections.update({(1,1): search})


    start = (0, 2, 0)
    end = (2, 4, 0)
    search = Astar.a_star(start, end, grid)
    print(search)
    end_time = time.time()
    print("time", end_time - start_time) 

    gate_connections.update({(1,2): search})

    print(gate_connections)

    end_time = time.time()
    print("TIME: ", end_time - start_time)

    allConnections = []
    colours = ['b','lightgreen','cyan','m','yellow','k', 'pink']
    colourcounter = 0
    for keys in gate_connections:
        allConnections = gate_connections[keys]
        print(len(allConnections))
        allconnectionlist = []
        for listconnection in allConnections: 
            allconnectionlist.append(listconnection)
        if colourcounter < 6:
            colourcounter += 1
        else: 
            colourcounter = 0

        for i in range(len(allconnectionlist)):
            try: 
                plot.draw_line(allconnectionlist[i], allconnectionlist[i + 1], colours[colourcounter], ax)
            except: 
                break 

    plt.show()