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

class Solution:
    def create_action_dict(self, num_players, num_actions):
        # type num: two integer values
        # return type: int dictionary
        
        action_dict = {}
        index = 0
        
        # Generate the mapping from integer keys to tuples of actions
        for i in range(num_actions):
            for j in range(num_actions):
                actions_tuple = tuple([i] + [0] * (num_players - 1))  # Create a tuple with the first action as 'i' and the rest as 0
                actions_tuple = actions_tuple[:num_players - 1] + (j,)  # Replace the last element with 'j'
                action_dict[index] = actions_tuple
                index += 1
        
        # Generate the mapping from tuples of actions to integer keys
        for i, actions_tuple in action_dict.items():
            action_dict[actions_tuple] = i
        
        return action_dict

def main():
    input1 = int(input("Enter the number of players: "))
    input2 = int(input("Enter the number of possible actions: "))
    
    tc1 = Solution()
    ans = tc1.create_action_dict(input1, input2)
    print(ans)

if __name__ == "__main__":
    main()
pass
    
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



