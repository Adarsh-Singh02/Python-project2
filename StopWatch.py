import tkinter as Tkinter

# Import datetime
from datetime import datetime

counter=66600
running=False

def counter_label(label):
    def count():
        if running:
            global counter

            # To manage the initial delay.
            if counter==66600:
                display="Starting...⏳"
            else:
                tt=datetime.fromtimestamp(counter)
                string=tt.strftime("%H:%M:%S")
                display=string

            label["text"]=display
            label.after(1000, count)
            counter+=1

    # Triggering the start of the counter.
    count()

# Start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
    start["state"]="disabled"
    stop["state"]="normal"
    reset["state"]="normal"

# Stop function of the stopwatch
def Stop():
    global running
    start["state"]="normal"
    stop["state"]="disabled"
    reset["state"]="normal"
    running=False

# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600

    # If rest is pressed after pressing stop.
    if running == False:
        reset["state"]="disabled"
        label["text"]="Click '▶' to Start⏱"

    # If reset is pressed while the stopwatch is running.
    else:
        label["text"]="Starting...⏳"
root=Tkinter.Tk()
root.title("Stopwatch")
'''root.iconbitmap("img/stopwatch.ico")'''  # optional
root.configure(bg="yellow")  #FFE873

# Fixing the window size.
root.minsize(width=350,height=100)
label=Tkinter.Label(root,text="Click '▶' to Start⏱",fg="#4B8BBE",bg="yellow",font="Verdana 25 bold") #4B8BBE #FFE873
label.pack()
f=Tkinter.Frame(root)
start=Tkinter.Button(f,text="Start ▶",width=10,command=lambda:Start(label))
stop=Tkinter.Button(f,text="Pause ⏸",width=10,state="disabled",command=Stop)
reset=Tkinter.Button(f,text="Reset 🔁",width=10,state="disabled",command=lambda:Reset(label))
f.pack(anchor="center",pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
root.mainloop()