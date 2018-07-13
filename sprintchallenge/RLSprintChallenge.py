import gym
import numpy as np

env = gym.make('Taxi-v2')
state = env.reset()
env.render()
env.seed(0)

#Initialize table with all zeros
Q = np.zeros([env.observation_space.n,env.action_space.n])

# Set learning parameters
learning_rate = .85
gamma = .95

episodes = 1000
max_steps = 99
rewards = []

for episode in range(episodes):
    #Reset environment and get first new observation
    state = env.reset()
    total_rewards = 0
    done = False
   
    #The Q-Table learning algorithm
    for step in range(max_steps):
     
        
        #action = np.argmax(Q[state])
        a = np.argmax(Q[state,:] + np.random.randn(1,env.action_space.n)*(1./(episode+1)))
        
        #Get new state and reward from environment
        state1, reward, done, info = env.step(a)
        
        #Update Q-Table with new knowledge
        Q[state,a] += learning_rate*(reward + gamma*np.max(Q[state1,:]) - Q[state,a])
        total_rewards += reward
        state = state1
        if done == True:
            break
    
    rewards.append(total_rewards)
print('Average score over time:', sum(rewards)/episodes)
