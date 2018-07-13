
# coding: utf-8

# In[1]:


import gym
import numpy as np
import random
from collections import defaultdict


# In[2]:


# https://github.com/openai/gym/blob/master/gym/envs/toy_text/blackjack.py
env = gym.make('Blackjack-v0')
print(env.observation_space)
print(env.action_space)


# In[3]:


qtable = np.zeros((32, 11, 2, 2))
# print(qtable)
qtable_dict = defaultdict(lambda: np.zeros(2))  # array of actions

def qtable_func(state):
    # TODO: magic! This is a non-functional example
    return np.array([0.5, 0])


# In[42]:


total_episodes = 100000       # Total episodes
learning_rate = 0.1           # Learning rate
max_steps = 10                # Max steps per episode
gamma = 0.01                  # Discounting rate

# Exploration parameters
epsilon = 0.3                 # Exploration rate
max_epsilon = 1.0             # Exploration probability at start
min_epsilon = 0.1            # Minimum exploration probability 
decay_rate = 0.1             # Exponential decay rate for exploration prob


# In[47]:


# List of rewards
rewards = []

# Learn through the episodes
for episode in range(total_episodes):
    # Reset the environment
    state = env.reset()
    #print('this is the state type',type(state))
    #print('this is the state',state)
    done = False
    total_rewards = 0
    
    for step in range(max_steps):
        player_total = state[0]
        dealer_showing = state[1]
        has_ace = 1 if state[2] else 0
        
        # Action selection - decide if we explore or exploit
        if random.uniform(0, 1) < epsilon:
            # Time to explore!
            action = env.action_space.sample()
            #print('taking random action', action)
        else:
            # Exploit based on best available rewards
            # action = np.argmax(qtable_dict[state])
            action = np.argmax(qtable[player_total,
                                      dealer_showing,
                                      has_ace, :])
            #print('taking best action', action)
        
        # Take the action, observe the outcome and reward
        new_state, reward, done, info = env.step(action)
        #print('new_state',new_state)
        #print('reward',reward)
        #print('done',done)
        #print('info',info)
        
        # Update Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
        # qtable[new_state,:] : all the actions we can take from new state
        '''
        qtable[player_total,
               dealer_showing,
               has_ace,
               action] = (qtable[player_total,
                                 dealer_showing,
                                 has_ace,
                                 action] +
                          learning_rate *
                          (reward + gamma *
                           np.max(qtable[new_state[0], new_state[1], 1 if new_state[2] else 0, :]) -
                           qtable[player_total, dealer_showing, has_ace, action]))
        '''
        qtable[player_total,
               dealer_showing,
               has_ace,
               action] = (qtable[player_total,
                                 dealer_showing,
                                 has_ace,
                                 action] +
                          learning_rate *
                          (reward + gamma *
                           np.max(qtable[new_state[0], new_state[1], 1 if new_state[2] else 0, :]) -
                           qtable[player_total, dealer_showing, has_ace, action]))        
        '''
        # Update the qtable with new expected rewards
        qtable_dict[state][action] += (learning_rate *(reward + gamma *(np.max(qtable_dict[new_state])) -qtable_dict[state][action]))
        '''
        #print('qtable',qtable)
        total_rewards += reward
        state = new_state
        if done:
            if gamma < 0.02:
                gamma=gamma+0.0000002
            break
    
    # Reduce epsilon (explore less)
    epsilon = (min_epsilon +
               (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode))
    rewards.append(total_rewards)

print('Score over time:', sum(rewards) / total_episodes)


# In[27]:


qtable[player_total,dealer_showing,has_ace, :]


# In[13]:


# Blackjack is hard (even optimum loses money)
# How do we compare to random?

# List of rewards
rewards = []

# Learn through the episodes
for episode in range(total_episodes):
    # Reset the environment
    state = env.reset()
    done = False
    total_rewards = 0
    
    for step in range(max_steps):
        # Action selection - always random
        action = env.action_space.sample()
        
        # Take the action, observe the outcome and reward
        new_state, reward, done, info = env.step(action)
              
        total_rewards += reward
        state = new_state
        if done:
            break
    
    rewards.append(total_rewards)

print('Score over time:', sum(rewards) / total_episodes)


# In[13]:


# So we're about twice as good (or half as bad) as random
# Let's play Blackjack!
def print_state(state):
    print('---')
    print('Player sum:', state[0])
    print('Dealer showing:', state[1])
    print('Player has usable ace:', state[2])

rewards = 0
hands = 5

for hand in range(hands):
    state = env.reset()
    print('****************************************************')
    print('HAND', hand)
    
    for step in range(max_steps):
        print_state(state)
        # Take the action with max expected future reward
        action = np.argmax(qtable_dict[state])
        
        print('Hit me!' if action else 'Stay.')
        
        state, reward, done, info = env.step(action)
        
        if done:
            rewards += reward
            print('HAND DONE')
            if reward == 1.0:
                print('You win!')
            elif reward == 0.0:
                print('Draw.')
            else:
                print('You lose!')
            break

print('****************************************************')
print('ALL HANDS COMPLETE')
print('Total score:', rewards)
print('Average per hand:', rewards / hands)
env.close()


# In[14]:


qtable_dict


# In[20]:


print(env.reset())


# In[9]:


a = np.arange(6).reshape(2,3)
print(a)
print('argmax of a',np.argmax(a, axis=1))

#np.argmax(a, axis=0)

