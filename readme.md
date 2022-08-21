This library simplifies creating Tkinter messageboxes. The documentation is as follows:

## msg_box("Title", "Content", "Bckground Color", "Text Color", integer width, integer height, integer position X, integer position Y). 
Creates a message box, args are (Title, Content of Box, Background Color, Text Color, Width of box, Height of box, Position X, Position Y)
To put the box in the center of the screen, set both position values to -1 (by default it is set to be centered). 
Every box will have an "Ok" button to dismiss the box, to get rid of that, comment out the lines labeled "Ok button". 
By default, every box will be pinned to the front of the screen. To disable this, comment out the area labeled "Bring to front". 
By default, every box will not be resizable by the user. To disable this, comment out the area labeled "Not resizable". 

## findCenterOfScreen()
Returns the center of screen 1.

## findMaxScreenCoords()
Returns the very maximum coordinates/resolution of the screen.
