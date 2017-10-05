import gym
from gym import wrappers

from baselines import deepq

def main():
    env = gym.make("CartPole-v0")

    outdir = '/tmp/CartPole'
    env = wrappers.Monitor(env, directory=outdir, force=True)

    act = deepq.load("cartpole_model.pkl")

    for i in range(65):
        obs, done = env.reset(), False
        episode_rew = 0
        while not done:
            obs, rew, done, _ = env.step(act(obs[None])[0])
            episode_rew += rew
        print("Episode reward", episode_rew)

if __name__ == '__main__':
    main()
