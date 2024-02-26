import tkinter as tk
from PIL import Image, ImageTk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Tkinter Image Example")

    # Open and convert the image using Pillow
    image_path = "C:\\Users\\U429604\\OneDrive - Danfoss\\Desktop\\Python\\NewUser\\logoDanfoss.png"
    pil_image = Image.open(image_path)
    img = ImageTk.PhotoImage(pil_image)

    # Create a label to display the image
    label = tk.Label(root, image=img)
    label.pack()

    # Run the Tkinter event loop
    root.mainloop()

main()
