import vlc
from tkinter import *
from tkinter import ttk

player = vlc.MediaPlayer("")

def play_radio():
    # get the selected stream
    stream = selected_stream.get()
    # create an instance of vlc
    global player
    player = vlc.MediaPlayer(stream)
    # play the stream
    player.play()
    return



def stop_radio():
    # stop the stream
    global player
    player.stop()
    return

def change_volume(event):
    # change the volume
    global player
    # get the volume from the slider
    vol = volume.get()
    # set the volume
    player.audio_set_volume(vol)
    return
    
# create the root window
root = Tk()
root.title("WebRadio")


# bind the change volume function to the slider
root.bind("<ButtonRelease-1>", change_volume)    

#configure the root window
root.geometry("400x300")
root.resizable(False,False)
root.title("WebRadio")

# configure the rows and columns to have flexible sizes
for i in range(5):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(0, weight=1)

# create a combobox with the webradio streams
selected_stream = StringVar()
streams = ["http://radio886.at/streams/radio_88.6/mp3","http://radio886.at/streams/88.6_Classic_Rock/mp3"]
stream_cb = ttk.Combobox(root, values=streams, textvariable=selected_stream, width=30, height=10, font=("Helvetica", 12), state="readonly")
stream_cb.grid(row=0, column=0, sticky=E+W)


# create a button to play the selected stream
play_button = Button(root, text="Play", command=play_radio)
play_button.grid(row=3, column=0, sticky=E+W)

# create a button to stop the stream
stop_button = Button(root, text="Stop", command=stop_radio)
stop_button.grid(row=4, column=0, sticky=E+W)


#create a slider to control the volume set the standard volume to 100
volume = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=200, width=20, font=("Helvetica", 12))
volume.set(100)
volume.grid(row=1, column=0, sticky=E+W)

# start the mainloop
root.mainloop()
