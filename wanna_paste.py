 def perf_code():
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
