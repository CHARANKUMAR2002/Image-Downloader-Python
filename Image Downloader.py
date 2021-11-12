import requests as re
from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.title("Image Downloader")
root.config(bg="systembuttonface")
root.geometry("300x145")


Label(root, text="Image Downloader", font=('times', 16,'italic', 'bold')).pack(pady=10)
Label(root, text="Paste The Image Url Below", font=('times', 14,'italic')).pack()
url = Entry(root, width=35, font=('times', 12, 'underline'), bg='systembuttonface', fg='blue', bd=0)
url.pack(pady=5)


def download():
    try:
        if len(url.get()) != 0:
            global save_file
            save_file = filedialog.asksaveasfilename(initialdir='C:/Users/Welcome/Pictures', defaultextension = ".jpg", filetypes=(("JPG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")))
            img_url = url.get()
            File = str(save_file)
            img = re.get(img_url)
            with open(File, 'wb') as image:
                image.write(img.content)
                messagebox.showinfo('Image Downloader', 'Image Downloaded')
        else:
            messagebox.showerror("Image Downloader", "Link Has Not Be Provided !")

    except re.exceptions.ConnectionError:
        messagebox.showerror("Image Downloader", "Could Not Download Image!\nCheck Your Internet Connection")
        root.update()


Button(root, text="Download", command=download).pack()


root.mainloop()
