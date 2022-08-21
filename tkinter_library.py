import tkinter as tk
from tkinter import *
root = tk.Tk()


#Creates a message box, args are (Title, Content of Box, Background Color, Text Color, Width of box, Height of box, Position X, Position Y)
#To put the box in the center of the screen, set both position values to -1 (by default it is set to be centered)
#Every box will have an "Ok" button to dismiss the box, to get rid of that, comment out the lines labeled "Ok button"
#By default, every box will be pinned to the front of the screen. To disable this, comment out the area labeled "Bring to front"
#By default, every box will not be resizable by the user. To disable this, comment out the area labeled "Not resizable"
def msg_box(title = "Msg Box", content = "Notification", bgcolor = "White", tcolor = "Black", width=250, height=150, posX=-1, posY=-1):

    ###################################################################
    #Options:

    #Ok button
    exit_button = Button(root, text="Ok", command=root.destroy)
    exit_button.pack(pady=5, side=BOTTOM)
 
 
    #Not resizable
    root.resizable(False, False)

    #Bring to front
    root.attributes('-topmost', 'true')
    ###################################################################

    root.configure(bg=bgcolor)
    root.title(title)
    canvas= Canvas(root, width= width, height= height, bg=bgcolor,highlightthickness=0)
    if posX == -1 and posY == -1:
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight() 
        posX = round((screen_width/2) - (width/2))
        posY = round((screen_height/2) - (height/2))
    x=round(width/2)
    y=round(height/2)
    canvas.create_text(x, y-10, text=content, fill=tcolor, font=('Arial'))
    canvas.pack()
    root.geometry(f'{width}x{height}+{posX}+{posY}')
    root.mainloop()


def findCenterOfScreen(): #Finds the center coordinate of the screen
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight() 
    posX = round(screen_width/2)
    posY = round(screen_height/2)
    return str(posX)+", "+str(posY)


def findMaxScreenCoords(): #Finds the very maximum screen coordinate/resolution of the screen
    posX=root.winfo_screenwidth()
    posY=root.winfo_screenheight() 
    return str(posX)+", "+str(posY)


