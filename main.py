from tkinter import *
from PIL import Image, ImageTk  # Import Image and ImageTk from Pillow

# Create an instance of tkinter frame
win = Tk()

# Define the geometry of window
win.geometry("2560x1664")

# Set the background color to white
win.config(bg="white")

#--------------------------------------------------------------------------------------------------------------------------------------

# Making Circle 

# Create a canvas object for the circle
circle_canvas = Canvas(win, width=500, height=500, bg="white")  # Set canvas background to white
circle_canvas.pack()

# Get the center of the canvas
center_x = 500 // 2
center_y = 500 // 2
radius = 200

# Draw the circle, adjusting by radius to center it with a thicker outline
circle_canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black", width=10)

#--------------------------------------------------------------------------------------------------------------------------------------

# Making Buttons 

# Create a frame for buttons below the circle
button_frame = Frame(win, bg="white")  # Set button frame background to white
button_frame.pack(pady=20)  # Add some vertical padding

# Load and resize images
def load_image(image_path, size):
    img = Image.open(image_path)  # Open the image file
    img = img.resize(size, Image.Resampling.LANCZOS)  # Resize the image using LANCZOS (replacement for ANTIALIAS)
    return ImageTk.PhotoImage(img)  # Convert to PhotoImage
        
# Define button size (100x100 pixels)
button_size = (100, 100)

# Load resized images
no_music_img = load_image("no_music.png", button_size)
campfire_img = load_image("campfire.png", button_size)
waves_img = load_image("waves.png", button_size)
rain_img = load_image("rain.png", button_size)

# Create buttons with resized images
button1 = Button(button_frame, image=no_music_img, width=100, height=100)
button1.pack(side=LEFT, padx=10)

button2 = Button(button_frame, image=campfire_img, width=100, height=100)
button2.pack(side=LEFT, padx=10)

button3 = Button(button_frame, image=waves_img, width=100, height=100)
button3.pack(side=LEFT, padx=10)

button4 = Button(button_frame, image=rain_img, width=100, height=100)
button4.pack(side=LEFT, padx=10)

# Start the Tkinter event loop
win.mainloop()