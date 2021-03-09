import tkinter as tk



def readlayout():
    with open('bigSearch.lay','r') as f:
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
            if layout[i][j]=='.' or layout[i][j]=='P':
                if layout[i][j]=='P':
                    init_position=(i,j)
                #print(i,j)
                pth_matrix[i].append(1)
            else:
                pth_matrix[i].append(0)

    #print(layout)
    print(pth_matrix)

def adjacency_list():
    mat_all=[]
    global ad_list
    ad_list=[]
    value=0
    for i in range(y_size):
        mat_all.append([])
        for j in range(x_size):
            mat_all[i].append(value)
            value+=1
    #print(mat_all)
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
        print(i,ad_list[i])    



def creategrid():
    x=0 
    y=0 
    w=20
    h=20
    for rows in layout:
        for columns in rows:
            z=_canvas.create_rectangle(x,y,w,h,fill="black",outline="red")
            if columns=='%':
                _canvas.itemconfig(z,fill="blue")
            elif columns=='P':
                _canvas.itemconfig(z,fill="yellow")
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
_canvas.pack()

creategrid()

pth_matrix()

adjacency_list()

#print(layout)




_root_window.mainloop()