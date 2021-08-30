import gym
from gym_automata.envs.simulation import Simulation
from stable_baselines3 import DQN 

# instantiate custom openai gym env
env = gym.make('gym_automata:automata-v0', automata_number_of=11, hosts_number_of=1893, days_total=364, moves=7)

# instantiate dqn agent
model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=51000)
model.save("dqn_automata")

# reset environment to initialise it
observation = env.reset()

# train agent over 1000 simulations
for i in range(1000):
    action, states = model.predict(observation)
    observation, reward, done, info = env.step(action)
    if done:
        observation = env.reset()
