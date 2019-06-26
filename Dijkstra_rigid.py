#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pygame
from sys import exit
import math
radius=input("Please input radius")
c=input("Please input clearance")
d=int(radius)+int(c)
c1=(6525/25) - d*math.sqrt((-41/25)**2+1)
c2=d*math.sqrt((-2/19)**2+1)+(1314/19)
c3=d*math.sqrt((38/7)**2+1)-(5830/7)
c4=-(6101/20)-d*math.sqrt((37/20)**2+1)
c5= d*math.sqrt((-38/23)**2+1) + (8530/23)
c61= (6551/10)- d*math.sqrt((-37/10)**2+1)
c62=  d*math.sqrt((-37/10)**2+1) +(6551/10)
def obstacle(x,y):
    k = 0
    if (x<(d/r))or (x>(250-d)/r) or (y<(d/r)) or (y>(150-d)/r):
        k=1
    if ((x-math.ceil(190/r))**2+(y-math.ceil(130/r))**2-(math.ceil((15+d)/r))**2)<0:
        k=1
    if ((2/19)*x + y - c2/r < 0) and (y+(41/25)*x -c1/r >0) and (y -( (15-d)/r)> 0) and (y<(-37/10)*x+c62/r):
        k=1
    if ((-38/7)*x +y - c3/r <0) and ((38/23)*x + y - c5/r < 0) and (y - ((15-d)/r )> 0) and ((-37/20)*x +y -c4/r > 0) and (y>(-37/10)*x+c61/r):
        k=1
    if (x-math.floor((50-d)/r) > 0) and (x - math.floor((100+d)/r) < 0) and (y - math.floor((67.5-d)/r) > 0) and (y - math.floor((112.5+d)/r) <0):
        k=1
    if ((x-math.ceil(140/r))/(math.ceil(15+d)/r))**2 + ((y - math.ceil(120/r))/(math.ceil(6+d)/r))**2 - 1 < 0:
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
cost=float('Inf')
cost_list.append(cost)
new_parent=[]
visited=[]
count=0
new_index=0
in_cost=0
children=[]
new_goal=[]
new_goal.append(goal)
def child(i):
    left(i)
    right(i)
    up(i)
    down(i)
    up_left(i)
    up_right(i)
    down_left(i)
    down_right(i)
def left(initial):
    current=initial[:]
    x=current[0]-1
    y=current[1]
    cost=1+in_cost
    current,cost=feasable(current,x,y,cost,initial)
    return current
def right(initial):
    current=initial[:]
    x=current[0]+1
    y=current[1]
    cost=1+in_cost
    current,cost=feasable(current,x,y,cost,initial)
    return current
def up(initial):
    current=initial[:]
    x=current[0]
    y=current[1]+1
    cost=1+in_cost
    current,cost=feasable(current,x,y,cost,initial)
def down(initial):
    current=initial[:]
    x=current[0]
    y=current[1]-1
    cost=1+in_cost
    current,cost=feasable(current,x,y,cost,initial)
def up_left(initial):
    current=initial[:]
    x=current[0]-1
    y=current[1]+1
    cost=1.42+in_cost
    current,cost=feasable(current,x,y,cost,initial)
def up_right(initial):
    current=initial[:]
    x=current[0]+1
    y=current[1]+1
    cost=1.42+in_cost
    current,cost=feasable(current,x,y,cost,initial)
def down_left(initial):
    current=initial[:]
    x=current[0]-1
    y=current[1]-1
    cost=1.42+in_cost
    current,cost=feasable(current,x,y,cost,initial)
def down_right(iniial):
    current=initial[:]
    x=current[0]+1
    y=current[1]-1
    cost=1.42+in_cost
    current,cost=feasable(current,x,y,cost,initial)
def feasable(current,x,y,cost,initial):
    c=obstacle(x,y)
    if x in range(0,int(250/r)+1) and y in range(0,int(150/r)+1)and c==0:
        current[0]=x
        current[1]=y
        cost=cost
        if current not in visited:
            if current in All_nodes:
                check=All_nodes.index(current)
                costcheck=cost_list[check]
                if costcheck<cost:
                    pass
                else:
                    All_nodes.pop(check)
                    cost_list.pop(check)
                    parent.pop(check)
                    All_nodes.append(current)
                    cost_list.append(cost)
                    parent.append(initial)
            else:
                All_nodes.append(current)
                cost_list.append(cost)
                parent.append(initial)
        else:
            pass
    return current,cost
print("-------Nodes are being explored------")
while goal not in visited:
        if All_nodes == []:
            print("Goal cant be reached")
            exit()
        child(All_nodes[new_index])
        visited.append(All_nodes[new_index])
        new_parent.append(parent[new_index])
        All_nodes.pop(new_index)
        cost_list.pop(new_index)
        parent.pop(new_index)
        count=count+1
        if cost_list != []:
            in_cost=min(cost_list)
            index=cost_list.index(in_cost)
            new_index=index

while True:
    if goal in visited:
        
        goal_index=visited.index(goal)
        goal=new_parent[goal_index]
        #print(goal)
        new_goal.append(goal)
        if goal == [float(x)/r,float(y)/r]:
            break
            
print("-----------The path is found--------")           
print("------The animation will begin------")

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

pygame.display.set_caption("Dijkstra Rigid")
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

    pygame.time.wait(1500)
    done = True
pygame.quit()


# In[ ]:




