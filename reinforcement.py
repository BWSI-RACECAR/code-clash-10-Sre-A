"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #10 - Reinforcement (reinforcement.py)


Author: Caroline Vincent

Difficulty Level: 8/10

Prompt: You are using a reinforcement learning algorithm to
play a multi-player game. At each time step, each player has P 
possible actions that they can take, denoted as 0 through P 
(Ex: a game where an agent can only move left, right, or stay
would have three possible actions: 0, 1, and 2). Your neural network 
receives and outputs a single integer that represents all 
possible combinations of actions taken by players (2-player Ex: 0=(0,0)).

You want to use a dictionary to map integer keys to tuples 
of actions, and tuples of actions to integer keys.
Write a function that takes in the number of players and the number of possible
actions as parameters and returns the dictionary. Assume that the number of possible
actions is the same for each player.

Example:
2 Players with 3 possible actions
Input: 2, 3
Output: {0: (0, 0), (0, 0): 0, 1: (1, 0), (1, 0): 1, 2: (2, 0), (2, 0): 2, 3: (0, 1), (0, 1): 3, 4: (1, 1), (1, 1): 4, 5: (2, 1),
(2, 1): 5, 6: (0, 2), (0, 2): 6, 7: (1, 2), (1, 2): 7, 8: (2, 2), (2, 2): 8}
'''

Test Cases:
2 Players with 3 possible actions
Input: 2, 3
Output: {0: (0, 0), (0, 0): 0, 1: (1, 0), (1, 0): 1, 2: (2, 0), (2, 0): 2, 3: (0, 1), (0, 1): 3, 4: (1, 1), (1, 1): 4, 5: (2, 1),
(2, 1): 5, 6: (0, 2), (0, 2): 6, 7: (1, 2), (1, 2): 7, 8: (2, 2), (2, 2): 8}

Input: 2, 2 Output: {0: (0, 0), (0, 0): 0, 1: (1, 0), (1, 0): 1, 2: (0, 1), (0, 1): 2, 3: (1, 1), (1, 1): 3}

Input: 3, 2 Output: {0: (0, 0, 0), (0, 0, 0): 0, 1: (1, 0, 0), (1, 0, 0): 1, 2: (0, 1, 0), (0, 1, 0): 2, 
3: (1, 1, 0), (1, 1, 0): 3, 4: (0, 0, 1), (0, 0, 1): 4, 5: (1, 0, 1), (1, 0, 1): 5, 6: (0, 1, 1), (0, 1, 1): 6, 7: (1, 1, 1), 
 (1, 1, 1): 7}
"""

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

class Solution:
    def create_action_dict(self, num_players, num_actions):
      if num_actions*num_players == 0:
        return {0: (), (): 0}
      enddict={}
      tuples = num_actions ** num_players
      for i in range(tuples):
        ibaction=numberToBase(i, num_actions)
        ibaction=ibaction[::-1]+(num_players-len(ibaction))*[0]
        ibaction=tuple(ibaction)
        enddict[i]=ibaction
        enddict[ibaction]=i
      return enddict
    
def main():
    input1 = input()
    input1= int(input1)
    input2= input()
    input2=int (input2)
    tc1 = Solution()
    ans = tc1.create_action_dict(input1, input2)
    print(ans)

if __name__ == "__main__":
    main()
