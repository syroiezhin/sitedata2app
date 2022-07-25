# <p id="UP">Want to get data about the site and its IP?</p>

## <p align="center">Give thanks : 5168 7450 1701 5535 <a href="https://en.privatbank.ua/all-ways-to-receive-send-an-international-transfer"><img src="https://upload.wikimedia.org/wikipedia/uk/f/ff/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%8224.png" width = "25" alt="Privat Bank UA"> </a></p>

> In this review, we'll take a look at all the changes.

### tk_wbs_IP.py

> Let's start with the fact that we have improved the input field.
-[X] A variable that holds the entered value.
-[X] Input field.
-[X] Text inside the field.
-[X] Specify the place to display the input field.
-[X] Assign the __click__ function to the input field.
-[X] Assign the __cursor__ function to the input field.
-[X] We instantly update this object to see the result of our assignments.
```python
info = tk.StringVar()
data = tk.Entry(bg='#cfaf32', fg='#2f3f4f', textvariable=info)
data.insert(0,'ENTER URL ...')
data.pack(padx=wdth/3, fill='x', pady=pdy/2, side=tk.TOP)
data.bind("<Button-1>",click)
data.bind("<Leave>",cursor)
data.update()
```
-[X] We need the first __click__ function to remove __the label__ (ENTER URL ...) from the input field.
```python
def analise():
    if data.get() == 'ENTER URL ...': data.delete(0,'end')
    
def click(*args): analise()
```
-[X] We need the second __cursor__ function to return __the label__ (ENTER URL ...) in the input field if it does not contain text.
```python
def cursor(*args):
    win.focus()
    analise()
    if data.get() == '': data.insert(0,'ENTER URL ...')
```

[⇪](#UP)
