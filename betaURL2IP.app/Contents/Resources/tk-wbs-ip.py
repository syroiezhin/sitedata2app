import tkinter as tk

def reboot():
    bttn['state'] = tk.NORMAL
    lbl['text'] = ''
    data.delete(0, tk.END)

def func(): 
    lbl['text'] = info.get()
    if info.get().replace(' ', '') == '':
        pass
    elif bttn['state'] == tk.NORMAL: bttn['state'] = tk.DISABLED



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
    data = tk.Entry(bg='#cfaf32', textvariable=info)
    data.focus()
    data.pack(padx=wdth/3, fill='x', pady=pdy, side='top')
    
    bttn = tk.Button( win, text="RESULT", highlightbackground='#2f3f4f', command = func, font=fnt, compound=tk.CENTER, state=tk.NORMAL)
    bttn.pack(padx=wdth/3, fill='x', side='top')
    
    lbl = tk.Label(win, bg='#2f3f4f', fg='#cfaf32', font=f'Helvetica {fnt} bold')
    lbl.pack(padx=wdth/3,fill='x', pady=pdy)
    
    rerun = tk.Button(text="RERUN", highlightbackground='#2f3f4f', command = reboot, font=fnt, compound=tk.CENTER, state=tk.NORMAL)
    rerun.pack(padx=wdth/3, fill='x', pady=pdy, side=tk.BOTTOM)

    win.mainloop()