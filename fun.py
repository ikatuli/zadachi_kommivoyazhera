import time
import itertools
from numpy import exp,sqrt,arange

def polnyi_perebor(xy,dist_xy):
    times=time.perf_counter();
    matrix=itertools.permutations(range(len(xy)))
    tmp=list()
    mini=10000
    g=0 # Количество итераций
    for j in matrix:
        g+=1
        j_tmp=list(j)
        j_tmp.append(j_tmp[0])
        suma=0
        for k in range(0,len(j_tmp)-1):
            suma+=dist_xy[j_tmp[k]][j_tmp[k+1]]
        if (suma<mini) and (suma!=float('inf')):
            mini=suma
            tmp=j_tmp

    return suma,tmp,g,time.perf_counter()-times

#Функция нахождения минимального элемента, исключая текущий элемент
def Min(lst,myindex):
    return min(x for idx, x in enumerate(lst) if idx != myindex)

#функция удаления нужной строки и столбцах
def Delete(matrix,index1,index2):
    del matrix[index1]
    for i in matrix:
        del i[index2]
    return matrix


def vetvi_i_grany(xy,dist_xy): #https://github.com/Clever-Shadow/python-salesman
    times=time.perf_counter();
    matrix=list()
    for i in range(len(dist_xy)):matrix.append(dist_xy[i].copy())
    H=0
    PathLenght=0
    Str=[]
    Stb=[]
    res=[]
    result=[]
    Str=[i for i in range(len(matrix))]
    Stb=Str.copy()

    while True:
        for i in range(len(matrix)): # Редукция по столбцам и колоннам
            min_row = min(matrix[i])
            min_column = min(row[i] for row in matrix)
            H += min_row + min_column
            for j in range(len(matrix)):
                matrix[i][j] -= min_row
                matrix[j][i] -= min_column

        #Оценка клеток и поиск нулевых клеток с максимальной оценкой
        NullMax=0
        index1=0
        index2=0
        tmp=0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j]==0:
                    tmp=Min(matrix[i],j)+Min((row[j] for row in matrix),i)
                    if tmp>=NullMax:
                        NullMax=tmp
                        index1=i
                        index2=j

        #Нахождение необходимого пути. Удаление ненужного.

        res.append(Str[index1]+1)
        res.append(Stb[index2]+1)

        oldIndex1=Str[index1]
        oldIndex2=Stb[index2]

        if oldIndex2 in Str and oldIndex1 in Stb:
            NewIndex1=Str.index(oldIndex2)
            NewIndex2=Stb.index(oldIndex1)
            matrix[NewIndex1][NewIndex2]=float('inf')
        del Str[index1]
        del Stb[index2]
        matrix=Delete(matrix,index1,index2)
        if len(matrix)==1:break

    for i in range(0,len(res)-1,2): #Порядок пути
        if res.count(res[i])<2:
            result.append(res[i])
            result.append(res[i+1])
    for i in range(0,len(res)-1,2):
        for j in range(0,len(res)-1,2):
            if result[len(result)-1]==res[j]:
                result.append(res[j])
                result.append(res[j+1])

    result=[x-1 for x in result]
    #result.insert(0,0)
    for i in range(0,len(result)-1,2):
        if i==len(result)-2:
            PathLenght+=dist_xy[result[i]][result[i+1]]
            PathLenght+=dist_xy[result[i+1]][result[0]]
        else:
            PathLenght+=dist_xy[result[i]][result[i+1]]

    tmp=result.index(0) #Преобразуем в формат для рисования.
    vozvrat=list()
    while True:
        vozvrat.append(result[tmp])
        tmp1=(tmp+1)%len(result)
        if result[tmp1]==result[tmp]:
            tmp1=(tmp+2)%len(result)
        tmp=tmp1
        if result[tmp]==0:
            break

    vozvrat.append(0) #print(vozvrat)


    return PathLenght,vozvrat,len(result),time.perf_counter()-times

def dinamicheskoe_programirovanie(xy,distxy):
    times=time.perf_counter();
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(distxy[0][1:])}
    #Словарь, где ключом является два индекса ячейка в строке. Значением является расстояние от первой точки до второго индекса.
    cnt = len(xy)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + distxy[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])
        A = B
    res = min([(A[d][0] + distxy[0][d[1]], A[d][1]) for d in iter(A)])
    res[1].append(0)

    g=1;
    for i in range(1,cnt):
        g*=i;
    
    return res[0],res[1],g,time.perf_counter()-times


def jadnyi_algoritm(xy,distxy):
    times=time.perf_counter();
    n=len(xy)
    RS=[];RW=[];RIB=[]
    s=[]
    for ib in arange(0,n,1):
        way=[]
        way.append(ib)
        for i in arange(1,n,1):
            s=[]
            for j in arange(0,n,1):
                s.append(M[way[i-1]][j])
                for j in arange(0,i,1):
                    distxy[way[i]][way[j]]=float('inf')
                    distxy[way[i]][way[j]]=float('inf')
        S=sum([sqrt((XY[way[i]][0]-XY[way[i+1]][0])**2+(XY[way[i]][1]-XY[way[i+1]][0])**2) for i in arange(0,n-1,1)])+ sqrt((XY[way[n-1]][0]-XY[way[0]][0])**2+(XY[way[n-1]][0]-XY[way[0]][0])**2)
        RS.append(S)
        RW.append(way)
        RIB.append(ib)
    
    S=min(RS)
    way=RW[RS.index(min(RS))]
    ib=RIB[RS.index(min(RS))]
    way.append(way[-1])

    return S,way,len(RS),time.perf_counter()-times
