# Developed by MD-Nazmus Samin Sunbeam
import gym
from gym import Env, spaces
import pyautogui
import numpy as np
import time
import os

class ComputerEnv(gym.Env):
    """Computer Environment that follows the gym template."""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(ComputerEnv, self).__init__()
        # define observation space
        (width, height) = pyautogui.size()
        self.observation_shape = (width, height, 3)
        self.observation_space = spaces.Box(low=0, high=255, shape=self.observation_shape, dtype=np.uint8)
        # define action space
        self.action_space = spaces.Discrete(10)


    def step(self, action):
        # Flag that marks the termination of an episode
        done = False
        
        # Assert that it is a valid action 
        assert self.action_space.contains(action), "Invalid Action"     
        t = 2
        d = 50
        x_mouse, y_mouse = pyautogui.position()
        # apply actions with mouse and keyboard
        # move horizontally right
        if action == 0:
            x_mouse = d
            pyautogui.move(x_mouse, 0, t)
        # move vertically down
        elif action == 1:
            y_mouse = d
            pyautogui.move(0, y_mouse, t)
        # move horizontally left
        elif action == 2:
            x_mouse = d
            pyautogui.move(x_mouse, 0, t)
        # move vertically down
        elif action == 3:
            y_mouse = d
            pyautogui.move(0, y_mouse, t)
        # move diagonally southeast
        if action == 4:
            x_mouse = d
            y_mouse = d
            pyautogui.move(x_mouse, y_mouse, t)
        # move diagonally southwest
        elif action == 5:
            x_mouse = d
            y_mouse = d
            pyautogui.move(x_mouse, y_mouse, t)
        # move diagonally northeast
        elif action == 6:
            x_mouse = d
            y_mouse = d
            pyautogui.move(x_mouse, y_mouse, t)
        # move diagonally northwest
        elif action == 7:
            x_mouse = d            
            y_mouse = d
            pyautogui.move(x_mouse, y_mouse, t)
        # right click
        elif action == 8:
            pyautogui.click(button='right', clicks=1, interval=0.25)
        # left click
        elif action == 9:
            pyautogui.click(button='left', clicks=1, interval=0.25)
        
        obs = pyautogui.screenshot()
        
        return obs

    def reset(self):
        os.system("killall -9 'Safari'")

    def render(self, mode='human', close=False):
        raise NotImplementedError