from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from math import *

from fun import * #Моя функция

def getXY(text):#Получение кординат из текстового виждета
    s = text.get(1.0, END)
    s=s.split('\n')
    s.pop(-1)
    for i in range(0,len(s)):
        s[i]=s[i].split(',')
        s[i]=[float(elem) for elem in s[i]]
    t=list()
    for i in range(0,len(s)):
        l=list()
        for k in range(0,len(s)):
            if k==i:
                l.append(float('inf'))
                continue
            c=sqrt((s[i][0]-s[k][0])**2 + (s[i][1]-s[k][1])**2)
            l.append(c)
        t.append(l)
    return s, t

def risovanie(xy,path):#Рисование графика
    x=list()
    y=list()
    for i in xy:
        plot1.text(i[0], i[1],str(i[0])+','+str(i[1]))
    for i in path:
        x.append(xy[i][0])
        y.append(xy[i][1])
    plot1.plot(x,y)

def fun_perebor():
    x_y,dist_xy=getXY(xy)
    s,pyth,lenn,times=polnyi_perebor(x_y,dist_xy)
    dlina.delete(0, END); dlina.insert(0, str(s))
    time.delete(0, END); time.insert(0, str(times))
    kol.delete(0, END); kol.insert(0, str(lenn))
    risovanie(x_y,pyth)

def fun_metod():
    x_y,dist_xy=getXY(xy)
    s,pyth,lenn,times=dinamicheskoe_programirovanie(x_y,dist_xy)
    dlina.delete(0, END); dlina.insert(0, str(s))
    time.delete(0, END); time.insert(0, str(times))
    kol.delete(0, END); kol.insert(0, str(lenn))
    risovanie(x_y,pyth)

def fun_dinam():
    x_y,dist_xy=getXY(xy)
    s,pyth,lenn,times=dinamicheskoe_programirovanie(x_y,dist_xy)
    dlina.delete(0, END); dlina.insert(0, str(s))
    time.delete(0, END); time.insert(0, str(times))
    kol.delete(0, END); kol.insert(0, str(lenn))
    risovanie(x_y,pyth)

def fun_jadn():
    x_y,dist_xy=getXY(xy)
    s,pyth,lenn,times=dinamicheskoe_programirovanie(x_y,dist_xy)
    dlina.delete(0, END); dlina.insert(0, str(s))
    time.delete(0, END); time.insert(0, str(times))
    kol.delete(0, END); kol.insert(0, str(lenn))
    risovanie(x_y,pyth)

window = Tk()
window.title("Определение кратчайшего пути")
window.geometry("600x550")

frame_top = Frame() #Фрейм для фреймов
frame_top.pack(side=TOP)
frame_bot = Frame() 
frame_bot.pack(side=BOTTOM)


frame_plot = Frame(master=frame_top,bg="gray22" ) #Фрейм для рисования графиков
frame_plot.pack(side=LEFT)

##
fig = Figure(figsize = (5, 5),dpi = 70) # фигура, которая будет содержать график
# список координат
plot1 = fig.add_subplot(111) #Вспомогательный плот
#plot1.plot(y) #Рисуем график
plot1.grid() #Сетка 
plot1.set_ylim(0, 10)
plot1.set_xlim(0, 10)
canvas = FigureCanvasTkAgg(fig,master = frame_plot) #Создаём конву
canvas.draw()
canvas.get_tk_widget().pack()
toolbar = NavigationToolbar2Tk(canvas,frame_plot)
color = "#fff"
for button in toolbar.winfo_children():
    if str(button)!='.!frame.!frame.!navigationtoolbar2tk.!label2':#Закршивать всё кроме координат #Убрать костыль.
        button.config(background=color)
toolbar.update()
canvas.get_tk_widget().pack()
##

frame_xy = LabelFrame(master=frame_top,text="Координаты точке x,y") #Фрейм для точек
frame_xy.pack(side=RIGHT)

xy = Text(master=frame_xy);
xy.pack()

frame_knopka =  LabelFrame(master=frame_bot,relief=SUNKEN,borderwidth=5,text="Расчёты") #Фрейм для Кнопок
frame_knopka.pack(side=LEFT)

But_perebor = Button(master=frame_knopka ,command=fun_perebor, text="Полный перебор")
But_perebor.pack(fill=BOTH)

But_metod = Button(master=frame_knopka ,command=fun_metod, text="Метод ветвей и границ")
But_metod.pack(fill=BOTH)

But_dinam = Button(master=frame_knopka ,command=fun_dinam, text="Динамическое программировние")
But_dinam.pack(fill=BOTH)

But_jadn = Button(master=frame_knopka ,command=fun_jadn, text="Жадный алгоритм")
But_jadn.pack(fill=BOTH)

frame_rezultat = LabelFrame(master=frame_bot,relief=SUNKEN,borderwidth=5,text="Результаты") #Фрейм для Результатов
frame_rezultat.pack(side=RIGHT)

dlina = Entry(master=frame_rezultat);dlina_lbl = Label(master=frame_rezultat, text="Длинна пути")  
dlina.grid(row=0, column=0);dlina_lbl.grid(row=0, column=1)

time = Entry(master=frame_rezultat);time_lbl = Label(master=frame_rezultat, text="Время рассчёта")  
time.grid(row=1, column=0);time_lbl.grid(row=1, column=1)

kol = Entry(master=frame_rezultat);kol_lbl = Label(master=frame_rezultat, text="Количество вариантов")
kol.grid(row=2, column=0);kol_lbl.grid(row=2, column=1)

window.mainloop()
