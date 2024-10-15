#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import random

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        ots=0
        if self.results[-1] == 1:
            ots=0       
        elif self.results[-1] == 0.5:
            ots=1
        else:  
            ots=2
        if ots==0:
            if (len(self.results)-self.points)/(len(self.results))>=(6/11):
                return 0
            return 2
        
        elif ots==1:
            return 0
        
        else :
            return 1
        
#         if a1>=max(a2,a3):
#             return 0
#         elif a2>max(a1,a3):
#             return 1
#         elif a3>max(a1,a2):
#             return 2

        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        Returns:
            None
        """
        self.past_play_styles=np.append(self.past_play_styles,own_style)
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points+=result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """ 
        self.past_play_styles=np.append(self.past_play_styles,(own_style))
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    Returns:
        None
    """
    a=bob.play_move()
    b=alice.play_move()
    Deci=random.choices([-1,0,1],weights=[payoff_matrix[b][a][0],payoff_matrix[b][a][1],payoff_matrix[b][a][2]],k=1)[0]
    if Deci==-1:
        alice.observe_result(b,a,1)
        bob.observe_result(a,b,0)
    elif Deci==1:
       alice.observe_result(b,a,0)
       bob.observe_result(a,b,1)
    else:
        alice.observe_result(b,a,0.5)
        bob.observe_result(a,b,0.5)
    
    pass
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    Returns:
        None
    """
    alice=Alice()
    bob=Bob()
    payoff_matrix=[[[1/2,0,1/2],[7/10,0,3/10],[5/11,0,6/11]],
         [[3/10,0,7,10],[1/3,1/3,1/3],[3/10,1/2,1/5]],
         [[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    for i in range(0,100000):
        simulate_round(alice,bob,payoff_matrix)
        payoff_matrix[0][0][0]=bob.points/(alice.points+bob.points)
        payoff_matrix[0][0][2]=alice.points/(alice.points+bob.points)
#     print(alice.points,bob.points)
#     print(alice.results,bob.results,sep="\n")
    pass
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10^5)


# In[ ]:





# In[ ]:





# In[62]:


import numpy as np
import random

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self,ots,pnt):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        a1=pnt[0][ots][0]
        a2=pnt[1][ots][0]
        a3=pnt[2][ots][0]
#         print(a1,a2,a3,end=" ")
        if a1>=max(a2,a3):
            return 0
        elif a2>max(a1,a3):
            return 1
        elif a3>max(a1,a2):
            return 2

        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        Returns:
            None
        """
        self.past_play_styles=np.append(self.past_play_styles,own_style)
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points+=result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """ 
        self.past_play_styles=np.append(self.past_play_styles,(own_style))
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    Returns:
        None
    """
    a=bob.play_move()
    b=alice.play_move(a,payoff_matrix)
    Deci=random.choices([-1,0,1],weights=[payoff_matrix[b][a][0],payoff_matrix[b][a][1],payoff_matrix[b][a][2]],k=1)[0]
#     print(b,a,payoff_matrix[b][a][0],payoff_matrix[b][a][1],payoff_matrix[b][a][2],Deci)
    if Deci==-1:
        alice.observe_result(b,a,1)
        bob.observe_result(a,b,0)
    elif Deci==1:
       alice.observe_result(b,a,0)
       bob.observe_result(a,b,1)
    else:
        alice.observe_result(b,a,0.5)
        bob.observe_result(a,b,0.5)
    pass
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    Returns:
        None
    """
    alice=Alice()
    bob=Bob()
    pnt=[[[1/2,0,1/2],[7/10,0,3/10],[5/11,0,6/11]],
         [[3/10,0,7,10],[1/3,1/3,1/3],[3/10,1/2,1/5]],
         [[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    for i in range(0,100000):
        simulate_round(alice,bob,pnt)
        pnt[0][0][0]=bob.points/(alice.points+bob.points)
        pnt[0][0][2]=alice.points/(alice.points+bob.points)
    print(alice.points,bob.points)
    print(alice.results,bob.results,sep="\n")
    print(pnt)
    pass
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10^5)


# In[ ]:


# 2b


# In[6]:


import numpy as np
import random

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        
        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        Returns:
            None
        """
        self.past_play_styles=np.append(self.past_play_styles,own_style)
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points+=result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """ 
        self.past_play_styles=np.append(self.past_play_styles,(own_style))
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    Returns:
        None
    """
    a=bob.play_move()
    b=alice.play_move(a,payoff_matrix)
    Deci=random.choices([-1,0,1],weights=[payoff_matrix[b][a][0],payoff_matrix[b][a][1],payoff_matrix[b][a][2]],k=1)[0]
    if Deci==-1:
        alice.observe_result(b,a,1)
        bob.observe_result(a,b,0)
    elif Deci==1:
       alice.observe_result(b,a,0)
       bob.observe_result(a,b,1)
    else:
        alice.observe_result(b,a,0.5)
        bob.observe_result(a,b,0.5)
    
    pass
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    Returns:
        None
    """
    alice=Alice()
    bob=Bob()
    pnt=[[[1/2,0,1/2],[7/10,0,3/10],[5/11,0,6/11]],
         [[3/10,0,7,10],[1/3,1/3,1/3],[3/10,1/2,1/5]],
         [[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    for i in range(0,100000):
        simulate_round(alice,bob,pnt)
        pnt[0][0][0]=bob.points/(alice.points+bob.points)
        pnt[0][0][2]=alice.points/(alice.points+bob.points)
    print(alice.points,bob.points)
    print(alice.results,bob.results,sep="\n")
    print(pnt)
    pass
    
    
 



# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10^5)


# In[5]:


import numpy as np
import random

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self,ots,pnt):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1]==1:
            return 1
        elif self.results[-1]==0.5:
            return 0
        else:
            return 2
        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        Returns:
            None
        """
        self.past_play_styles=np.append(self.past_play_styles,own_style)
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points+=result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1]==1:
            return 2
        elif self.results[-1]==0.5:
            return 1
        else:
            return 0
        pass
        
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """ 
        self.past_play_styles=np.append(self.past_play_styles,(own_style))
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    Returns:
        None
    """
    a=bob.play_move()
    b=alice.play_move(a,payoff_matrix)
    Deci=random.choices([-1,0,1],weights=[payoff_matrix[b][a][0],payoff_matrix[b][a][1],payoff_matrix[b][a][2]],k=1)[0]
    if Deci==-1:
        alice.observe_result(b,a,1)
        bob.observe_result(a,b,0)
    elif Deci==1:
       alice.observe_result(b,a,0)
       bob.observe_result(a,b,1)
    else:
        alice.observe_result(b,a,0.5)
        bob.observe_result(a,b,0.5)
    
    pass
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    Returns:
        None
    """
    alice=Alice()
    bob=Bob()
    pnt=[[[1/2,0,1/2],[7/10,0,3/10],[5/11,0,6/11]],
         [[3/10,0,7,10],[1/3,1/3,1/3],[3/10,1/2,1/5]],
         [[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    for i in range(0,100000):
        simulate_round(alice,bob,pnt)
        pnt[0][0][0]=bob.points/(alice.points+bob.points)
        pnt[0][0][2]=alice.points/(alice.points+bob.points)
    print(alice.points,bob.points)
    print(alice.results,bob.results,sep="\n")
    print(pnt)
    pass
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10^5)


# In[ ]:


# 2c


# In[18]:


import numpy as np
import random

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        ots=0
        if self.results[-1] == 1:
            ots=0       
        elif self.results[-1] == 0.5:
            ots=1
        else:  
            ots=2
        if ots==0:
            if (len(self.results)-self.points)/(len(self.results))>=(6/11):
                return 0
            return 2
        
        elif ots==1:
            return 0
        
        else :
            return 1
#         a1=0
#         a2=0
#         a3=0
#         if ots==0:
#             if pnt[0][0][0]>=pnt[2][0][0]:
#                 return 0
#             return 2
        
#         elif ots==1:
#             return 0
        
#         else :
#             return 1
        
#         if a1>=max(a2,a3):
#             return 0
#         elif a2>max(a1,a3):
#             return 1
#         elif a3>max(a1,a2):
#             return 2

        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        Returns:
            None
        """
        self.past_play_styles=np.append(self.past_play_styles,own_style)
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points+=result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """ 
        self.past_play_styles=np.append(self.past_play_styles,(own_style))
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    Returns:
        None
    """
    a=bob.play_move()
    b=alice.play_move()
    Deci=random.choices([-1,0,1],weights=[payoff_matrix[b][a][0],payoff_matrix[b][a][1],payoff_matrix[b][a][2]],k=1)[0]
    if Deci==-1:
        alice.observe_result(b,a,1)
        bob.observe_result(a,b,0)
    elif Deci==1:
       alice.observe_result(b,a,0)
       bob.observe_result(a,b,1)
    else:
        alice.observe_result(b,a,0.5)
        bob.observe_result(a,b,0.5)
    
    pass
    
    

def monte_carlo(Tau):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    Returns:
        None
    """
    alice=Alice()
    bob=Bob()
    potr=[]
    t=[1]
    pnt=[[[1/2,0,1/2],[7/10,0,3/10],[5/11,0,6/11]],
         [[3/10,0,7,10],[1/3,1/3,1/3],[3/10,1/2,1/5]],
         [[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    j=2
    for i in range(0,100000):
        x=alice.points
        simulate_round(alice,bob,pnt)
        pnt[0][0][0]=bob.points/(alice.points+bob.points)
        pnt[0][0][2]=alice.points/(alice.points+bob.points)
        y=alice.points
        if y-x==1:
            t[0]=t[0]+1
        j=j+1
        if t[0]==Tau:
            alice=Alice()
            bob=Bob()
            pnt[0][0][0]=1/2
            pnt[0][0][2]=1/2
            potr.append(j)
            print(i,Tau,t[0],j)
            t[0]=1
            j=2
    calc=0
    for i in potr:
        calc=calc+i
        
    print(calc/len(potr))
    return (calc/len(potr))
    pass
    
# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(99)
#     monte_carlo(num_rounds=10^5)


# In[ ]:


# doing 3a


# In[14]:


import numpy as np
import random
class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        

        """
        a1=((len(self.results)-self.points)/(len(self.results)))+(7/10)+(5/11)
        a3=1.49
        if a1>=a3:
            return 0
        return 2
        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        Returns:
            None
        """
        self.past_play_styles=np.append(self.past_play_styles,own_style)
        self.results=np.append(self.results,result)
        self.opp_play_styles=np.append(self.opp_play_styles,opp_style)
        self.points+=result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = np.random.choice([0, 1, 2])
        return move
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles=np.append(self.past_play_styles,(own_style))
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    a=bob.play_move()
    b=alice.play_move()
    Deci=random.choices([-1,0,1],weights=[payoff_matrix[b][a][0],payoff_matrix[b][a][1],payoff_matrix[b][a][2]],k=1)[0]
    if Deci==-1:
        alice.observe_result(b,a,1)
        bob.observe_result(a,b,0)
    elif Deci==1:
       alice.observe_result(b,a,0)
       bob.observe_result(a,b,1)
    else:
        alice.observe_result(b,a,0.5)
        bob.observe_result(a,b,0.5)
    pass
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    alice=Alice()
    bob=Bob()
    payoff_matrix=[[[1/2,0,1/2],[7/10,0,3/10],[5/11,0,6/11]],
                   [[3/10,0,7/10],[1/3,1/3,1/3],[3/10,1/2,1/5]],
                   [[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    for i in range(0,100000):
        simulate_round(alice,bob,payoff_matrix)
        payoff_matrix[0][0][0]=bob.points/(alice.points+bob.points)
        payoff_matrix[0][0][2]=alice.points/(alice.points+bob.points)
    print(alice.points,bob.points)
    print(alice.past_play_styles)
    print(bob.past_play_styles)
    pass
  
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10^5)


# In[8]:


# 3b


# In[10]:


import numpy as np
import random
class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self,pnt):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        

        """
        if len(self.results)%3==0:
            return 0
        return 2
#         a1=pnt[0][0][0]+(7/10)+(5/11)
#         a3=1.49
#         if a1>=a3:
#             return 0
#         return 2
        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        Returns:
            None
        """
        self.past_play_styles=np.append(self.past_play_styles,own_style)
        self.results=np.append(self.results,result)
        self.opp_play_styles=np.append(self.opp_play_styles,opp_style)
        self.points+=result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = np.random.choice([0, 1, 2])
        return move
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles=np.append(self.past_play_styles,(own_style))
        self.results=np.append(self.results,(result))
        self.opp_play_styles=np.append(self.opp_play_styles,(opp_style))
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    a=bob.play_move()
    b=alice.play_move(payoff_matrix)
    Deci=random.choices([-1,0,1],weights=[payoff_matrix[b][a][0],payoff_matrix[b][a][1],payoff_matrix[b][a][2]],k=1)[0]
    if Deci==-1:
        alice.observe_result(b,a,1)
        bob.observe_result(a,b,0)
    elif Deci==1:
       alice.observe_result(b,a,0)
       bob.observe_result(a,b,1)
    else:
        alice.observe_result(b,a,0.5)
        bob.observe_result(a,b,0.5)
    pass
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    alice=Alice()
    bob=Bob()
    payoff_matrix=[[[1/2,0,1/2],[7/10,0,3/10],[5/11,0,6/11]],
                   [[3/10,0,7/10],[1/3,1/3,1/3],[3/10,1/2,1/5]],
                   [[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    for i in range(0,10000):
        simulate_round(alice,bob,payoff_matrix)
        payoff_matrix[0][0][0]=bob.points/(alice.points+bob.points)
        payoff_matrix[0][0][2]=alice.points/(alice.points+bob.points)
    print(alice.points,bob.points)
    print(alice.past_play_styles)
    print(bob.past_play_styles)
    pass
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10^5)


# In[ ]:




