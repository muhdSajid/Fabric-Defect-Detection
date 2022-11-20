import os
import tkinter as tk

from PIL import Image

'''
My script is programmed in OOP. I replaced the frames as follows:
frame1 = self.pages[0].frame
frame2 = self.pages[1].frame
frame3 = self.pages[2].frame
frame4 = self.pages[3].frame
frame5 = self.pages[4].frame
frame6 = self.pages[5].frame
'''
 
APP_TITLE = "Fabric Solutions"
MIN_APP_WIDTH = 400
MIN_APP_HEIGHT = 400 
class AppPage(tk.Frame):
     
    def __init__(self, app, page_nr, **kwargs):
        self.app = app
        self.page_nr = page_nr
         
        tk.Frame.__init__(self, app, **kwargs)
        #
        self.image = Image.open(r"C:\Users\ASUS\Downloads\Project-Sajid\Sajid\images (1)\images\pos\11.jpg")
        self.frame = tk.Frame(self)
        self.frame.pack(fill='both', expand=True, padx=0, pady=0)
       # self.background_image = ImageTk.PhotoImage(self.image)
        #self.background.configure(image=self.background_image)
 
             
class Application(tk.Frame):
    NUM_OF_PAGES = 6
    N_TRIALS = 3
    COUNT=-2
   # N_INTERVALS = 2 * N_TRIALS + 1
   # RELAXING_TIME = 2000
   # RESTING_TIME = 2000
   # TASKING_TIME = 2000
   # LABEL_FONT = ("Arial Bold",10)
     
    def __init__(self, app_win):
        self.app_win = app_win
        tk.Frame.__init__(self, app_win)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1) 
        self.pages = list()
                   
        for page_ptr in range(self.NUM_OF_PAGES):
            page = self.create_page_frame(page_ptr)
            #if page_ptr == 1:
             #   page.frame.config(bg='red')
                #tk.Label(page.frame, text='ACTION-1').pack()
           # elif page_ptr == 2:
             #   page.frame.config(bg='green')
                #tk.Label(page.frame, text='ACTION-2').pack(side='left')
            #elif page_ptr == 3:
             #   page.frame.config(bg='blue')
                #tk.Label(page.frame, text='ACTION-3').pack()
            #elif page_ptr == 4:
             #   page.frame.config(bg='black')
                #tk.Label(page.frame, text='RELAXING FINAL').pack()
                 
        self.build_start_page()
        self.show_page(0)


    def build_start_page(self):
        container = self.pages[0].frame
        tk.Label(container, text="Fabric Defect Solution",font=("Arial Bold",60)
            ).pack(padx = 20, pady=20)
        
        #tk.Button(container, text="Train",font=("Arial Bold",20),background="Red",
           # command=self.pyfile).pack(padx=20,pady=30)
 
        tk.Button(container, text="Fabric Testing",font=("Arial Bold",20),background="Orange",
            command=self.pyfile1).pack(padx=10,pady=30)
        
        #tk.Button(container, text="Copy the image path",font=("Arial Bold",20),background="Blue",
           # command=self.pyfile2).pack(padx=10,pady=30)
        
        #tk.Button(container, text="Identify the error type",font=("Arial Bold",20),background="Green",
            #command=self.pyfile3).pack(padx=10,pady=30)
        
         
        tk.Button(container, text="Defect Location",font=("Arial Bold",20),background="Blue",
            command=self.pyfile4).pack(padx=10,pady=20)
 
 
        tk.Button(container, text="Abort",font=("Arial Bold",20),background="Violet",
            command=self.finish).pack(padx=10,pady=30)
             
        container.pack_configure(fill='none', expand=True)
         
    def pyfile(self):
        os.system('python retrain.py')
    def pyfile1(self):
        os.system('python test.py')
    def pyfile2(self):
        os.system('python qadvanced.py')
    def pyfile3(self):
        os.system('python test2ndmod.py')
    def pyfile4(self):
        os.system('python Detections_1.py')
        
    def finish(self):
        self.app_win.withdraw()
        self.app_win.destroy()
     
    def raise_page(self, page_ptr):
       # print(page_ptr)
        self.show_page(page_ptr)
        if page_ptr == 2 and self.COUNT == self.N_INTERVALS:
            self.app_win.after(self.RESTING_TIME, self.raise_page, 4)
        elif page_ptr == 4:
            self.app_win.after(self.RESTING_TIME, self.raise_page, 5)
        elif page_ptr == 1:
            self.app_win.after(self.RELAXING_TIME, self.raise_page, 2)
        elif page_ptr == 2:
            self.app_win.after(self.RESTING_TIME, self.raise_page, 3)
        elif page_ptr == 3:
            self.app_win.after(self.TASKING_TIME, self.raise_page, 4) 
        elif page_ptr == 5:
            self.show_page(0) 
         
    def show_page(self, page_ptr=0):
        self.pages[page_ptr].lift()
                
    def create_page_frame(self, page_ptr):
        page = AppPage(self, page_ptr)
        page.grid(row=0, column=0, sticky='wens')
        self.pages.append(page)
        return page
 
            
def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.minsize(MIN_APP_WIDTH, MIN_APP_HEIGHT)
    app_win.configure(background="black")
    
    
    
    # With title bar
    #app_win.attributes('-zoomed', True)
     
    # Without title bar
    app_win.attributes('-fullscreen', True)
   
   
     
    app = Application(app_win)
    app.pack(fill='both', expand=True)
    app_win.mainloop()
  
  
if __name__ == '__main__':
    main()
