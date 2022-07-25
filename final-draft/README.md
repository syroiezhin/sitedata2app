# <p id="UP">Want to get data about the site and its IP?</p>

## <p align="center">Give thanks : 5168 7450 1701 5535 <a href="https://en.privatbank.ua/all-ways-to-receive-send-an-international-transfer"><img src="https://upload.wikimedia.org/wikipedia/uk/f/ff/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%8224.png" width = "25" alt="Privat Bank UA"> </a></p>

> In this review, we'll take a look at all the changes.

### tk_wbs_IP.py

> Let's start with the fact that we have improved the input field.


- [X] A variable that holds the entered value.
- [X] Input field.
- [X] Text inside the field.
- [X] Specify the place to display the input field.
- [X] Assign the __click__ function to the input field.
- [X] Assign the __cursor__ function to the input field.
- [X] We instantly update this object to see the result of our assignments.
```python
info = tk.StringVar()
data = tk.Entry(bg='#cfaf32', fg='#2f3f4f', textvariable=info)
data.insert(0,'ENTER URL ...')
data.pack(padx=wdth/3, fill='x', pady=pdy/2, side=tk.TOP)
data.bind("<Button-1>",click)
data.bind("<Leave>",cursor)
data.update()
```
- [X] We need the first __click__ function to remove __the label__ (ENTER URL ...) from the input field.
```python
def analise():
    if data.get() == 'ENTER URL ...': data.delete(0,'end')
    
def click(*args): analise()
```
- [X] We need the second __cursor__ function to return __the label__ (ENTER URL ...) in the input field if it does not contain text.
```python
def cursor(*args):
    win.focus()
    analise()
    if data.get() == '': data.insert(0,'ENTER URL ...')
```
> When the __RESULT__ button is pressed, the __processing_data_in_the_wbs_IP_py()__ function is called. In this function, errors will be processed and if there are none, the program will display the result in the __Label()__.
- [X] When pressing the __RESULT__ button, if the field was empty, or consisted of spaces, or contains source text (ENTER URL...), the program will generate an error (Error: you didn't enter a url).
- [X] In the best case, the program will start processing the result and display the obtained information in the __Label()__ field.
- [X] When you click on the __RESULT__ button, if the field contains something that did not pass the filter, the program will generate an error (Error: you did entered something wrong).
```python
if (info.get() == 'ENTER URL ...') or (info.get().replace(' ', '') == ''):
    print(text:="Error: you didn't enter a url")
    lbl['text'] = text
elif info.get().count('.')<3 and (bttn['state'] == tk.NORMAL): 
    bttn['state'] = tk.DISABLED
    print("please wait...")
    lbl['text'] = wbs_IP.main(info.get())
else: 
    print(text:="Error: you did entered something wrong")
    lbl['text'] = text
```
[⇪](#UP)
