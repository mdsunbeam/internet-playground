# Developed by MD-Nazmus Samin Sunbeam
import os
import time

import gym
import numpy as np
import pyautogui
from gym import Env, spaces


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
        self.action_space = spaces.Discrete(44)


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
        # press a key
        elif action == 10:
            pyautogui.press('a')
        # press b key
        elif action == 11:
            pyautogui.press('b') 
        # press c key
        elif action == 12:
            pyautogui.press('c')
        # press d key
        elif action == 13:
            pyautogui.press('d')
        # press e key
        elif action == 14:
            pyautogui.press('e')
        # press f key
        elif action == 15:
            pyautogui.press('f')
        # press g key
        elif action == 16:
            pyautogui.press('g')
        # press h key
        elif action == 17:
            pyautogui.press('h')
        # press j key
        elif action == 18:
            pyautogui.press('j')
        # press k key
        elif action == 19:
            pyautogui.press('k')
        # press l key
        elif action == 20:
            pyautogui.press('l')
        # press m key
        elif action == 21:
            pyautogui.press('m')
        # press n key
        elif action == 22:
            pyautogui.press('n')
        # press o key
        elif action == 23:
            pyautogui.press('o')
        # press p key
        elif action == 24:
            pyautogui.press('p')
        # press q key
        elif action == 25:
            pyautogui.press('q')
        # press r key
        elif action == 26:
            pyautogui.press('r')
        # press s key
        elif action == 27:
            pyautogui.press('s')
        # press t key
        elif action == 28:
            pyautogui.press('t')
        # press u key
        elif action == 29:
            pyautogui.press('u')
        # press v key
        elif action == 30:
            pyautogui.press('v')
        # press x key
        elif action == 31:
            pyautogui.press('x')
        # press y key
        elif action == 32:
            pyautogui.press('y')
        # press z key
        elif action == 33:
            pyautogui.press('z')
        # press 0 key
        elif action == 34:
            pyautogui.press('0')
        # press 1 key
        elif action == 35:
            pyautogui.press('1')
        # press 2 key
        elif action == 36:
            pyautogui.press('2')
        # press 3 key
        elif action == 37:
            pyautogui.press('3')
        # press 4 key
        elif action == 38:
            pyautogui.press('4')
        # press 5 key
        elif action == 39:
            pyautogui.press('5')
        # press 6 key
        elif action == 40:
            pyautogui.press('6')
        # press 7 key
        elif action == 41:
            pyautogui.press('7')
        # press 8 key
        elif action == 42:
            pyautogui.press('8')
        # press 9 key
        elif action == 43:
            pyautogui.press('9')
        



        obs = pyautogui.screenshot()
        
        return obs

    def reset(self):
        os.system("killall -9 'Safari'")

    def render(self, mode='human', close=False):
        raise NotImplementedError