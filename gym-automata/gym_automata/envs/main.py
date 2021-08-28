import gym
from gym_automata.envs.simulation import Simulation

import tensorflow as tf
from tf_agents.agents.dqn import dqn_agent
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import sequential
from tf_agents.policies import random_tf_policy
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.trajectories import trajectory
from tf_agents.specs import tensor_spec
from tf_agents.utils import common

env = gym.make('gym_automata:automata-v0', automata_number_of=11, hosts_number_of=1893, days_total=364, moves=7)

observation = env.reset()

for i in range(1000):
    observation, reward, done, info = env.step(action)
