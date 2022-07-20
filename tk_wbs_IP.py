import wbs_IP
import tkinter as tk

def reboot():
    bttn['state'] = tk.NORMAL
    lbl['text'] = ''
    data.delete(0, tk.END)
    cursor()

def processing_data_in_the_wbs_IP_py(): 
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
    

def analise():
    if data.get() == 'ENTER URL ...': data.delete(0,'end')
    
def click(*args): analise()
    
def cursor(*args):
    win.focus() # when we move the cursor away from the Entry field, we lose the ability to enter until the next click 
    analise()
    if data.get() == '': data.insert(0,'ENTER URL ...')
    
    

if __name__ == '__main__':
    
    wdth = (hght := 300)
    fnt = (pdx := (pdy := 16))
    
    win = tk.Tk()
    win.iconphoto(False,tk.PhotoImage(file='icon.png'))
    win.config(bg='#2f3f4f')
    win.title('DATA SEARCH BY URL')
    win.geometry(f"{wdth}x{hght}")
    win.resizable(False,False)
    
    info = tk.StringVar()
    data = tk.Entry(bg='#cfaf32', fg='#2f3f4f', textvariable=info)
    data.insert(0,'ENTER URL ...')
    data.pack(padx=wdth/3, fill='x', pady=pdy/2, side=tk.TOP)
    data.bind("<Button-1>",click)
    data.bind("<Leave>",cursor)
    data.update() # this is an important command for the correct operation of the program as a whole
    
    bttn = tk.Button( win, text="RESULT", highlightbackground='#2f3f4f', command = processing_data_in_the_wbs_IP_py, font=fnt, compound=tk.CENTER, state=tk.NORMAL)
    bttn.pack(padx=wdth/3, fill='x', pady=pdy/2, side=tk.TOP)
    
    lbl = tk.Label(win, text="", bg='#2f3f4f', fg='#cfaf32', width=2*pdx, height=8, font=f'Helvetica {fnt} bold')
    lbl.pack(side=tk.TOP)
    
    rerun = tk.Button(text="RERUN", highlightbackground='#2f3f4f', command = reboot, font=fnt, compound=tk.CENTER, state=tk.NORMAL)
    rerun.pack(padx=wdth/3, fill='x', pady=pdy/2, side=tk.BOTTOM)

    win.mainloop()