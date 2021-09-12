import gym
from gym_automata.envs.simulation import Simulation
from stable_baselines3 import DQN 

def controlPolicy():
    """Use this function if you would like to use the pretained algorithm on an episode of the simulation"""

    # instantiate custom openai gym env
    env = gym.make('gym_automata:automata-v0', automata_number_of=11, hosts_number_of=1893, days_total=364, moves=7)

    # load pretained dqn
    model = DQN.load("dqn_automata")

    observation = env.reset()

    for i in range(52):
        action, states = model.predict(observation)
        observation, reward, done, info = env.step(action)

controlPolicy()
