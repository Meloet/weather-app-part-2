from http.client import responses
from tkinter import *
from tkinter.font import BOLD
from numpy import place
import requests

def getweather():
    city=city_text.get()
    link='https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=22515dbe8047cf659da74a1cae281c2e'
    responce=requests.get(link)
    data=responce.json()
    placeLabel['text']='{} , {}'.format(data['name'],data['sys']['country'])
    placeLabel.place(x=200,y=150)
    templabel['text']='Temperature : {} °C'.format(data['main']['temp'])
    templabel.place(x=200,y=180)

root=Tk()
root.title('Weather App')
root.geometry('500x300')

title=Label(root,text='Weather App',font=('bold',10)).place(x=190,y=50)
city_label=Label(root,text='Enter Your City',font=('bold',15)).place(x=110,y=80)
city_text=StringVar()
city_entry=Entry(root,textvariable=city_text)
city_entry.place(x=265,y=90)

goButton=Button(root,text='Go',width=12,command=getweather)
goButton.place(x=210,y=120)

placeLabel=Label(root,text='',font=('bold',10))
templabel=Label(root,text='',font=('bold',10))
root.mainloop()