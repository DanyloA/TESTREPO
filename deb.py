from tkinter import*
from tkinter.colorchooser import askcolor
class Paint(object):
    PEN_SIZE=5.0
    PEN_color='black'
    def init(self):
        self.window=Tk()
        self.stack = []
        self.pencil=Button(self.window, text='ОЛІВЕЦЬ',command=self.click_pencil)
        self.pencil.grid(row=0,column=0)
        self.lastyk=Button(self.window, text='CТИРАЧКА',command=self.click_lastyk)
        self.lastyk.grid(row=0,column=1)
        self.color=Button(self.window, text='КОЛІР1',command=self.click_color)
        self.color.grid(row=0,column=2)
        
        self.color=Button(self.window, text='КОЛІР2',command=self.click_color1)
        self.color.grid(row=0,column=3)
        
        self.color=Button(self.window, text='UNDO',command=self.click_undo)
        self.color.grid(row=0,column=5)
       

        self.pen_width=Scale(self.window,from_=1,to=20,orient=HORIZONTAL)
        self.pen_width.grid(row=0,column=4)

        self.c=Canvas(self.window,width=700,height=700,bg='white')
        self.c.grid(row=1,columnspan=4)

        self.options()
 
        self.window.mainloop()
    def options(self):
        self.old_x=None
        self.old_y=None
        self.width_line=self.PEN_SIZE
        self.choosen_color=self.PEN_color
        self.lastyk_on=False
        self.active_button=self.pencil
        self.c.bind("<B1-Motion>",self.paint1)
        self.c.bind("<B3-Motion>",self.paint2)
        self.c.bind("<ButtonReleaase-1>",self.release)
    def release(self,event):
        self.old_x=None
        self.old_y=None
    def paint1(self,event):
        self.width_line=self.pen_width.get()
        paint_color="white"if self.lastyk_on else self.choosen_color
        if self.old_x and self.old_y:
            z =self.c.create_line(self.old_x,self.old_y,event.x,event.y,width=self.width_line,fill=paint_color,capstyle=ROUND,smooth=TRUE)
#           self.c.create_line(self.old_x,self.old_y,event.x,event.y,width=self.width_line,fill=paint_color,capstyle=ROUND,smooth=TRUE)
            self.stack.append(z)
        
        self.old_x=event.x
        self.old_y=event.y
        
    def paint2(self,event):
        self.width_line=self.pen_width.get()
        paint_color="white"if self.lastyk_on else self.choosen_color1
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,event.x,event.y,width=self.width_line,fill=paint_color,capstyle=ROUND,smooth=TRUE)
        self.old_x=event.x
        self.old_y=event.y
    def click_pencil(self):
        self.activate_button(self.pencil)
    def click_color(self):
        self.lastyk_on=False
        self.choosen_color=askcolor(color=self.choosen_color)[1]

    def click_color1(self):
        self.lastyk_on=False
        self.choosen_color1=askcolor(color=self.choosen_color)[1]
        
    def click_lastyk(self):
        self.activate_button(self.lastyk,lastyk_model=True)
        
    def activate_button(self,button,lastyk_model=False):
        self.active_button.config(relief=RAISED)
        button.config(relief=SUNKEN)
        self.active_button=button
        self.lastyk_on=lastyk_model

    def click_undo(self):
        x = self.stack.pop()
        self.c.delete(x) 
        
Paint()
