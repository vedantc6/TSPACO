from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("ACO for TSP")

ants_var = StringVar()
iter_var = StringVar()

def reset_values():
   ants_var.set("20") #  ants number recommended
   iter_var.set("10") #  iteration number recommended

def validate_ant_input():
    ants_input = ants_entry.get()
    try:
       ants_var = int(ants_input)
       if(ants_var < 0):
          messagebox.showerror("Error", "Ants Number must be positive integer")
          return False
       elif(ants_var > 48):
          messagebox.showerror("Error", "Ants Number must be smaller than 48")
          return False
       return True
    except ValueError:
       messagebox.showerror("Error", "Ants Number must be an Integer")
       return False

def validate_iter_input():
    iter_input = iter_entry.get()
    try:
       iter_var = int(iter_input)
       if(iter_var < 0):
          messagebox.showerror("Error", "Iteration Number must be positive")
          return False
       elif(iter_var > 100):
          messagebox.showerror("Error", "Iteration Number must be smaller than 100")
          return False
       return True
    except ValueError:
       messagebox.showerror("Error", "Iteration Number must be an Integer")
       return False

def tsp():
   ants_num = int(ants_entry.get())
   iter_num = int(iter_entry.get())

   import paco
   import matplotlib.pyplot as plt
   num_cities = 48
   # Intialize the ACO algorithm with some parameter values
   aco = paco.ACO(num_cities, initial_pheromone=1, alpha=1, beta=3,
                  pheromone_deposit=2, evaporation_constant=0.6)

   with open("./att48.txt") as f:
      content = f.readlines()
   content = [x.strip() for x in content]

   for line in content:
      items = line.split()
      num = int(items[0]) - 1
      x_cord = int(items[1])
      y_cord = int(items[2])
      aco.add_cities(paco.City(num, x_cord, y_cord))

   # run the aco algorithm and return the shortest path
   shortest_path = aco.get_best_path(num_ants=ants_num, num_steps=iter_num)
   # print the shortest path length found in the aco
   print("Number of ants used: {}".format(ants_num))
   print("Shortest route found: {0:.3f}".format(aco.shortest_path_len))

   #plt.axes([0.15, 0.15, 0.8, 0.8])
   plt.figure(1, figsize=[8, 6], facecolor='#F0F0F0')
   plt.margins(0.1, 0.1)
   for i, c in enumerate(aco.cities):  # output the cities to a plot
      if i == 0:
         plt.title("Visualization of ACO algorithms on TSP (48 cities)")
         plt.ylabel("Y - Coordinates of the cities")
         plt.xlabel("X - Coordinates of the cities")
         plt.plot(c.x, c.y, 'gx')  # the first city to be printed will be green
      else:
         plt.plot(c.x, c.y, 'ro')

   for i in range(0, len(
           shortest_path) - 1):  # plot connecting lines between each city visited in the order they are visited
      plt.plot([shortest_path[i].x, shortest_path[i + 1].x], [shortest_path[i].y, shortest_path[i + 1].y], 'c-',
               linewidth=2.0, alpha=0.4)
      plt.pause(0.05)

   plt.show()


validate_cmd_ant = root.register(validate_ant_input)
validate_cmd_iter = root.register(validate_iter_input)

Label(root, text="Ants Number: ").grid(row=0, sticky=W)
ants_entry = Entry(root, textvariable=ants_var, validate='focusout', validatecommand=(validate_cmd_ant))
ants_entry.grid(row=0, column=1)

Label(root, text="Iteration Number:").grid(row=1, sticky=W)
iter_entry = Entry(root, textvariable=iter_var, validate='focusout', validatecommand=(validate_cmd_iter))
iter_entry.grid(row=1, column=1)

bt_reset = Button(root, text="Reset", command=reset_values)
bt_reset.grid(row=2,column=0)
bt_search = Button(root, text ="Search", command=tsp)
bt_search.grid(row=2, column=1)

root.mainloop()