from tkinter import *
from PIL import ImageTk,Image
from tkinter import font
from tkinter import scrolledtext
import tkinter.messagebox
from tkinter.filedialog import *

#root window
root=Tk()
root.title("Modern Note-Taking")
# Load and set icon
try:
    icon = Image.open("icon/notes.png")
    icon = icon.resize((32, 32), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(icon)
    root.iconphoto(False, photo)
except:
    print("Icon file not found")
root.geometry("800x700")  # ปรับขนาดหน้าต่างให้ใหญ่ขึ้น
root.resizable(0,0)

# Modern color scheme
COLORS = {
    'bg': '#2E3440',           # สีพื้นหลักแบบ Nord theme
    'menu_bg': '#3B4252',      # สีพื้นเมนูเข้มขึ้น
    'text_bg': '#4C566A',      # สีพื้นที่พิมพ์
    'text_fg': '#ECEFF4',      # สีตัวอักษร
    'button_bg': '#5E81AC',    # สีปุ่มกด
    'button_hover': '#81A1C1', # สีปุ่มตอนเมาส์ชี้
    'accent': '#88C0D0'        # สีเน้น
}

root.config(bg=COLORS['bg'])

def changeFont(e):
    if fontStyle.get()=="none":
        myFont=(fontFamily.get(),fontSize.get())
    else:
        myFont=(fontFamily.get(),fontSize.get(),fontStyle.get())
    textArea.config(font=myFont)

def newNote():
    confirm=tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการสร้างโน๊ตใหม่หรือไม่ ?")
    if confirm=="yes":
        textArea.delete("1.0",END)

def closeNote():
    confirm=tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่ ?")
    if confirm=="yes":
        root.destroy()

def saveNote():
    myFile=asksaveasfilename(initialdir="./",title="บันทึกโน๊ต",filetypes=(("Text File","*.txt"),("All File","*")))
    with open(myFile,"w",encoding="utf8") as file:
        file.write(fontFamily.get()+"\n")
        file.write(str(fontSize.get())+"\n")
        file.write(fontStyle.get()+"\n")
        file.write(textArea.get("1.0",END))

def openNote():
    myFile=askopenfilename(initialdir="./",title="เปิดโน๊ต",filetypes=(("Text File","*.txt"),("All File","*")))
    with open(myFile,"r",encoding="utf8") as file:
        textArea.delete("1.0",END)
        fontFamily.set(file.readline().strip())
        fontSize.set(file.readline().strip())
        fontStyle.set(file.readline().strip())
        changeFont(1)
        content=file.read()
        textArea.insert("1.0",content)

# Button hover effect
def on_enter(e):
    e.widget['background'] = COLORS['button_hover']

def on_leave(e):
    e.widget['background'] = COLORS['button_bg']

#design frame
menuFrame=Frame(root, bg=COLORS['menu_bg'], padx=10, pady=10)
textFrame=Frame(root, bg=COLORS['bg'], padx=10, pady=5)
menuFrame.pack(fill=X, padx=5, pady=5)
textFrame.pack(fill=BOTH, expand=True, padx=5, pady=5)

# Load and resize menu icons
def load_icon(path):
    img = Image.open(path)
    img = img.resize((24, 24), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Custom button style
button_style = {
    'bg': COLORS['button_bg'],
    'activebackground': COLORS['button_hover'],
    'relief': 'flat',
    'borderwidth': 0,
    'padx': 10,
    'pady': 5
}

#menu buttons with modern style
new_img=load_icon("icon/add.png")
btnNew=Button(menuFrame, image=new_img, command=newNote, **button_style)
btnNew.grid(row=0, column=0, padx=5, pady=5)
btnNew.bind("<Enter>", on_enter)
btnNew.bind("<Leave>", on_leave)

open_img=load_icon("icon/open-folder.png")
btnOpen=Button(menuFrame, image=open_img, command=openNote, **button_style)
btnOpen.grid(row=0, column=1, padx=5, pady=5)
btnOpen.bind("<Enter>", on_enter)
btnOpen.bind("<Leave>", on_leave)

save_img=load_icon("icon/save.png")
btnSave=Button(menuFrame, image=save_img, command=saveNote, **button_style)
btnSave.grid(row=0, column=2, padx=5, pady=5)
btnSave.bind("<Enter>", on_enter)
btnSave.bind("<Leave>", on_leave)

quit_img=load_icon("icon/shutdown.png")
btnQuit=Button(menuFrame, image=quit_img, command=closeNote, **button_style)
btnQuit.grid(row=0, column=3, padx=5, pady=5)
btnQuit.bind("<Enter>", on_enter)
btnQuit.bind("<Leave>", on_leave)

# Modern dropdown style
dropdown_style = {
    'bg': COLORS['button_bg'],
    'activebackground': COLORS['button_hover'],
    'fg': COLORS['text_fg'],
    'relief': 'flat',
    'highlightthickness': 0
}

#font options with modern style
allFonts=font.families()
fontFamily=StringVar()
fontOption=OptionMenu(menuFrame, fontFamily, *allFonts, command=changeFont)
fontFamily.set("Arial")
fontOption.config(width=20, **dropdown_style)
fontOption.grid(row=0, column=4, padx=5, pady=5)

#size options
sizes=[8,12,18,25,36,42,50]
fontSize=IntVar()
sizeOption=OptionMenu(menuFrame, fontSize, *sizes, command=changeFont)
fontSize.set(12)
sizeOption.config(width=5, **dropdown_style)
sizeOption.grid(row=0, column=5, padx=5, pady=5)

#style options
styles=["none","bold","italic"]
fontStyle=StringVar()
styleOption=OptionMenu(menuFrame, fontStyle, *styles, command=changeFont)
fontStyle.set("none")
styleOption.config(width=10, **dropdown_style)
styleOption.grid(row=0, column=6, padx=5, pady=5)

#scroll text with modern style
myFont=(fontFamily.get(), fontSize.get())
textArea=scrolledtext.ScrolledText(
    textFrame,
    bg=COLORS['text_bg'],
    fg=COLORS['text_fg'],
    font=myFont,
    insertbackground=COLORS['text_fg'],  # สีของเคอร์เซอร์
    selectbackground=COLORS['accent'],    # สีของข้อความที่ถูกเลือก
    selectforeground=COLORS['text_fg'],
    relief='flat',
    padx=10,
    pady=10
)
textArea.pack(fill=BOTH, expand=True)

root.mainloop()