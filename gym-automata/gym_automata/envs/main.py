from simulation import Simulation

# instantiate simulation with parameters number of automata and hosts
simulation = Simulation(10, 602)
# call run method with parameters number of days and time steps per day
simulation.run(364, 20)
