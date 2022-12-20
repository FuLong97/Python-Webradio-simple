import vlc
from tkinter import *
from tkinter import ttk

player = None

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
    
    
# create the root window
root = Tk()
root.title("WebRadio")

#configure the root window
root.geometry("400x300")
root.resizable(False,False)
root.title("WebRadio")

# create a label
label = Label(root, text="WebRadio", font=("Helvetica", 16))
label.pack()

# create a combobox with the webradio streams
selected_stream = StringVar()
streams = ["http://radio886.at/streams/radio_88.6/mp3","http://radio886.at/streams/88.6_Classic_Rock/mp3"]
stream_cb = ttk.Combobox(root, values=streams, textvariable=selected_stream, width=30, height=10, font=("Helvetica", 12), state="readonly")
stream_cb.pack()

# create a button to play the selected stream
play_button = Button(root, text="Play", command=play_radio)
play_button.pack()

# create a button to stop the stream
stop_button = Button(root, text="Stop", command=stop_radio)
stop_button.pack()

# start the mainloop
root.mainloop()