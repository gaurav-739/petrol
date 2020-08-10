import urllib.request as urll
import json
import geocoder
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext


api="OQCfyg1-zphLiedjk0VWqRTu9HkreHnx0K7VRKWpnSg"
def petrol(a,b):
    print("petrol station near your location")

    url="https://discover.search.hereapi.com/v1/discover?at="+a+","+b+"&limit=5&lang=en-US&apiKey="+api
    category="petrol-station"
    final_url=url+"&q="+category
    json_obj=urll.urlopen(final_url)
    data=json.load(json_obj)
    lang=[]
    lati=[]
    add=[]

    for item in data['items']:
  

        name=(str(item['title']))
        address= (item['address'])
        addr=(address["label"])
        access= (item['access'])
        lat= (access[0]['lat'])
        lan=(access[0]['lng'])
        lang.append(lan)
        lati.append(lat)
        add.append(addr)
        
    
    

    print(add)
    print(lati)
    print(lang)

    

def charge(a,b):
    print("charge station near your location")
    url="https://discover.search.hereapi.com/v1/discover?at="+a+","+b+"&limit=5&lang=en-US&apiKey="+api
    category="ev-charging-station"
    final_url=url+"&q="+category
    json_obj=urll.urlopen(final_url)
    data=json.load(json_obj)
    lang=[]
    lati=[]
    add=[]

    for item in data['items']:
  

        name=(str(item['title']))
        address= (item['address'])
        addr=(address["label"])
        access= (item['access'])
        lat= (access[0]['lat'])
        lan=(access[0]['lng'])
        lang.append(lan)
        lati.append(lat)
        add.append(addr)
        
   
    

    print(add)
    print(lati)
    print(lang)


g = geocoder.ip('me')
loc=(g.latlng)

longitude=str(loc[0])
latitude=str(loc[1])





root = tk.Tk()
root.title("Charge explorer")
root.geometry("950x500+200+100")
root.resizable(False,False)
root.configure(background="slate gray")

p1 = PhotoImage(file = 'p1.jpg')
root.iconphoto(False, p1)


#main window
photo = tk.PhotoImage(file =r"C:\Users\Jarvis\Downloads\Charge-Explorer-master\Charge-Explorer-master\p1.jpg")

photo1 = tk.PhotoImage(file =r"C:\Users\Jarvis\Downloads\Charge-Explorer-master\Charge-Explorer-master\p2.jpg")

l1 = Label(root,text="Charge Explorer",font=("arial",16,'bold'),bg="black",fg="white",width=15,cursor="dot",relief=SUNKEN,borderwidth=6)
l2 = Label(root,text="Petrol",font=("arial",16,'bold'),fg="seashell4",bg="black",cursor="dot",width=10,relief=SUNKEN,borderwidth=6)
l3 = Label(root,text="Electricity",font=("arial",16,'bold'),fg="seashell4",bg="black",cursor="dot",width=10,relief=SUNKEN,borderwidth=6)

btn = tk.Button(root, text="",image=photo,width=180,compound=BOTTOM,relief=RAISED,borderwidth=6,\
cursor="hand2",command=lambda: petrol(longitude,latitude))



btn1 = tk.Button(root, text="",image=photo1,width=180,compound=BOTTOM,relief=RAISED,borderwidth=6,\
cursor="hand2",command=lambda: charge(longitude,latitude))


l1.grid(row=1,column=3,padx=5,pady=25)
l2.grid(row=2,column=2,padx=5,pady=5)
l3.grid(row=2,column=4,padx=5,pady=5)

btn.grid(row=4,column=2,padx=90,pady=0)
btn1.grid(row=4,column=4,padx=90,pady=0)





root.mainloop()
