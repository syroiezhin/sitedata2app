# <p id="UP">Do you want to create your first macbook app file?</p>

> To create our first working project using py2app for macbook, we will use a ready-made template called __tk-wbs-ip.py__ written using only the Tkinter library to create a simple and useful interface. Then we use it in a final program that extracts information about the owner of the entered domain (getting the site's IP address). The final version is in the final-draft folder.

## <p align="center">Give thanks : 5168 7450 1701 5535 <a href="https://en.privatbank.ua/all-ways-to-receive-send-an-international-transfer"><img src="https://upload.wikimedia.org/wikipedia/uk/f/ff/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%8224.png" width = "25" alt="Privat Bank UA"> </a></p>

### tk-wbs-ip.py

> Let's start by reviewing this template, which we will need in the project.

- [X] Create a application window; 
- [X] Assign an icon to it; 
- [X] Fill the background of the window with gray color; 
- [X] Assign the name, which is displayed in the middle at the top of the window; 
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

> Similarly to the above example, we create two buttons and a text field to test the program's performance.
```python
bttn = tk.Button( win, text="RESULT", highlightbackground='#2f3f4f', command = func, font=fnt, compound=tk.CENTER, state=tk.NORMAL)
bttn.pack(padx=wdth/3, fill='x', side='top')
    
lbl = tk.Label(win, bg='#2f3f4f', fg='#cfaf32', font=f'Helvetica {fnt} bold')
lbl.pack(padx=wdth/3,fill='x', pady=pdy)
    
rerun = tk.Button(text="RERUN", highlightbackground='#2f3f4f', command = reboot, font=fnt, compound=tk.CENTER, state=tk.NORMAL)
rerun.pack(padx=wdth/3, fill='x', pady=pdy, side=tk.BOTTOM)
```

> Now it remains for us to create functions for each of the buttons so that they implement simple functionality, namely:
> 1. For the __RESULT__ button, we will display the entered text in the __Label__ field to make sure that we can use the received value from the __Entry__ in some way in the future. Also, it will be important for us to process the received value of __info__, and for this we can consider the case when only spaces will be entered in the field. We need to block the button after clicking, so that the program will take up its task, which we will implement in the final project.
```python
def func(): 
    lbl['text'] = info.get()
    if info.get().replace(' ', '') == '': pass
    elif bttn['state'] == tk.NORMAL: bttn['state'] = tk.DISABLED
```
> 2. The pre-created second button (__RERUN__) will return the first button (__RESULT__) to its previous status, for the next launch of the program's functionality. After pressing the __RESULT__ button, the input field and the output field of the program result are cleared.
```python
def reboot():
    bttn['state'] = tk.NORMAL
    lbl['text'] = ''
    data.delete(0, tk.END)
```
> I share this simple template with you so that you save time. The file __tk-wbs-ip.py__ will not be used in the project, for this I will create a copy called __final-draft/tk_wbs_IP.py__ and improve the code. My project will use a second python file called __final-draft/wbs_IP.py__, which in turn has evolved from the __website-IP.py__ file. Let's start by analyzing the simplified version of the code, which is also not used in the main project, but it is important for us to understand the code.

### website-IP.py

- [X] To get the ip address of the site use `socket.gethostbyname()` passing it a link to the site.
- [X] Sends an HTTP request to the specified site and receives a JSON object of the result.
```python
requests.get(url=f'http://ip-api.com/json/{ip}').json()
```
- [X] Сollect data from the received json list using the get() request.
- [X] Now we can create an html map with the obtained coordinates of the owner of the IP address:
```python
marker = folium.Map(location=[lat,lon], zoom_start=13, tiles= "CartoDB dark_matter")
folium.CircleMarker(location=[lat,lon], popup = f"{org}<br/>{reg}", radius=50, line_color='#3186cc', fill_color='#3186cc').add_to(marker)
marker.save(f'{os.getcwd()}/map_{ip}.html', 'wb')
```
- [X] In order to see the result of our program, I made the launch of html page for instant viewing.
```python
option = webdriver.ChromeOptions()
        option.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
        driver = webdriver.Chrome(service=Service(f"/USER/v.syroiezhin/.wdm/drivers/chromedriver/mac64/103.0.5060.53/chromedriver"), options=option)
        driver.get("file://" + f"/USER/v.syroiezhin/{html_file}")
```
[⇪](#UP)
