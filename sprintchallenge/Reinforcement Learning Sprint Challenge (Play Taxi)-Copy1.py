
# coding: utf-8

# In[7]:


import numpy as np
import gym
import random


# In[8]:


env = gym.make("Taxi-v2")


# In[9]:


action_size = env.action_space.n
state_size = env.observation_space.n
print(action_size)
print(state_size)
#print(env.reset())


# In[10]:


qtable = np.zeros((state_size, action_size))
print(qtable)


# In[62]:


total_episodes = 10000        # Total episodes
learning_rate = 0.8           # Learning rate
max_steps = 99                # Max steps per episode
gamma = 0.97                  # Discounting rate

# Exploration parameters
epsilon = 0.5                 # Exploration rate
max_epsilon = 1.0             # Exploration probability at start
min_epsilon = 0.01            # Minimum exploration probability 
decay_rate = 0.01             # Exponential decay rate for exploration prob


# In[70]:


# List of rewards
rewards = []

# 2 For life or until learning is stopped
for episode in range(total_episodes):
    # Reset the environment
    state = env.reset()
    env.render()
    step = 0
    done = False
    total_rewards = 0
    print("****************************************************")
    print("EPISODE ", episode)

    
    for step in range(max_steps):
        # 3. Choose an action a in the current world state (s)
        ## First we randomize a number
        exp_exp_tradeoff = random.uniform(0, 1)
        
        ## If this number > greater than epsilon --> exploitation (taking the biggest Q value for this state)
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(qtable[state,:])

        # Else doing a random choice --> exploration
        else:
            action = env.action_space.sample()

        # Take the action (a) and observe the outcome state(s') and reward (r)
        new_state, reward, done, info = env.step(action)

        # Update Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
        # qtable[new_state,:] : all the actions we can take from new state
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])
        
        total_rewards += reward
        env.render()
        # Our new state is state
        state = new_state
        
        # If done (if we're dead) : finish episode
        if done == True:
            #if gamma < 0.97:
            #    gamma=gamma+0.015
            break
        
    episode += 1
    # Reduce epsilon (because we need less and less exploration)
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode) 
    rewards.append(total_rewards)

print ("Score over time: " +  str(sum(rewards)/total_episodes))
print(qtable)


# In[72]:


episodes = 1000
rewards = []
max_steps = 99

for episode in range(episodes):
    state = env.reset()  # Assuming you already have env created as above
    total_rewards = 0
    
    for step in range(max_steps):
        action = np.argmax(qtable[state,:])  # TODO your policy here!
        state, reward, done, info = env.step(action)
        total_rewards += reward
        if done:
            break
    rewards.append(total_rewards)        

print('Average score over time:', sum(rewards) / episodes)

