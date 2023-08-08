from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import requests
from PIL import ImageTk,Image
from datetime import datetime,date

#creating the basics
start = Tk()
start.title("Global weather app")
start.geometry("400x200")

def get_forcast():
    maxDay=[]
    minDay =[]
    global img1
    base = Toplevel()
    base.title("Global weather app")
    base.geometry("400x600")
    
#-------------------------------------------------------------------------------------------------------------------------------

    location =entry.get()
    location =location.replace(" ","+")
    
    api_req = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=5580229a7d3042049da132814232807&q={location}&days=5&aqi=no&alerts=no")

    try:

        api = json.loads(api_req.content)

        cur_temp =api["current"]["temp_c"]
        city_name = api["location"]["name"]
        wind = api["current"]["wind_kph"]
        chance_of_rain =api['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
        
        #appending all the min,max values 
        for forcast_day in api['forecast']["forecastday"]:
            day = forcast_day["day"]
            maxDay.append(day["maxtemp_c"])
            minDay.append(day["mintemp_c"])

    except Exception as e:
        api ="Error for some reasone"

    #-------------------------------------------------------------------------------------------------------------------------------
    # the upper area - today forcast: temp.wind,rain 
    color = "#aee0f5"
    #Create an frame
    today_frame= Frame(base, bg= color,bd=20)


    #Create an label inside the frame
    lab=Label(today_frame, text= city_name,bg=color)
    lab.config(font=("Fixedsys",30))
    lab.pack()

    #the current data:
#-------------------------------------------------------------------------------------------------------------------------------
    #choosing the right img
    # getting the current hour for the img-sun\moon

    now = datetime.now()
    now_hour = now.strftime("%H")
    now_hour = int(now_hour)
    
    if(now_hour > 19):
        img1 = ImageTk.PhotoImage(Image.open("moon.png"))
    else:
        img1 = ImageTk.PhotoImage(Image.open("sun.png"))

    if(chance_of_rain >= 40):
         img1 = ImageTk.PhotoImage(Image.open("rainfall.png"))
    
#-------------------------------------------------------------------------------------------------------------------------------
    Label(today_frame,image=img1,bg=color).pack()
    
    temp=Label(today_frame, text= str(cur_temp)+"°"+"\nwind:"+str(wind)+"km"+"\nchance of rain:"+str(chance_of_rain)+'%',bg=color)
    temp.config(font=("Fixedsys",20))
    temp.pack()
    
    today_frame.pack(expand=True,fill=BOTH)

#-------------------------------------------------------------------------------------------------------------------------------
#The bars frame: 7 days forcast base on max & min temp
    
    fig ,ax = plt.subplots() 
    
    bar_frame= Frame(base, bg= color,bd=20)
    
    canvas =FigureCanvasTkAgg(fig, master=bar_frame)
    canvas.get_tk_widget().pack()
    
    days =['sun','mon','tue','wed','thu']
    
    plt.style.use('fivethirtyeight')
    fig.patch.set_facecolor(color)
    
    ax.set_title("Temp")
    ax.plot(days,maxDay,label="max",color="#f54242",linewidth=2)
    ax.plot(days,minDay,label="min",color="#7bcbed",linewidth=2)
    
    plt.legend(loc="best",fontsize=10)
    ax.grid(True)
    plt.tight_layout()

    canvas.draw()
    
    bar_frame.pack(expand=True,fill=BOTH)
#-------------------------------------------------------------------------------------------------------------------------------
#Opening page
open_frame= Frame(start, bg= "#aee0f5",bd=20)

lab = Label(open_frame,text="type your desire destanation",bg="#aee0f5")
lab.config(font=("Fixedsys",10))

entry = Entry(open_frame)
loc = entry.get()

but = Button(open_frame,text="press when you ready",command=get_forcast)

lab.pack()
entry.pack()
but.pack()

open_frame.pack(expand=True,fill=BOTH)

start.mainloop()


