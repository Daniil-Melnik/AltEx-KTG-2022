import random
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
import shutil
from tkinter.ttk import Checkbutton
import math

def Get_data():
    val_map = {}
    n=int(txtn.get()) 
    us =selected.get()
    print(us)
    if (us==1):
        p=float(txtp.get())
        txtс.delete(0, END)
        txtс.insert(0,'c')
    elif (us==2):
        c=float(txtс.get())
        p=c*(math.log(n)/n)
        txtp.delete(first=0,last=END)
        txtp.insert(0, str(p))
    elif (us==3):
        c=float(txtс.get())
        p=c/n
        txtp.delete(first=0,last=END)
        txtp.insert(0, str(p))
    elif (us==4):
        w=n/math.log(n)
        p=w/n
        txtp.delete(first=0,last=END)
        txtp.insert(0, str(p))
    elif (us==5):
        a=1/n
        p=a/n
        txtp.delete(first=0,last=END)
        txtp.insert(0, str(p))
    elif (us==6):
        p=1/(n**3)
        txtp.delete(first=0,last=END)
        txtp.insert(0, str(p))
    elif (us==7):
        p=n*math.log(n)/n
        txtp.delete(first=0,last=END)
        txtp.insert(0, str(p))
    elif (us==8):
        p=float(txtp.get())
        txtс.delete(0, END)
        txtс.insert(0,'c')
    f = open("data.txt", "w")
    f.write(str(n)+'\n')
    f.write(str(p)+'\n')
    

def Show_Graph():
    G= nx.Graph()
    edges = nx.read_edgelist('edges.txt')
    nodes = nx.read_adjlist("nodes.txt")
    G.add_edges_from(edges.edges())
    G.add_nodes_from(nodes)

    us =selected.get()
    val_map = {}
    
    if (us==4):
        all_cliques= nx.enumerate_all_cliques(G)
        triad_cliques=[x for x in all_cliques if len(x)==3 ]
        if (len(triad_cliques)!=0):
            for v in triad_cliques[0]:
                val_map[v]=0.1
            
    all_cliques= nx.enumerate_all_cliques(G)
    triad_cliques=[x for x in all_cliques if len(x)==3 ]
    if (len(triad_cliques)!=0):
        lbl3.configure(text='+', foreground='#008000')
    else:
        lbl3.configure(text='-', foreground='#ff0000')

    if (us==8):
        for v in (max(nx.connected_components(G))):
            val_map[v]=0.1 

    values = [val_map.get(node, 0.25) for node in G.nodes()]
    
    plt.clf()
    if (nx.check_planarity(G, counterexample=False)[0]==True):
        nx.draw_planar(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
        lbl2.configure(text="+", foreground='#008000')
    else:
        nx.draw(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
        lbl2.configure(text="-", foreground='#ff0000')

    if (nx.is_connected(G)):
        lbl1.configure(text="+", foreground='#008000')
    else:
        lbl1.configure(text="-", foreground='#ff0000')
    print(max(nx.connected_components(G)))
    plt.axis('on')
    plt.savefig("st.png")
    
        

    #nx.draw(G,pos=nx.spring_layout(G) ,with_labels = False)
    plt.show()
    plt.clf()

root = Tk()
colors={"bgr":'#2F4F4F', 'bfr': '#696969', 'bfr1' : '#808080', 'bent':'#C0C0C0'}
root.title("Модель случайного графа Эрдёша-Реньи")
root["bg"] = colors['bgr']
root.geometry('750x500')

selected = IntVar()

#frame1 = LabelFrame(text="изображение графа", width=640, height=480, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
frame2 = LabelFrame(text="способы работы", width=400, height=280, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
frame3 = LabelFrame(text="ввод значений", width=400, height=180, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
frame4 = LabelFrame(text="свойства графа", width=250, height=180, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')

#frame1.place(x=5, y=5)
frame4.place(x=420, y=5)
frame3.place(x=5, y=300)
frame2.place(x=5, y=5)

frame31 = LabelFrame(frame3, width=350, height=30, background=colors['bfr'])
frame32 = LabelFrame(frame3, width=350, height=30, background=colors['bfr'])
frame33 = LabelFrame(frame3, width=350, height=30, background=colors['bfr'])

frame41 = LabelFrame(frame4, width=220, height=30, background=colors['bfr'])
frame42 = LabelFrame(frame4, width=220, height=30, background=colors['bfr'])
frame43 = LabelFrame(frame4, width=220, height=30, background=colors['bfr'])

frame41.place(x=10, y=10)
frame42.place(x=10, y=60)
frame43.place(x=10, y=110)

frame31.place(x=10, y=10)
frame32.place(x=10, y=60)
frame33.place(x=10, y=110)

#Количество вершин
lbl = Label(frame31, text="колво вершин:", font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff')
lbl.place(x=0, y=0)
txtn = Entry(frame31, width=40, background=colors['bent'])
txtn.place(x=100, y=2)

#вероятность p
txtp = Entry(frame32,width=40, background=colors['bent'])
txtp.place(x=100, y=2)
lblp = Label(frame32, text="вероятность:", font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff')
lblp.place(x=0, y=0)

#задать с
txtс = Entry(frame33,width=40, background=colors['bent'])
txtс.place(x=100, y=2)
lblс = Label(frame33, text="с: ", font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff')
lblс.place(x=0, y=0)

frame21 = LabelFrame(frame2, width=350, height=30, background=colors['bfr'])
frame22 = LabelFrame(frame2, width=350, height=30, background=colors['bfr'])
frame23 = LabelFrame(frame2, width=350, height=30, background=colors['bfr'])
frame24 = LabelFrame(frame2, width=350, height=30, background=colors['bfr'])
frame25 = LabelFrame(frame2, width=350, height=30, background=colors['bfr'])
frame26 = LabelFrame(frame2, width=350, height=30, background=colors['bfr'])
frame27 = LabelFrame(frame2, width=350, height=30, background=colors['bfr'])
frame28 = LabelFrame(frame2, width=350, height=30, background=colors['bfr'])

frame21.place(x=10, y=10)
frame22.place(x=10, y=40)
frame23.place(x=10, y=70)
frame24.place(x=10, y=100)
frame25.place(x=10, y=130)
frame26.place(x=10, y=160)
frame27.place(x=10, y=190)
frame28.place(x=10, y=220)

rad1 = Radiobutton(frame21,text='задать вероятность', value=1, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad1.place(x=5, y=0)

#Связность графа
rad2 = Radiobutton(frame22,text='связность(теорема 13)', value=2, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad2.place(x=5, y=0) 

#Планарность графа
rad3 = Radiobutton(frame23,text='планарность(теорема 26)', value=3, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad3.place(x=5, y=0)

#Присутствие треугольников
rad4 = Radiobutton(frame24,text='присутствие треугольников (теорема 12)', value=4, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad4.place(x=5, y=0)

#Отсутсвие треугольников
rad5 = Radiobutton(frame25,text='отсутствие треугольников (теорема 10)', value=5, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad5.place(x=5, y=0)

#Феодальная раздробленность
rad6 = Radiobutton(frame26,text='феодальная раздробленность (стр. 48)', value=6, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad6.place(x=5, y=0)

#Империя
rad7 = Radiobutton(frame27,text='империя (стр. 48)', value=7, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad7.place(x=5, y=0)

#Гигантская компонента связности
rad8 = Radiobutton(frame28,text='Гигантская компонента связности', value=8, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad8.place(x=5, y=0)

Label(frame41, text="cвязность", background=colors['bfr'], font='Arial 10 bold', foreground='#FFFFFF').place(x=5, y=0)
lbl1 = Label(frame41, text='-', font='Arial 12 bold', foreground='#ff0000', background=colors['bfr'])
lbl1.place(x=200, y=0)

Label(frame42, text="планарность", background=colors['bfr'], font='Arial 10 bold', foreground='#FFFFFF').place(x=5, y=0)
lbl2 = Label(frame42, text='-', font='Arial 12 bold', foreground='#ff0000', background=colors['bfr'])
lbl2.place(x=200, y=0)

Label(frame43, text="наличие треугольников", background=colors['bfr'], font='Arial 10 bold', foreground='#FFFFFF').place(x=5, y=0)
lbl3 = Label(frame43, text='-', font='Arial 12 bold', foreground='#ff0000', background=colors['bfr'])
lbl3.place(x=200, y=0)

img = ImageTk.PhotoImage(Image.open("start1.png"))

btn = Button(root, text="отправить", command=Get_data, width=10, height=1, font='Arial 20 bold', background='#228B22', foreground='#FFFFFF')
btn.place(x=460, y=380)

btn = Button(root, text="показать", command=Show_Graph, width=10, height=1, font='Arial 20 bold', background='#DC143C', foreground='#FFFFFF')
btn.place(x=460, y=300)

root.mainloop()