from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

from fun import * #Моя функция

def getXY(text):
    s = text.get(1.0, END)
    s=s.split('\n')
    s.pop(-1)
    for i in range(0,len(s)):
        s[i]=s[i].split(',')
    return s

def fun_perebor():
    x_y=getXY(xy)
    polnyi_perebor()
    dlina.delete(0, END); dlina.insert(0, 'test1')
    time.delete(0, END);  time.insert(0, 'test2')
    kol.delete(0, END);  kol.insert(0, 'test3')

def fun_metod():
    x_y=getXY(xy)
    vetvi_i_grany()
    dlina.delete(0, END); dlina.insert(0, 'test1')
    time.delete(0, END);  time.insert(0, 'test2')
    kol.delete(0, END);  kol.insert(0, 'test3')

def fun_dinam():
    x_y=getXY(xy)
    dinamicheskoe_programirovanie()
    dlina.delete(0, END); dlina.insert(0, 'test1')
    time.delete(0, END);  time.insert(0, 'test2')
    kol.delete(0, END);  kol.insert(0, 'test3')

def fun_jadn():
    x_y=getXY(xy)
    jadnyi_algoritm()
    dlina.delete(0, END); dlina.insert(0, 'test1')
    time.delete(0, END);  time.insert(0, 'test2')
    kol.delete(0, END);  kol.insert(0, 'test3')

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
