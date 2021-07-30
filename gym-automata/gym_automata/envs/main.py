from simulation import Simulation

# instantiate simulation with parameters number of automata and hosts
simulation = Simulation(10, 2)
# call run method with parameters number of days and time steps
simulation.run(364, 2000)
