import nle
import gym

e = gym.envs.make("NetHackScore-v0", dnum=4)
e.reset()
e.render()
