# Developed by MD-Nazmus Samin Sunbeam
import gym
from gym import Env, spaces
import pyautogui
import numpy as np

class ComputerEnv(gym.Env):
    """Computer Environment that follows the gym template."""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(ComputerEnv, self).__init__()
        # define observation space
        self.screenshot_img = pyautogui.screenshot()
        self.observation_shape = (self.screenshot_img.size[0], self.screenshot_img.size[1], 3)
        self.observation_space = spaces.Box(low=0, high=255, shape=self.observation_shape, dtype=np.uint8)
        # define action space
        self.action_space = spaces.Discrete(4)

    def step(self, action):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def render(self, mode='human', close=False):
        raise NotImplementedError