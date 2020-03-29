#main_top.py  Guoxuter
#main_top.py  Guoxuter
#main_top.py  Guoxuter
#main_top.py  Guoxuter
#main_top.py  Guoxuter
#main_top.py  Guoxuter
#main_top.py  Guoxuter
#f_list.py  guoxuter


# txt_path为(r'文件的绝对路径'),txt_line_list为行导出的列表

# txt_path为(r'文件的绝对路径'),txt_line_list为行导出的列表
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from tkinter import *

from tkinter import *
import tkinter.messagebox
#f_list.py  guoxuter


# txt_path为(r'文件的绝对路径'),txt_line_list为行导出的列表
#
def txt_read(txt_path,txt_line_list):
    file1=open(txt_path,"r")
    while True:
        line = file1.readline()
        if not line:
            break
        txt_line_list.append(line)
    file1.close()
# a为含有所有待处理行句子的列表，即txt_line_list
# v_list为单词导出的列表，
# v_number为b所对应单词的词频，
# d为空字符串，f为d导出的列表f导出后应该仅有d一个元素
# g为所有行元素导出的列表[’行1’‘行2‘……]
def txt_Arrangement(a,v_list,v_number,line_list):
 d=''
 f=[]#方便统计进入line—list
 def txt_arrangement(a,aa,d,f):
  d=''
  aa=list(aa.split())
  for k in range(len(aa)):
    if aa[k] == ' ':
      aa.remove(' ')

  for i in range(len(aa)):
    aa[i]=aa[i].strip(",.?<>/@#$%^&*();:!【】{[]}+-！@#￥%……&*（）——+-=【】{}、|；：‘“、？。》，《_=\|")
    aa[i]=aa[i].lower()
    d+=aa[i]
    #print(d)
  f.append(d)
 aaa=[]
 bbb=[]
 for k in range(len(a)):
      aaa.extend(list(a[k].split()))
      bbb.extend(list(a[k].split()))
 for i in range(len(aaa)):
      aaa[i] = aaa[i].strip(",.?<>/@#$%^&*();:!【】{[]}+-！@#￥%……&*（）——+-=【】{}、|；：‘“、？。》，《_=\|")
      aaa[i] = aaa[i].lower()
      d += aaa[i]

 for j in aaa:
    if j in v_list:
        pass
    else:
        v_list.append(j)
        v_number.append(aaa.count(j))


 for i in range(len(a)):
     txt_arrangement(a,a[i], d, f)
     line_list.append(f[i])
 ccc=[aaa,bbb]
 return ccc
#print(list_list_list_of_stoping_V)


#用于统计总词数
#
def txt_size(v_number):
    b=0
    for i in range(len(v_number)):
        b+=v_number[i]
    return b
#解决停用词表问题,返回去除停用词后的v_list 与v_number
def txt_TL(v_list,v_number):
    # 制作停用词表列表
    kkkk = []
    kkk = []
    kk = []
    list_list_list_of_stoping_V = []
    txt_read('D:\A-COURSE\Important  Text\python2\大计基大作业\停用词表.txt', list_list_list_of_stoping_V)
    txt_Arrangement(list_list_list_of_stoping_V, kkkk, kkk, kk)
    list_list_list_of_stoping_V = kkkk



    m=[]
    n=[]
    k=[]
    ccc=v_list
    ddd=v_number
    for i in v_list:
        if i not in list_list_list_of_stoping_V:
            m.append(i)
            n.append(v_number[v_list.index(i)])

    k.append(m)
    k.append(n)
    return k





# keywords_visiable  guoxuter



from matplotlib.font_manager import FontProperties
font = FontProperties(fname='C:\Windows\Fonts\simkai.ttf')



def visiable(k_list,k_number):
    N = 6
    ind = np.arange(N)
    width = 0.35
    fig, ax = plt.subplots()
    plt.bar(ind, k_number, width)


    plt.ylabel(u"词频", FontProperties=font)

    plt.xlabel(u"关键词", FontProperties=font)

    ax.set_xticks(ind)

    ax.set_xticklabels(k_list)

    plt.show()
a=[]
v_list, v_number, line_list = [], [], []
txt_Arrangement(a, v_list, v_number, line_list)




a = []
txt_read('D:\A-COURSE\Important  Text\python2\大计基大作业\PUMA.txt', a)
# print(a)
b = a
v_list = []
v_number = []
line_list = []






aaa = txt_Arrangement(b, v_list, v_number, line_list)
Number_of_the_words=txt_size(v_number)
# print(line_list)

k = txt_TL(v_list,v_number)
#print(k)

# 建立字典对应单词与词频
dic_list = {}
for i in range(len(v_list)):
    dic_list[v_list[i]]=v_number[i]



# 建立关于关键词的列表
guan_jian_ci =[]
guan_jian_ci.append([])
guan_jian_ci.append([])
for i in range(6):
    v_max = max(k[1])
    v_n = k[1].index(v_max)
    guan_jian_ci[1].append(k[1].pop(v_n))
    guan_jian_ci[0].append(k[0].pop(v_n))
#print(guan_jian_ci)






def M1():#词频
    print("请点击文本框旁边按钮")
def M2():   #关键词频
    visiable(guan_jian_ci[0], guan_jian_ci[1])

def T1():
    tkinter.messagebox.showinfo('提示', '全篇词数为：'+str(txt_size(v_number)))



#返回，相当于一键返回txt中的文档
def T2():
    a = []
    txt_read('PUMA.txt', a)
    # print(a)
    b = a
    v_list = []
    v_number = []
    line_list = []

    txt_Arrangement(b, v_list, v_number, line_list)
    Number_of_the_words = txt_size(v_number)
    # print(line_list)

    k = txt_TL(v_list, v_number)
    # print(k)

    # 建立字典对应单词与词频
    dic_list = {}
    for i in range(len(v_list)):
        dic_list[v_list[i]] = v_number[i]

    # 建立关于关键词的列表
    guan_jian_ci = []
    guan_jian_ci.append([])
    guan_jian_ci.append([])
    for i in range(6):
        v_max = max(k[1])
        v_n = k[1].index(v_max)
        guan_jian_ci[1].append(k[1].pop(v_n))
        guan_jian_ci[0].append(k[0].pop(v_n))
    # print(guan_jian_ci)
#
    textbox = Text(top, width=60, height=40, highlightthickness=2)
    textbox.grid(row=1, column=1, sticky=N)
    for i in range(len(a)):
        textbox.insert(INSERT, a[i])

    textbox2 = Text(top, width=60, height=40, highlightthickness=2)
    textbox2.grid(row=1, column=3, sticky=N)
    for i in range(len(line_list)):
        textbox2.insert(INSERT, line_list[i]+'\n')



def S2():
        # print(guan_jian_ci)
#
    textbox = Text(top, width=60, height=40, highlightthickness=2)
    textbox.grid(row=1, column=1, sticky=N)
    for i in range(len(a)):
        textbox.insert(INSERT, a[i])

    # print(a)






# 统计词频并输出
def T3():
    cipin=Tk()
    cipin.geometry("500x600")
    cishuzifuwei=''
    textbox3=Text(cipin, width=60, height=40, highlightthickness=2)
    textbox3.place(x=10, y=10)
    for i in range(len(v_number)):
        cishuzifuwei+=v_list[i]+': '+str(v_number[i])+'\n'

    textbox3.insert(INSERT, cishuzifuwei)
    #tkinter.messagebox.showinfo('词频','各词词频统计：'+cishuzifuwei)
    cipin.mainloop()




#文本查找和高亮
def F1():
    print('1')





    
    #删除单词
def K2():
    top3=Tk()
    top3.geometry("300x150")
    def shan():
        yyyy=e3.get()
        for i in range(len(a)):
            jjjj=yyyy[0]
            kkkk=jjjj.upper()+yyyy[1::]+" "
            #yyyy=" "+yyyy
            a[i]=a[i].replace(yyyy,"")
            a[i]=a[i].replace(kkkk,"")

    e3=Entry(top3)
    e3.place(x=150,y=10)
    Label(top3, text =  "请输入要删除的单词：").place(x=10,y=10)
    Button(top3, text="一键删除", command=shan).place(x=70,y=120)
    top3.mainloop()



#替换单词        

def F2():
    shurudanci=Tk()
    shurudanci.geometry("300x150")
    def huan():
     m=e1.get()
     n=e2.get()
     mmmm=m[0]
     nnnn=n[0]
     mm=m[1::]
     mm=mmmm.upper()+mm
     nn=n[1::]
     nn=nnnn.upper()+nn
    
     for i in range(len(a)):
        a[i]=a[i].replace(m,n)
        a[i]=a[i].replace(mm,nn)

     with open('PUMA.txt', "r+") as f:
        read_data = f.read()
        f.truncate()
        f.write(a)
    # print(a)
    shurudanci.title('输入被替换单词')
    Label(shurudanci, text='请输入被替换单词：').place(x=10,y=10)
    e1=Entry(shurudanci)
    e1.place(x=120,y=10)
    Label(shurudanci, text="请输入 替 换单词：  ").place(x=10,y=60)
    e2=Entry(shurudanci)
    e2.place(x=120,y=60)
    Button(shurudanci, text="进行替换", command=huan).place(x=70,y=120)
    shurudanci.mainloop()






top = Tk()
top.geometry("1150x630")
top.title("文本编辑系统")
Label(top, text="原文本").grid(row=0,column=1)
Label(top, text='编辑文本').grid(row=0, column=3)
Button(top, text='词数统计', command=T1).place(x=518, y=60)
Button(top, text=' 返   回 ', command=T2).grid(row=1, column=2, sticky = N)
Button(top, text='词频统计', command=T3).place(x=518, y=260)
Button(top, text='查找高亮', command=F1).place(x=518, y=180)
Button(top, text="关 键 词",command=M2).place(x=519, y=140)
Button(top, text="替换单词",command=F2).place(x=518, y=220)
Button(top, text="刷    新",command=S2).place(x=518, y=100)
Button(top, text="一键删除",command=K2).place(x=518, y=300)
Label(top, text="                     ").grid(row=1,column=0)
Label(top, text="   ").grid(row=5)
Label(top, text="   ").grid(row=6)
menubar=Menu(top)
MM=[M1, M2]
ii=0
filemenu=Menu(menubar, tearoff=0)
for item in ["词频", "关键词频"]:
    filemenu.add_command(label=item, command=MM[ii])
    filemenu.add_separator()
    ii = ii+1

menubar.add_cascade(label="菜单", menu=filemenu)
menubar.add_command(label="其他")
menubar.add_command(label="退出", command=top.quit)
top['menu']=menubar


textbox = Text(top, width=60, height=40, highlightthickness=2)
textbox.grid(row=1,column=1, sticky=N)
for i in range(len(a)):
    textbox.insert(INSERT, a[i])

textbox2 = Text(top, width=60, height=40, highlightthickness=2)
textbox2.grid(row=1, column=3, sticky=N)
for i in range(len(line_list)):
    textbox2.insert(INSERT, line_list[i]+'\n')






top.mainloop()
