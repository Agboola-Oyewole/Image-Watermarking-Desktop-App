from tkinter import *
from PIL import ImageTk, Image, ImageGrab
from tkinter import filedialog, messagebox
import numpy as np


def get_image():
    file = filedialog.askopenfilename()
    return file


def save():
    x = window.winfo_rootx() + canvas.winfo_x()
    y = window.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save('updated_image.jpg')


def watermark():
    text = text_entry.get().title()

    if len(text) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        canvas.itemconfig(title_text, text='@' + text, fill="#fff", font=("Noto Sans", 20, "italic"))


request = messagebox.askyesno(title="Upload an Image", message="Do you want to upload an image?")
if request:
    filename = get_image()
    my_img = Image.open(filename)
    img_array = np.array(my_img)
    print(img_array.shape)
    img_height = img_array.shape[0]
    img_width = img_array.shape[1]
    canvas_width = int(img_width / 2)
    canvas_height = int(img_height / 2)
    if img_width > 1000 or img_height > 500:
        messagebox.showerror(title="Error", message=f"This file {img_width}x{img_height} exceeding "
                                                    f"the maximum of 1000x500"
                                                    f". Please upload a lesser resolution and try again.")
    else:
        BACKGROUND_COLOR = "#65647C"
        window = Tk()
        window.title("Water Marker")
        window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)
        canvas = Canvas(width=img_width, height=img_height, highlightthickness=0)
        image = Image.open(filename)
        photo = ImageTk.PhotoImage(image)
        canvas_image = canvas.create_image(canvas_width, canvas_height, image=photo)
        title_text = canvas.create_text(canvas_width + 290, canvas_height + 200, text="", font=("Arial", 25, "italic"))
        canvas.grid(column=0, row=0)

        text_label = Label(text="Text to be displayed:", font=("Montserrat", 10, "bold"), background=BACKGROUND_COLOR)
        text_label.config(pady=20, padx=0)
        text_label.place(x=(-220 + (img_width / 2)), y=img_height + 10)

        text_entry = Entry(width=29)
        text_entry.focus()
        text_entry.place(x=(-80 + (img_width / 2)), y=img_height + 20)
        add_button = Button(text="Add Text", font=("Montserrat", 10, "bold"), command=watermark)
        add_button.config(width=10, height=-2)
        add_button.place(x=(120 + (img_width / 2)), y=img_height + 20)
        save_button = Button(text="Save Image", font=("Montserrat", 10, "bold"), command=save)
        save_button.config(width=45)
        save_button.place(x=(-80 + (img_width / 2)), y=img_height + 50)
        # Run the mainloop
        window.mainloop()
