import pyttsx3   
import speech_recognition as sr 
import wikipedia
import datetime
import subprocess
import os
import webbrowser
import random
import time
import datetime
import smtplib
from email.message import EmailMessage
import requests
from pprint import pprint
import tkinter as tk
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import ImageTk,Image
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[1].id) to print the voices
engine.setProperty('voice',voices[1].id)


anim = None
count = 0
def starting():
    animation(count)
    
    query = takecommand().lower() 

    if 'wikipedia' in query:
        try:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia")
            print(results)

            speak(results)
        except Exception as e:
            print(e)
            speak("There is no Content Regarding this topic in Wikipedia")

    elif 'open calculator' in query:
        try:
            speak('The Calculator is opening')
            os.startfile('calc.exe')
        except Exception as e:
            print(e)
            speak("There is a problem while opening calculator")
    elif 'play music' in query:
            try:
                speak("The Music is playing")
                musicdir = "C:\\Users\\Kalyan\\Music\\Music\\all music"
                songs = os.listdir(musicdir)
                Range = range(1,20)
                os.startfile(os.path.join(musicdir, songs[random.choice(Range)]))
            except Exception as e:
                print(e)
                speak("There is a touble playing Music")
    elif 'quit' in query:
        speak("iam quitting")
        quit()
    elif 'terminate' in query:
        speak("iam terminating")
        quit()
    elif 'tell me a joke' in query:
        jokes = ["What is the most shocking city in the World, its Electricity hahaha\n","Which playing cards are the best dancers,The king and queen of clubs. hahaha\n","what did one ocean say to other ocean, nothing ,they just waved. hehehe\n","what happend when the geese fell down the stairs? they all got goose bumps,hehehe\n"]
        speak(random.choice(jokes))
        t.insert(tk.END,random.choice(jokes),"\n")
        t.see(tk.END)
    elif 'time right now' in query:
        current_time()
    elif 'time' in query:
        current_time()
    elif 'date' in query:
        date = datetime.datetime.today()
        print(date)
        speak(date)
    elif 'hey Alpha' in query:
        print("hi sir, How may i help you")
        speak("hi sir, How may i help you")
    elif 'your name' in query:
        print("my name is Aplha")
        speak("my name is Alpha")
    elif 'yourself' in query :
        print("my name is Alpha,version 1.1.0, and i can perform tasks like searching in wikipedia,opeing websites,telling some jokes ans some more")
        speak("my name is Alpha,version 1.1.0, and i can perform tasks like searching in wikipedia,opeing websites,telling some jokes ans some more")
    elif 'send email' in query:
        emaillist = {
            'kalyan' : 'mkbngrr@gmail.com',
            'babu':'mmkbngr@gmail.com',
            'anusha':'anushasrinivas1221@gmail.com'
                }
        speak("Whom you want to send email")
        receiver = emaillist[takecommand().lower()]
        print(receiver)
        speak("Tell the subject to include")
        subject = takecommand()
        speak("Tell the message that you want to send")
        message = takecommand()

        send_email(receiver,subject,message)
        # server.sendmail("mkbngr@gmail.com","mkbngrr@gmail.com","this is a test mail")
    elif 'weather report' in query:
        speak("Tell the city name")
        city=takecommand()
        print()
        try:
            query='q='+city
            w_data=weather_data(query)
            print_weather(w_data, city)
            print()
        except:
            print('City name not found...') 
    elif 'make a note' in query:
        files = open('reminder.txt','w+')
        speak("say the note you want to save")
        content = takecommand()
        files.write(content)
        os.startfile("reminder.txt")
        files.close()
    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
    elif 'open face book' in query:
        webbrowser.open("https://www.facebook.com")
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'special' in query:
        special()
    else:
        # print(len(query))
        if(len(query)==4):
            speak("please try again or check the network connection and then try again")

        else:
            speak("Your results are")
            driver = webdriver.Chrome()
            driver.get("https://www.google.com")

            inputelements = driver.find_elements_by_css_selector('input[name=q]')

            for  inputele in inputelements:
                inputele.send_keys(query)
                inputele.send_keys(Keys.ENTER)
            time.sleep(10)
            driver.close()

def special():
    dates = str(datetime.datetime.today())

    spiltted = dates.split()
    month_day =str(spiltted[0][5]+spiltted[0][6]+":"+spiltted[0][8]+spiltted[0][9])
    datee = "Date:",spiltted[0]
    print(datee)
    for ke in special_of_the_day.keys():
        if ke==month_day:
            print(special_of_the_day[ke])
            speak(special_of_the_day[ke])
        else:
            speak("there is no special today")
            


                    

def weather_data(query): #to get the wheather data using api
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
	return res.json()
def print_weather(result,city): #to get the wheather report
	temperature_of_city =  "{}'s temperature: {}°C ".format(city,result['main']['temp'])
	wind_speed = "Wind speed: {} m/s".format(result['wind']['speed'])
	Description_of = "Description: {}".format(result['weather'][0]['description'])
	weather = "Weather: {}".format(result['weather'][0]['main'])
	print(temperature_of_city)
	speak(temperature_of_city)
	print(wind_speed)
	speak(wind_speed)
	print(Description_of)
	speak(Description_of)
	print(weather)
	speak(weather)
         

def send_email(receiver, subject, message): #for sending email
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    email_address = "mkbngr@gmail.com"
    password = "Salma@143"
    server.login(email_address,password)
    email = EmailMessage()
    email['from'] = email_address
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)
def current_time(): # to tell the current time
    seconds = time.time()
    times = time.ctime(seconds)
    spliting = times.split()
    print(spliting[3])
    speak(spliting[3])   
def wishme(): # treating according to the time in the day
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Sir,I am Alpha,Please Tell Me How May I help You")


# def timing():
#     text = time.strftime("%H:%M:%S")
#     datelabel.config(text=text)
#     datelabel.after(200,timing)

def speak(audio): # to speak the string
    engine.say(audio)
    engine.runAndWait()


def takecommand(): # to take command and to recognize the speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        t.insert(tk.END,"Listening......\n")
        t.see(tk.END)
        r.pause_threshold = 1
        r.energy_threshold = 2500
        audio = r.listen(source)
    try:
        print("recognizing....")
        t.insert(tk.END,"recognizing....\n")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said :{query}\n")
        t.insert(tk.END,f"user said:{query}\n")
        t.see(tk.END)
    except Exception as e:
        print(e)
        print("say that again please....")
        t.insert(tk.END,"say that again please....\n")
        t.see(tk.END)
        return "None"
    return query

def animation(count):
    global anim
    im2 = im[count]
    animation_label.configure(image=im2)
    count += 1
    anim = root.after(30,lambda:animation(count))

    # if(count == frames):
    #     count = 0

special_of_the_day={"01:01" : "new year",
                    "01:04" : "world braille day",
                    "01:09" : "NRI day",
                    "01:10" : "world Hindi day",
                    "01:12" : "world youth day",
                    "01:15" : "Army Day",
                    "01:25" : "National Voters Day",
                    "01:26" : "India’s Republic Day & International Customs Day",
                    "01:27" :  " International Day of Commemoration",
                    "01:30" : "martyrs'Day",
                    "02:02" : "World Wetlands Day",
                    "02:04" : "World Cancer Day",
                    "02:06" : "International Day of Zero Tolerance to Female Genital Mutilation",
                    "02:10" : "National De-worming Day",
                    "02:11" : " International Day of Women and Girls in Science",
                    "02:12" : " National Productivity Day",
                    "02:13" : "World Radio Day, World Women’s Day",
                    "02:14" : "Valentine’s Day",
                    "02:20" : "World Day of Social Justice",
                    "02:21" : " International Mother Language Day",
                    "02:24" : "Central Excise Day",
                    "02:28" : " National Science Day",
                    "03:01" : " Zero Discrimination Day and World Civil Defence Day",
                    "03:03" : "World Wildlife Day and World Hearing Day",
                    "03:04" : "National Security Day",
                    "03:08" : " International Women’s Day",
                    "03:15" : "World Disabled Day and World Consumer Rights Day",
                    "03:16" : " World Sleep Day",
                    "03:18" : "Ordnance Factories Day (India)",
                    "03:20" : " International Day of happiness and  World Sparrow Day",
                    "03:21" : "World Forestry Day and World Down Syndrome Day & World Poetry Day",
                    "03:22" : "World Day for Water",
                    "03:23" : " World Meteorological Day",
                    "03:24" : "World TB Day",
                    "03:27" : "World Theatre Day",
                    "04:01" : "Odisha day",
                    "04:02" : "World Autism Awareness Day",
                    "04:04" : " International Day for Mine Awareness",
                    "04:05" : " National Maritime Day",
                    "04:07" :"World Health Day",
                    "04:10": "World Homeopathy Day",
                    "04:11" : "National Safe Motherhood Day & National Pet Day",
                    "04:17" : "World Haemophilia Day",
                    "04:18" : "World Heritage Day",
                    "04:19" : "World Liver Day",
                    "04:21" : "Secretaries Day & Civil Services Day",
                    "04:22" : "Earth Day",
                    "04:23" : " World Book and Copyright Day",
                    "04:24" : " National Panchayati Day",
                    "04:25" : "World Malaria Day",
                    "04:26" : "World Intellectual property Day",
                    "04:28" : "World Day for Safety and Health at Work & World Veterinary Day",
                    "04:29" : "International Dance Day",
                    "04:30" : "Ayushman Bharat Diwas",
                    "05:1": "Worker’s Day (International Labour Day) & Maharashtra Day",
                    "05:3":"Press Freedom Day",
                    "05:4": "Coal Miners Day; International Firefighters Day",
                    "05:7":"world Athletics Day",
                    "05:8":"World Red cross Day & Thalassaeima Day",
                    "05:11":"National Technology Day",
                    "05:12":"International Nurse Day and Mothers Day",
                    "05:15":"International Day of family",
                    "05:17":"World Telecommunication Day & World Hypertension Day",
                    "05:18":"World AIDS vaccine Day;International Museum Day",
                    "05:21":"National Anti-Terrorism Day",
                    "05:22":"International Day for Biological Diversity",
                    "05:24":"Common wealth Day",
                    "05:31":"Anti-Tabacco Day",
                    "06:1":"World Milk Day",
                    "06:3":"World Bicycle Day",
                    "06:4":"International Day of Innocent Childern victims of Aggression",
                    "06:5":"world Environment Day",
                    "06:8":"World Ocean Day",
                    "06:12":"Anti-Child Labor Day",
                    "06:13":"International Albinism Awareness Day",
                    "06:14":"World Blood Donor Day",
                    "06:20":"World Refugee Day",
                    "06:21":"International Day of Yoga",
                    "06:23":"United Nations Public Service Day",
                    "06:26":"International Day against Drug Abuse and lllict Trafficiking",
                    "07:1":"Doctors Day",
                    "07:6":"World Zoonoses Day",
                    "07:11":"World Population Day",
                    "07:17":"world Day of International Justice",
                    "07:18":"International Nelson Mandela Day",
                    "07:28":"World Hepatitis Day",
                    "08:5":"International FriendShip Day",
                    "08:6":"Hiroshima Day",
                    "08:8":"World Senior Citizens Day",
                    "08:9":"Quit India Day, Nagasaki Day & International Day of the World’s Indigenous peoples",
                    "08:15":"Indian Independence Day",
                    "08:12":"International Youth Day",
                    "08:19":"Photography Day & World Humanitarian Day",
                    "08:29":"National Sports Day",
                    "09:02" :"Coconut Day",
                    "09:05":"Teacher’s Day & Sanskrit Day",
                    "09:08":"International Literacy Day",
                    "09:14":"Hindi Diwas",
                    "09:15":"Engineers Day & International Day of Democracy",
                    "09:16":"World Ozone Day & International Day for preservation",
                    "09:21":"Alzheimer's Day & Day for Peace&Non-Violence(UN)",
                    "09:22":"Rose Day(Welfare of cancer patients)",
                    "09:23":"International Day of Sign Languages",
                    "09:26":"Day of the Deaf;World COntraception Day",
                    "09:27":"World Tourism Day;World Maritime Day:",
                    "09:29":"World Heart Day",
                    "09:30":"International Translation Day",
                    "10:01":"International Day of the Elderly",
                    "10:02":"Gandhi Jayanthi & International Day of Non-Violence",
                    "10:04":"World Animal Welfare Day",
                    "10:08":"Indian Airforce Day",
                    "10:09":"World Post Office Day",
                    "10:10":"National post Day & World mental health day",
                    "10:11":"National Giri Child Day",
                    "10:13":"UN International Day for Natural Disaster Reducation",
                    "10:14":"World Standards Day",
                    "10:15":"World Students Day & World White Cane Day",
                    "10:16":"World Food Day",
                    "10:24":"UN Day & World Development Information Day",
                    "10:30":"World Thrift Day",
                    "10:31":"National Unity Day",
                    "11:05":"World Tsunami Day",
                    "11:07":"National Cancer Awareness Day",
                    "11:09":"Legal Services Day",
                    "11:14":"Children's Day & Diabetes Day",
                    "11:17":"National EPilepsy Day",
                    "11:20":"Africa Industrialization Day",
                    "11:21":"World Television Day",
                    "11:29":"International Day of Solidarity with Palestinian People",
                    "12:01":"World AIDS Day",
                    "12:02":"National Pollustion Control",
                    "12:03":"World Day of the Handicapped",
                    "12:04":"Indian Navy Day",
                    "12:07":"Indian Armed Forces Flag Day",
                    "12:10":"Human Rights Day & International Children’s Day of Broadcasting",
                    "12:11":"International Mountain Day",
                    "12:14":"World Energy Conservation Day",
                    "12:16":"Vijay Diwas",
                    "12:18":"Minorities Rights Day (India)",
                    "12:22":" National Mathematics Day",
                    "12:23":" Kisan Divas (Farmer’s Day) (India)",
                    "12:24":"National Consumers Day",
                    "12:25":"Chrismas Day",
                    } 




if __name__=="__main__":
    root = Tk()
    root.geometry("1366x768+0+0")
    root.title("Alpha")
    root.configure(bg="#1B1B1B")
    # root.resizable(0,0)
    # root.overrideredirect(1)
    # datelabel = Label(root,font=("ds-digital",50,'bold'),bg='#43ABC9',fg="black",bd=50)
    # datelabel.pack()
    # datelabel.place(x=0,y=0)
    # timing()
    label1 = Label(root,text="Alpha",font=("Waltograph UI Bold",40),bg='#1B1B1B',fg="white")
    label1.pack()
    label1.place(x=390,y=30)
    # label_photo = Image.open("background.png")
    # label_photo = label_photo.resize((1980,1080))
    # label_out = ImageTk.PhotoImage(label_photo)
    # background_labeling = Label(root,image=label_out,bg="#1B1B1B",width="600")
    # background_labeling.pack()
    # background_labeling.place(x=0,y=200)
    photo = Image.open("start.png")
    photo = photo.resize((100,100))
    image_out= ImageTk.PhotoImage(photo)
    button1 = Button(root,text="Start Listening..",width=100,height=100,command=lambda:threading.Thread(target=starting).start(),image=image_out,bg="#1B1B1B",border=0,activebackground="#1B1B1B")
    button1.configure(bg="#1B1B1B")
    button1.pack()
    button1.place(x=400,y=470)

        
    file = 'listening.gif'

    info = Image.open(file)
    frames = (info.n_frames)
    # print(frames)
    im = [tk.PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]
    animation_label = Label(root,image="",activebackground="#1B1B1B",bg="#1B1B1B",height=100)
    animation_label.pack()
    animation_label.place(x=60,y=570)



    t = Text(root,height=47.4,width=80,bg='#1B1B1B',borderwidth=1,fg="white")

    t.pack()
    # t.configure(font=("Monotype Corsiva",10))
    t.place(x=900,y=0)
    wishme()


    root.mainloop()

        