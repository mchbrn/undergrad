import gym
from gym_automata.envs.simulation import Simulation
from stable_baselines3 import DQN 

# instantiate custom openai gym env
env = gym.make('gym_automata:automata-v0', automata_number_of=11, hosts_number_of=1893, days_total=364, moves=7)

# instantiate dqn agent
model = DQN("MlpPolicy", env, verbose=1)
# train agent over 1000 episodes
model.learn(total_timesteps=104000)
model.save("dqn_automata")

# reset environment to initialise it
observation = env.reset()

# use dqn control policy on one full year
for i in range(52):
    action, states = model.predict(observation)
    observation, reward, done, info = env.step(action)
    if done:
        observation = env.reset()
