# Python-Webradio-simple

This is a simple Python script that uses the vlc module to play a stream from a list of radio stations through a graphical user interface (GUI) created with the tkinter module.

The script first imports the vlc and tkinter modules. It then defines a function called play_radio that plays the selected stream using vlc. The function is called when the user clicks the "Play" button. The function stop_radio is defined to stop the stream when the user clicks the "Stop" button.

The script then creates the GUI with tkinter. It creates a Tk object and sets the window title and size. It then creates a label and a combobox widget with the list of radio stations using the ttk.Combobox class. The combobox is set to be read-only, so the user can only select a stream from the list, but cannot edit it. The script also creates two buttons: "Play" and "Stop", which are associated with the play_radio and stop_radio functions, respectively.

Finally, the script starts the main loop of the GUI with root.mainloop(). This will keep the GUI running until the user closes it.

note: you have to have tkinter, python-vlc and vlc-media player installed for this code to work
