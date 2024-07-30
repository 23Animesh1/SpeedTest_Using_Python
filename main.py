from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / 10**6, 3)) + " Mbps"  # Call download() method
    up = str(round(sp.upload() / 10**6, 3)) + " Mbps"  # Call upload() method
    lab_down.config(text=down)
    lab_up.config(text=up)

# Create the main window
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg='sky blue')

# Add a label for the title
lab = Label(sp, text="Internet Speed Test", font=('Time New Roman', 30, "bold"), bg='white', fg='black')
lab.place(x=60, y=40, height=50, width=380)

# Add a label for download speed
lab = Label(sp, text="Download Speed", font=('Time New Roman', 30, "bold"))
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=('Time New Roman', 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

# Add a label for upload speed
lab = Label(sp, text="Upload Speed", font=('Time New Roman', 30, "bold"))
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=('Time New Roman', 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

# Add a button to check speed
button = Button(sp, text="Check Speed", font=('Time New Roman', 30, "bold"), relief=RAISED, bg='yellow', command=speedcheck)
button.place(x=60, y=460, height=50, width=380)

# Run the main loop
sp.mainloop()
