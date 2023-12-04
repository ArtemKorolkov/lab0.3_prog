class film():
    def load_film(self):
        f=open('films.txt','r', encoding='utf-8')
        dict = {}
        for i in f:
            s = i.split(',')
            dict.update({int(s[0]): s[1][0:-1]})
        return dict

class users():
    def load_users(self):
        f = open('users.txt')
        res=[]
        for i in f:
            m=list(map(int,i.split(',')))
            res.append(m)
        return res

class analiz():
    def recomend(input):
        dict_films=film.load_film(open('films.txt'))
        ls_users=users.load_users(open('users.txt'))
        m=list(map(int,input.split(',')))
        res=[]
        for i in ls_users:
            count=0
            for j in m:
                if i.count(j)>0:
                    count+=1
            res.append([count,i])
        res=sorted(res,reverse=True)
        rec=list(set(res[0][1]))
        for i in m:
            if i in rec:
                rec.remove(i)
        rec.sort()
        print(res)
        return dict_films[rec[0]]

print(film.load_film(open('films.txt','r')))
print(users.load_users(open('users.txt')))
print(analiz.recomend('2,4'))

#2
from tkinter import *
from tkinter import messagebox
users_ls=[]
def sort():
   s = user_tf.get()
   age_ls = list(map(int,age_tf.get().split()))
   age_ls=[0]+age_ls
   if s!='END':
       m=s.split(',')
       users_ls.append([m[0],int(m[1])])
   else:
       diap=[]
       dict={}
       for i in range(0,len(age_ls)-1,2):
           diap.append([age_ls[i],age_ls[i+1]])
       for i in users_ls:
           for j in diap:
               #условие если возраст в диапазоне
               if i[1]>=j[0] and i[1]<=j[1]:
                   group=str(j[0])+'-'+str(j[1])
                   if group in dict.keys():
                       dict[group].append(str(i[0])+' '+'('+str(i[1])+')')
                   else:
                       dict.update({group:[str(i[0])+' '+'('+str(i[1])+')']})
                   break
               elif i[1]>=101:
                   #случай 101+
                   group = '101+'
                   if group in dict.keys():
                       dict[group].append(str(i[0]) + ' ' + '(' + str(i[1]) + ')')
                   else:
                       dict.update({group: [str(i[0]) + ' ' + '(' + str(i[1]) + ')']})
                   break
               elif i[1]>=123:
                   break
       for key, value in dict.items():
           messagebox.showinfo(key,str(key)+': '+', '.join(str(x) for x in value))
       print('result:')
       for key, value in dict.items():
           print(key, ':', ', '.join(str(x) for x in value))

window = Tk() #Создаём окно приложения.
window.title("Деление на возрастные группы") #добавляем название

window.geometry('600x800')
frame = Frame(
   window, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10 #Задаём отступ по вертикали.
)
frame.pack(expand=True) #Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.

#последовательность возрастных групп
age = Label(
   frame,
   text="Введите границы возрастных групп  "
)
age.grid(row=2, column=1)
age_tf = Entry(
   frame,
)
age_tf.grid(row=2, column=2, pady=5)


#строка и окно для ввода пользователей
user = Label(
   frame,
   text="Введите ФИО,возраст респондента  "
)
user.grid(row=3, column=1)
user_tf = Entry(
   frame,
)
user_tf.grid(row=3, column=2, pady=5)

#кнопка довавления пользователей
load_user_btn = Button(
   frame,
   text='Добавить в список',
   command=sort
)
load_user_btn.grid(row=5, column=2)


window.mainloop()