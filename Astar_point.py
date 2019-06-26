#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pygame
import math
from sys import exit
def obstacle(x,y):
    k = 0
    if ((x-math.ceil(190/r))**2+math.ceil(y-(130/r))**2-math.ceil(15/r)**2)<=0:
        k=1
    if (2*x + 19*y - 1314/r <= 0) and (41*x+ 25*y -6525/r >= 0) and (y - 15/r>= 0) and (37*x +10*y - 6551/r <= 0):
        k=1
    if (38*x- 7*y - 5830/r >= 0) and (38*x + 23*y - 8530/r <= 0) and (37*x -20*y -6101/r <= 0) and (37*x +10*y - 6551/r >= 0):
        k=1
    if (x-math.floor(50/r) >= 0) and (x - math.floor(100/r) <= 0) and (y - math.floor(67.5/r) >= 0) and (y - math.floor(112.5/r) <= 0):
        k=1
    if ((x-math.ceil(140/r))/math.ceil(15/r))**2 + ((y - math.ceil(120/r))/math.ceil(6/r))**2 - 1 <=0:
        k=1
    return k
def start(initial):
    c=obstacle(initial[0],initial[1])
    if c ==1 or initial[0]  not in range(0,251) or (initial[1] not in range(0,151)):
        print("Start point inside obstacle space or not in workspace space or not a good entry for resolution")
        exit()
    else:
        pass

def end(goal):
    c=obstacle(goal[0],goal[1])
    if c ==1 or goal[0] not in range(0,251) or goal[1] not in range(0,151):
        print("Goal point inside obstacle space or not in workspace space or not a good entry for resolution")
        exit()
    else:
        pass
def checkr(r):
    if (250%r)!=0  or(150%r)!=0:
        print("Please enter an achivable resolution")
        exit()
    else:
        pass
x=input("Please input x value for initial node")
y=input("Please input y value for initial node")
x1=input("Please input x value for goal node")
y1=input("Please input y value for goal node")
r=input("Please input an interger value for resolution")
r=int(r)
checkr(r)
initial = [float(x)/r,float(y)/r]
start(initial)
goal=[float(x1)/r,float(y1)/r]
end(goal)
goallist=[]
All_nodes=[]
All_nodes.append(initial)
parent=[]
parent.append(initial)
cost_list=[]
costh_list=[]
cost=float('Inf')
cost_list.append(cost)
costh=float('Inf')
costh_list.append(costh)
new_parent=[]
visited=[]
count=0
c=0
new_index=0
in_cost=0
children=[]
new_goal=[]
new_goal.append(goal)

def heuristic(c,g):
    #h=max(abs(c[0]-g[0]),abs(c[1]-g[1])) #dia
    #h=abs(c[0]-g[0])+abs(c[1]-g[1]) # man
    h=math.sqrt((c[0]-g[0])**2+(c[1]-g[1])**2) # euc
    #h=0
    return h

def child(i):
    right(i)
    left(i)
    up(i)
    down(i)
    up_right(i)
    down_right(i)
    up_left(i)
    down_left(i)
def left(initial):
    current=initial[:]
    x=current[0]-1
    y=current[1]
    h=heuristic([x,y],goal)
    #print(current,h)
    cost=1+in_cost
    costh=cost+h
    current,cost=feasable(current,x,y,cost,costh,initial)
    return current
def right(initial):
    current=initial[:]
    x=current[0]+1
    y=current[1]
    h=heuristic([x,y],goal)
    #print(current,h)
    cost=1+in_cost
    costh=cost+h
    current,cost=feasable(current,x,y,cost,costh,initial)
    return current
def up(initial):
    current=initial[:]
    x=current[0]
    y=current[1]+1
    h=heuristic([x,y],goal)
    #print(current,h)
    cost=1+in_cost
    costh=cost+h
    current,cost=feasable(current,x,y,cost,costh,initial)
def down(initial):
    current=initial[:]
    x=current[0]
    y=current[1]-1
    h=heuristic([x,y],goal)
    #print(current,h)
    cost=1+in_cost
    costh=cost+h
    current,cost=feasable(current,x,y,cost,costh,initial)
def up_left(initial):
    current=initial[:]
    x=current[0]-1
    y=current[1]+1
    h=heuristic([x,y],goal)
    #print(current,h)
    cost=math.sqrt(2)+in_cost
    costh=cost+h
    current,cost=feasable(current,x,y,cost,costh,initial)
def up_right(initial):
    current=initial[:]
    x=current[0]+1
    y=current[1]+1
    h=heuristic([x,y],goal)
    #print(current,h)
    cost=math.sqrt(2)+in_cost
    costh=cost+h
    current,cost=feasable(current,x,y,cost,costh,initial)
def down_left(initial):
    current=initial[:]
    x=current[0]-1
    y=current[1]-1
    h=heuristic([x,y],goal)
    #print(current,h)
    cost=math.sqrt(2)+in_cost
    costh=cost+h
    current,cost=feasable(current,x,y,cost,costh,initial)
def down_right(iniial):
    current=initial[:]
    x=current[0]+1
    y=current[1]-1
    h=heuristic([x,y],goal)
    #print(current,h)
    cost=math.sqrt(2)+in_cost
    costh=cost+h
    current,cost=feasable(current,x,y,cost,costh,initial)
def feasable(current,x,y,cost,costh,initial):
    c=obstacle(x,y)
    #print(c)
    if x in range(0,int(250/r)+1) and y in range(0,int(150/r)+1) and c==0:
        current[0]=x
        current[1]=y
        cost=cost
        if current not in visited:
            if current in All_nodes:
                check=All_nodes.index(current)
                costcheck=costh_list[check]
                if costcheck<=costh:
                    pass
                else:
                    All_nodes.pop(check)
                    cost_list.pop(check)
                    costh_list.pop(check)
                    parent.pop(check)
                    All_nodes.append(current)
                    cost_list.append(cost)
                    costh_list.append(costh)
                    parent.append(initial)
            else:
                All_nodes.append(current)
                cost_list.append(cost)
                costh_list.append(costh)
                parent.append(initial)
        else:
            pass
    return current,cost
print("-------Nodes are being explored------")
while goal not in visited:
        child(All_nodes[new_index])
        visited.append(All_nodes[new_index])
        new_parent.append(parent[new_index])
        All_nodes.pop(new_index)
        cost_list.pop(new_index)
        costh_list.pop(new_index)
        parent.pop(new_index)
        count=count+1
        if costh_list != []:
            in_costh=min(costh_list)
            index=costh_list.index(in_costh)
            in_cost=cost_list[index]
            new_index=index


while True:
    if goal in visited:
        goal_index=visited.index(goal)
        goal=new_parent[goal_index]
        new_goal.append(goal)
        if goal == initial:
            break
print("-----------The path is found---------")           
print("------The animation will begin--------")

obs=[]            
for i in range(0,251):
    for j in range(0,151):
        c=obstacle(i,j)
        if c==1:
            obs.append([i,j])

k=2
obs1=np.array(obs)
obs=obs1*k*r
my_list = np.array(visited)
visited=my_list*k*r
my_list1 = np.array(new_goal)
new_goal=my_list1*k*r
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
blue=[0,0,255]
green = [0,255,0]
 
SIZE = [250*k+r+r, 150*k+r+r]

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("A*Star Point Robot")
clock = pygame.time.Clock()
done = False
while not done:
 
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True 
 
    
    screen.fill(BLACK)
    for i in obs:
        pygame.draw.rect(screen, WHITE, [i[0],150*k-i[1],r*k,r*k])
    pygame.display.flip()
    clock.tick(20)
    for i in visited:
        pygame.time.wait(1)
        pygame.draw.rect(screen, green, [i[0],150*k-i[1],r*k,r*k])
        pygame.display.flip()
    for j in new_goal[::-1]:
        pygame.time.wait(1)
        pygame.draw.rect(screen, blue, [j[0], 150*k-j[1], r*k,r*k])
        pygame.display.flip()    
    pygame.display.flip()

    pygame.time.wait(15000)
    done = True
    print("-----The animation has ended---------")

pygame.quit()


# In[ ]:




