
import tkinter as tk
from tkinter import messagebox 
from collections import deque
import time 
import os
import sys

full_path = os.path.realpath(__file__)

pathx, filename = os.path.split(full_path)



def readlayout():
    with open(pathx+'\\openClassic.lay','r') as f:
        conatents=f.readlines()
        global layout
        global x_size
        global y_size
        layout=[[n for n in lines if n != '\n'] for lines in conatents ]
        y_size=len(layout)
        x_size=len(layout[0])

def pth_matrix():
    global pth_matrix
    global init_position
    init_position=()
    pth_matrix=[]

    #print(pth_matrix)
    for i in range(y_size):
        pth_matrix.append([])
        for j in range(x_size):
            if (layout[i][j] in (' ','.','P','G','o')):  ###### ADD symobls to be considered as path
                if layout[i][j]=='P':
                    init_position=(i,j)
                #print(i,j)
                pth_matrix[i].append(1)

            else:
                pth_matrix[i].append(0)

    #print(layout)
    #print(pth_matrix)




def on_key_press(e):
    new_direction = e.keysym
    print("Executed")
    print(new_direction)

def adjacency_list():
    global mat_all
    mat_all=[]
    global ad_list
    # global start_value
    # start_value = 0
    ad_list=[]
    value=0
    for i in range(y_size):
        mat_all.append([])
        for j in range(x_size):
            mat_all[i].append(value)
            value+=1
    #print(mat_all)
    a,b=init_position
    #start_value=mat_all[a][b]
    #print(start_value)
    for i in range(value):
        ad_list.append([])
    for i in range(y_size):
        for j in range(x_size):
            if pth_matrix[i][j]==1:
                if pth_matrix[i-1][j]==1:
                    ind_1=mat_all[i][j]
                    ind_2=mat_all[i-1][j]
                    ad_list[ind_1].append(ind_2)
                if pth_matrix[i][j+1]==1:
                    ind_1=mat_all[i][j]
                    ind_2=mat_all[i][j+1]
                    ad_list[ind_1].append(ind_2)

                if pth_matrix[i+1][j]==1:
                    ind_1=mat_all[i][j]
                    ind_2=mat_all[i+1][j]
                    ad_list[ind_1].append(ind_2)

                if pth_matrix[i][j-1]==1:
                    ind_1=mat_all[i][j]
                    ind_2=mat_all[i][j-1]
                    ad_list[ind_1].append(ind_2)
    for i in range(value):
        #print(i,ad_list[i])
        pass    

def setOutput(i,j):
    global end_value
    if pth_matrix[i][j]==0:
        messagebox.showinfo("Position Doesnt exist in path", "Exiting" )
        exit()
    else:
        end_value=mat_all[i][j]

def rightClicked(event):
    global start_value
    item=_canvas.find_closest(event.x, event.y)
    start_value,=item
    start_value-=1
    for i in range(y_size):
        for j in range(x_size):
            if mat_all[i][j]==start_value:
                _canvas.itemconfig(rectangles[i][j],fill="Red")
                _root_window.update
    


# def bfs():

#     #end_value=23
#     queue=deque()
#     visited=[False for i in range(len(ad_list))]
#     prev=[0 for i in range(len(ad_list))]
#     #print(prev)
#     queue.appendleft(start_value)
#     visited[start_value]=True
#     # a,b=index_2d(mat_all,start_value)
#     # _canvas.itemconfig(rectangles[a][b],fill="green2")
#     # time.sleep(0.02)
#     _root_window.update()

#     #print(i,j)

#     #print(prev)

#     while len(queue) != 0:
#         node=queue.pop()
#         a,b=index_2d(mat_all,node)
#         _canvas.itemconfig(rectangles[a][b],fill="coral3")
#         time.sleep(0.02)
#         _root_window.update()

#         if node==end_value:
#             return prev
#         neighbours = ad_list[node]
#         for i in neighbours:
#             if visited[i]==False:
#                 queue.appendleft(i)
#                 visited[i]=True
#                 a,b=index_2d(mat_all,i)
#                 _canvas.itemconfig(rectangles[a][b],fill="green2")
#                 #print(rectangles[0][0])
#                 time.sleep(0.02)
#                 _root_window.update()
#                 prev[i]=node

#     return prev

def pathing(prev):
    #print(prev)
    path=[]
    path.append(end_value)
    for i in range(len(prev)):
        path.append(prev[int(path[i])])
    
    path.reverse()
    path=[n for n in path if n!= 0]
    
    for value in path:
        a,b=index_2d(mat_all,value)
        _canvas.itemconfig(rectangles[a][b],fill="light yellow")
        time.sleep(0.02)
        _root_window.update()



def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

    pass

def pause(flag):
    while flag == 0:
        print("Looped")

def clicked(event):

    #print(event)
    #print("clicked")
    item=_canvas.find_closest(event.x, event.y)
    value,=item
    for i in range(y_size):
        for j in range(x_size):
            if mat_all[i][j]==(value-1):
                _canvas.itemconfig(rectangles[i][j],fill="purple")
                _root_window.update
                setOutput(i,j)
                # prev=bfs()
                # pathing(prev)
                # _canvas.delete(all)
                #print(full_path)
                #os.execv(__file__, sys.argv)
                



def creategrid():

    global rectangles
    rectangles=[]
    #for i in range(len(layout)):

    x=0 
    y=0 
    w=20
    h=20
    for i in range(len(layout)):
        rectangles.append([])
        for j in range(len(layout[0])):
            rectangles[i].append(_canvas.create_rectangle(x,y,w,h,fill="black",outline="black",tags="rectangle_click"))
            if layout[i][j]=='%':
                _canvas.itemconfig(rectangles[i][j],fill="blue")
            # elif layout[i][j]=='P':
            #     _canvas.itemconfig(rectangles[i][j],fill="yellow")
            x=x+20
            w=w+20
        x=0
        w=20
        y=y+20
        h=h+20

readlayout()

_root_window=tk.Tk()
_root_window.title('Pacman path finder')
_root_window.config(bg="black")
_root_window.resizable(0,0)

_canvas=tk.Canvas(_root_window,width=x_size*20,height=y_size*20)
_canvas.tag_bind("rectangle_click", "<Key>" ,on_key_press)
_canvas.tag_bind("rectangle_click", "<Button-3>" ,rightClicked)
#_canvas.tag_bind("rectangle_click", "<Button-3>" ,rightClicked)
_canvas.pack()


creategrid()

pth_matrix()

adjacency_list()

#setOutput(1,2)
#pause(0)
#prev=bfs()
#print(prev)

#pathing(prev)
#print(layout)




_root_window.mainloop()