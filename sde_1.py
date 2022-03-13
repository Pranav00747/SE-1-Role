from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import time

class pet_pooja_app:
 def internal_comp(par):
   top1 = Canvas(par, bg='#ffffff', width=par.winfo_screenwidth(), height=80)
   top1.place(x=0, y=0)
   def get_img(name):
     img = Image.open(name)
     img = img.resize((128, 36))
     global img1
     img1 = ImageTk.PhotoImage(img)
     return img1
   top1.create_image(120, 40, image=get_img('petpooja.png'))
   lab1 = Label(text='Pet Pooja', bg='#ffffff', fg='#b51908', font=('Bauhaus 93', 26))
   lab1.place(x=366, y=26)
   def m_e(e):
     lab1.config(font=('Bauhaus 93', 28))
   def m_o(e):
     lab1.config(font=('Bauhaus 93', 26))
   lab1.bind('<Enter>', m_e)
   lab1.bind('<Leave>', m_o)
   ocan1 = Canvas(par, bg='#13700c', width=par.winfo_screenwidth()-100, height=400)
   ocan1.place_forget()
   l1 = Label(ocan1, text='Name', bg='#13700c', fg='#ffffff', font=('Arial', 8))
   l1.place(x=10, y=10)
   l2 = Label(ocan1, text='Address', bg='#13700c', fg='#ffffff', font=('Arial', 8))
   l2.place(x=10+60, y=10)
   l3 = Label(ocan1, text='Food Item', bg='#13700c', fg='#ffffff', font=('Arial', 8))
   l3.place(x=10+120, y=10)
   l4 = Label(ocan1, text='Restuarent', bg='#13700c', fg='#ffffff', font=('Arial', 8))
   l4.place(x=10+180, y=10)
   l5 = Label(ocan1, text='Status', bg='#13700c', fg='#ffffff', font=('Arial', 8))
   l5.place(x=10+240, y=10)

   fcan1 = Canvas(par, bg='#b51908', width=par.winfo_screenwidth()-100, height=400)
   fcan1.place_forget()
   ll1 = Label(fcan1, text='Food Item', bg='#b51908', fg='#ffffff', font=('Arial', 8))
   ll1.place(x=10, y=10)

   order = Label(par,text='Order', width=6, height=2, bg='#13700c', fg='#ffffff', font=('Arial', 10), highlightthickness=1)
   order.place(x=200, y=100)
   menu = Label(par,text='Menu', width=6, height=2, bg='#b51908', fg='#ffffff', font=('Arial', 10), highlightthickness=1)
   menu.place(x=366, y=100)
   def o_e(e):
      time.sleep(0.2)
      order.config(bg='#ffffff', fg='#13700c')
   def o_l(e):
      time.sleep(0.2)
      order.config(bg='#13700c', fg='#ffffff')
   def o_c(e):
       fcan1.place_forget()
       ocan1.place(x=60, y=200)

   order.bind('<Enter>', o_e)
   order.bind('<Leave>', o_l)
   order.bind('<Button-1>', o_c)
   def m_e(e):
     time.sleep(0.2)
     menu.config(bg='#ffffff', fg='#13700c')
   def m_l(e):
      time.sleep(0.2)
      menu.config(bg='#b51908', fg='#ffffff')
   def m_c(e):
      ocan1.place_forget()
      fcan1.place(x=60, y=200)

   menu.bind('<Enter>', m_e)
   menu.bind('<Leave>', m_l)
   menu.bind('<Button-1>', m_c)
   btn_close = Label(top1, text="x", bg='#ffffff', fg='#434441', font=('Arial', 12))
   btn_close.place(x=par.winfo_screenwidth()-60, y=4)
   def btn_e(e):
     btn_close.config(fg='#b51908')
     btn_close.config(font=('Arial', 14))
   def btn_l(e):
    btn_close.config(fg='#434441')
    btn_close.config(font=('Arial', 12))
   def btn_clk(e):
    par.destroy()
   btn_close.bind('<Enter>', btn_e)
   btn_close.bind('<Leave>', btn_l)
   btn_close.bind('<Button-1>', btn_clk)
   """
   dat1 = getmenus()
   dat2 = getorders()
   x1=0
   y1=0
   z1=0
   for xx in dat2:
    for yy in xx:
      lab_o = Label(ocan1, text=yy, bg='#13700c', fg='#ffffff', font=('Arial', 8))
      lab_o.place(x=10+x1, y=30+y1)
      x1 = x1+60
   y1=y1+20
  for zz in dat1:
     lab_f = Label(fcan1, text=zz, bg='#b51908', fg='#ffffff', font=('Arial', 8))
     lab_f.place(x=10, y=30+z1)
     z1=z1+20
  """
 def init_ui():
   tt = Tk()
   tt.geometry(('%dx%d')%(tt.winfo_screenwidth(), tt.winfo_screenheight()))
   tt.title("Pet Pooja Restuarent")
   tt.overrideredirect(1)
   tt.configure(bg='#434441')
   return tt

if __name__=="__main__":
 ppa = pet_pooja_app
 par_m = ppa.init_ui()
 ppa.internal_comp(par_m)
 par_m.mainloop()

   