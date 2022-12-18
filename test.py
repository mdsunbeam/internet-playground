# useful commands for shutting down processes
# import os

# os.system("killall -9 'Safari'")
# os.system("killall -9 'Activity Monitor'")

import gym
from env import ComputerEnv

env = ComputerEnv()

while True:
    action = env.action_space.sample()
    obs = env.step(action)