# -*- coding: cp950 -*-
import random
def findrandom(listelm,adr,color_num):
    if(adr == 0):
        listelm = random.randint(adr,color_num-1)
    elif(adr == color_num-1):
        listelm = random.randint(0,color_num-2)
    else:
        listelm = random.randint(adr+1,color_num-1)
    return listelm


def newlist(color_num):
    twod_list = []
    for i in range(10):
        new = [0,0,0,0,0,0,0,0,0,0]
        for j in range(10):
            new[j] = random.randint(0,color_num-1)
        twod_list.append(new)  #存入twod_list中
        
    check = checksame(twod_list)
    while len(check) != 0:
        remove(check,twod_list,color_num)
        check = checksame(twod_list)
        
    return twod_list

def checkchange(listed):
    coor1 = input('輸入第一個座標(x.y) : ')  #ex:(1,2) , (2,2)
    coor2 = input('輸入第二個座標(x,y) : ')  #ex:(2,2) , (2,3)
    print(coor1)
    print(coor2)
    print('')
    check = 0
    while check == 0:
        if(coor1[0] > 9 or coor1[0] < 0)and(coor1[1] > 9 or coor1[1] < 0)and(coor2[0] > 9 or coor2[0] < 0)and(coor2[1] > 9 or coor2[1] < 0):
            print('輸入的座標不正確,請重新輸入')
            coor1 = input('輸入第一個座標 : ')
            coor2 = input('輸入第二個座標 : ')
        if(coor1[0] != coor2[0])and(coor1[1] != coor2[1]):
            print('輸入的座標不可交換,請重新輸入1')
            coor1 = input('輸入第一個座標 : ')
            coor2 = input('輸入第二個座標 : ')
        elif(coor1[0] == coor2[0]):
            if(coor1[1]+1 != coor2[1])and(coor1[1]-1 != coor2[1]):
                print('輸入的座標不可交換,請重新輸入2')
                coor1 = input('輸入第一個座標 : ')
                coor2 = input('輸入第二個座標 : ')
            elif(coor1[1]+1 == coor2[1])or(coor1[1]-1 == coor2[1]):
                check = 1
        elif(coor1[1] == coor2[1]):
            if(coor1[0]+1 != coor2[0])and(coor1[0]-1 != coor2[0]):
                print('輸入的座標不可交換,請重新輸入3')
                coor1 = input('輸入第一個座標 : ')
                coor2 = input('輸入第二個座標 : ')
            elif(coor1[0]+1 == coor2[0])or(coor1[0]-1 == coor2[0]):
                check = 1
        elif(coor1[0] == coor2[0])and(coor1[1] == coor2[1]):
            print('輸入的座標不可交換,請重新輸入1')
            coor1 = input('輸入第一個座標 : ')
            coor2 = input('輸入第二個座標 : ')

    temp = 0
    temp = listed[coor1[0]][coor1[1]]
    listed[coor1[0]][coor1[1]] = listed[coor2[0]][coor2[1]]
    listed[coor2[0]][coor2[1]] = temp

    print('   0  1  2  3  4  5  6  7  8  9')   
    for i in range(10):
        print(i),
        print(listed[i])

    print('')
    check = set()
    check = checksame(listed)
    
    if(len(check) >= 3):
        remove(check,listed,color_num)
        print('')
        
        while len(checksame(listed)) != 0:
            print('有連線的座標'),
            print(checksame(listed))
            print('   0  1  2  3  4  5  6  7  8  9')   
            for i in range(10):
                print(i),
                print(listed[i])
            print('')
            
            remove(check,listed,color_num)
            print('消除後的二維陣列')
            print('   0  1  2  3  4  5  6  7  8  9')   
            for i in range(10):
                print(i),
                print(listed[i])
            print('')
        
        print('   0  1  2  3  4  5  6  7  8  9')   
        for i in range(10):
            print(i),
            print(listed[i])
    else:
        print('兩座標交換不能產生連線')
        temp = 0
        temp = listed[coor1[0]][coor1[1]]
        listed[coor1[0]][coor1[1]] = listed[coor2[0]][coor2[1]]
        listed[coor2[0]][coor2[1]] = temp

def checksame(li):
    check = set()
    for i in range(10):
        for j in range(10):
            l = j+1
            check_set = set()
            check_set.add((i,j))
            while l < 10:
                if(li[i][j] == li[i][l] and l < 10):
                    check_set.add((i,l))
                    l+=1
                else:
                    break
            if(len(check_set) >= 3):
                for a in check_set:
                    check.add(a)
            s = i+1
            check_set2 = set()
            check_set2.add((i,j))
            while s < 10:
                if(li[i][j] == li[s][j] and s < 10):
                    check_set2.add((s,j))
                    s+=1
                else:
                    break
            if(len(check_set2) >= 3):
                for b in check_set2:
                    check.add(b)  
    return check

def remove(check,listed,color_num):
    for a in sorted(check):
        for i in range(a[0],0,-1):
            listed[i][a[1]] = listed[i-1][a[1]]
        listed[0][a[1]] = random.randint(0,color_num-1)

def check_nochange(listed):
    check = set()
    for i in range(9):
        check_havechange = 0
        for j in range(9):
            temp = 0
            temp = listed[i][j]
            listed[i][j] = listed[i][j+1]
            listed[i][j+1] = temp
            for a in checksame(listed):
                check.add(a)
            temp = 0
            temp = listed[i][j]
            listed[i][j] = listed[i][j+1]
            listed[i][j+1] = temp
            
            if(len(check) > 0):
                check_havechange = 1
                break
            
            temp = 0
            temp = listed[j][i]
            listed[j][i] = listed[j+1][i]
            listed[j+1][i] = temp
            for b in checksame(listed):
                check.add(b)
            temp = 0
            temp = listed[j][i]
            listed[j][i] = listed[j+1][i]
            listed[j+1][i] = temp
            
            if(len(check) > 0):
                check_havechange = 1
                break
        if(check_havechange == 1):
            break
    if(len(check) > 0):
        return 1
    else:
        return 0
            
from datetime import datetime
color_num = input('要幾種顏色')
listed = []
listed = newlist(color_num)
print('   0  1  2  3  4  5  6  7  8  9')
for i in range(10):
    print(i),
    print(listed[i])
    
while check_nochange(listed):
    checkchange(listed)
    if(check_nochange(listed) == 0):
        print('已經沒有可交換的項目,將刷新陣列')
        listed = newlist(color_num)
          

