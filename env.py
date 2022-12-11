# Developed by MD-Nazmus Samin Sunbeam
# WORK-IN-PROGRESS 
import gym
from gym import spaces

class ComputerEnv(gym.Env):
    """Computer Environment that follows the gym template."""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(ComputerEnv, self).__init__()
        raise NotImplementedError

    def step(self, action):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def render(self, mode='human', close=False):
        raise NotImplementedError