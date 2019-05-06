from tkinter import *
from gtts import gTTS
import os

counter_red = 30
counter_yellow = 6
counter_green = 26
seconds = 0
color = ''

global root
root = Tk()
root.title("Signaling")

global canvas
canvas = Canvas(height=350, width=650)
canvas.pack()

red_circle = canvas.create_oval(50, 50, 200, 200, fill="red")
yellow_circle = canvas.create_oval(250, 50, 400, 200, fill="yellow")
green_circle = canvas.create_oval(450, 50, 600, 200, fill="green")

middle_rectangle = canvas.create_rectangle(250, 250, 400, 300, fill="pink")


def countdown():

    global counter_red
    global counter_yellow
    global counter_green
    global middle_rectangle

    if counter_red > 1:
        counter_red -= 1
        if counter_red % 2 == 0:
            red_circle = canvas.create_oval(50, 50, 200, 200, fill="orange")
        else:
            red_circle = canvas.create_oval(50, 50, 200, 200, fill="red")
        middle_rectangle = canvas.create_rectangle(250, 250, 400, 300, fill="red")
        label1.config(text="Time left: " + str(counter_red))

    elif counter_yellow > 1:
        counter_yellow-=1
        if counter_yellow % 2 == 0:
            yellow_circle = canvas.create_oval(250, 50, 400, 200, fill="pink")
        else:
            yellow_circle = canvas.create_oval(250, 50, 400, 200, fill="yellow")
        middle_rectangle = canvas.create_rectangle(250, 250, 400, 300, fill="yellow")
        label1.config(text="Time left: "+str(counter_yellow))

    elif counter_green > 1:
        counter_green-=1
        if counter_green % 2 == 0:
            green_circle = canvas.create_oval(450, 50, 600, 200, fill="lime")
        else:
            green_circle = canvas.create_oval(450, 50, 600, 200, fill="green")
        middle_rectangle = canvas.create_rectangle(250, 250, 400, 300, fill="green")
        label1.config(text="Time left: "+str(counter_green))
    else:
        counter_red = 30
        counter_yellow = 6
        counter_green = 26

    label1.after(1000, countdown)


def start_signal():

    print("Inside Start Function")
    if counter_red == 30:
        countdown()
    elif counter_yellow == 6:
        countdown()
    else:
        countdown()


def stop_signal():
    print("Inside Stop Function")
    root.destroy()


def file_writing():
    file = open("signal.txt", "w")
    file.write(str(seconds))
    file.close()


def which_signal():
    try:
        file = open("signal.txt", "r")
        string1 = file.read()

        if color == 'red':
            string_to_say = "Red signal is on, Now you can go for" + string1 + "Seconds"
        elif color == 'yellow':
            string_to_say = "Yellow signal is on, now wait."
        elif color == 'green':
            string_to_say = "Green signal is on, you have to wait for" + string1 + "Seconds"

        sound = gTTS(text=string_to_say, lang="en")
        sound.save("F:\Python Projs\signal.mp3")

        os.chdir("F:\Python Projs")
        os.system("signal.mp3")
    except UnboundLocalError:
        print("Local Variable is unbounded and Not Found!!, Exception handled.")
    except FileNotFoundError:
        print("Requested media file is not found, Exception handled.")


def time_speak():
    global color
    color = canvas.itemcget(middle_rectangle, 'fill')
    print(color)
    global seconds
    if color == 'red':
        seconds = counter_red
        print(seconds)
        #file_writing()
        #which_signal()
    elif color == 'yellow':
        seconds = counter_yellow
        print(seconds)
        #file_writing()
        #which_signal()
    elif color == 'green':
        seconds = counter_green
        print(seconds)
        #file_writing()
        #which_signal()
    else:
        print("Error Occured, Exception handled")
    file_writing()
    which_signal()


start_btn = Button(root, text="Start", height=2, width=40, command=start_signal)
start_btn.pack()
stop_btn = Button(root, text="Stop", height=2, width=40, command=stop_signal)
stop_btn.pack()

label1 = Label(root, text="Time left: " + str(counter_red), font=('Helvetica', 12))
label1.pack()

label = Label(root, font=('Helvetica', 60))
label.pack()

run_btn = Button(root, text="How much time remaining ???", height=2, width=40, command=time_speak)
run_btn.pack()


root.mainloop()




