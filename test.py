import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageFilterEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter Editor")

        self.image_path = None
        self.image = None
        self.filtered_image = None

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.apply_filter_button = tk.Button(root, text="Apply Filter", command=self.apply_filter)
        self.apply_filter_button.pack()

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.display_image(self.image)

    def display_image(self, image):
        # Resize the image to fit within 400x400 pixels
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(200, 200, image=photo)
        self.canvas.image = photo

    def apply_filter(self):
        if self.image:
            # Your color manipulation code here
            width, height = self.image.size
            for x in range(width):
                for y in range(height):
                    r, g, b = self.image.getpixel((x, y))
                    average = int((r + g + b) / 2.7)
                    self.image.putpixel((x, y), (r, b, r))
                    if average > 150:
                        self.image.putpixel((x, y), (255, 255, 255))
                    else:
                        self.image.putpixel((x, y), (10, 8, 0))
            self.display_image(self.image)

def main():
    root = tk.Tk()
    app = ImageFilterEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
