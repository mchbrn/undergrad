from benchmark_simulation import Simulation

# instantiate simulation with parameters number of automata, hosts, days and time steps
simulation = Simulation(11, 1893, 364, 7)
simulation.run()
