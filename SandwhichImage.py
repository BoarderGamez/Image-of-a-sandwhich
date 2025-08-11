import tkinter as tk
from PIL import Image, ImageTk  # Pillow for better image handling

# Create the main window
root = tk.Tk()
root.title("Sandwich Display - Yasss")

# Load the image with Pillow
image = Image.open("Sandwhich.png")
photo = ImageTk.PhotoImage(image)

# Create a label to hold the image
label = tk.Label(root, image=photo)
label.pack(padx=20, pady=20)
# Run the app
root.mainloop()
