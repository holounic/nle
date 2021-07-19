import nle
import gym

e = gym.envs.make("NetHackScore-v0", dnum=10, dlevel=4)
e.reset()
e.render()
