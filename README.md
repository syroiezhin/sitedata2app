# <p id="UP">Do you want to create your first macbook app file?</p>

> To create our first working project using py2app for macbook, we will use a ready-made template called "tk-wbs-ip.py" written using only the Tkinter library to create a simple and useful interface. Then we use it in a more advanced program that extracts information about the owner of the entered domain (getting the site's IP address).

## <p align="center">Give thanks : 5168 7450 1701 5535 <a href="https://en.privatbank.ua/all-ways-to-receive-send-an-international-transfer"><img src="https://upload.wikimedia.org/wikipedia/uk/f/ff/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%8224.png" width = "25" alt="Privat Bank UA"> </a></p>

> Let's start by reviewing this template, which we will need in the project.
- [X] Create a window; 
- [X] Assign an icon to it; 
- [X] Fill the background of the window with gray color; 
- [X] Assign the name of the window, which is displayed in the middle at the top of the window; 
- [X] Set the window size; 
- [X] Prohibit changing window sizes with the last command.
```python
win = tk.Tk()
win.iconphoto(False,tk.PhotoImage(file='icon.png'))
win.config(bg='#2f3f4f')
win.title('DATA SEARCH BY URL')
win.geometry(f"{wdth}x{hght}")
win.resizable(False,False)
```
- [X] Create a variable in which we will write the contents of the Entry();
- [X] Сreate an entry field into which something will be entered;
- [X] You can set focus to this field to position the cursor inside the field on startup;
- [X] Be sure to specify where to display this element, otherwise it will not be visible in the window.
```python
info = tk.StringVar()
data = tk.Entry(bg='#cfaf32', textvariable=info)
data.focus()
data.pack(padx=wdth/3, fill='x', pady=pdy, side='top')
```

[⇪](#UP)
