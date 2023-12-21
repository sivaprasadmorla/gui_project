from tkinter import *
import pyautogui as pag
from threading import *
import time

window=Tk()
window.title("Auto Messenger")

class Automessenger(Thread):
    hmt_c=0
    wt_c=0.0
    msg_c=""

    def run(self):
        i=1
        while True:
            time.sleep(self.wt_c)
            pag.typewrite(self.msg_c)
            pag.press("enter")
            if self.hmt_c ==i:
                break
            i+=1

            


def messenger(ht,wt,msg):
    send=Automessenger()
    send.hmt_c=int(ht)
    send.wt_c=float(wt)
    send.msg_c=msg
    send.daemon=True  # if our application is closed then working in the other application will close by using the "daemon"
    send.start()




hmt_msg=Label(text="How many times:" ,font=('arial',14))
hmt_msg.grid(row=0,column=0,padx=10,pady=10)

hmt_input=Entry(window,width=10)
hmt_input.grid(row=0,column=1,padx=2,pady=10)

after_hmt=Label(window,text="times (0 to infinite times)",font=("Arial",10))
after_hmt.grid(row=0,column=2,pady=10)

wt_msg=Label(window,text="Waiting time:",font=("Arial",14))
wt_msg.grid(row=1,column=0,padx=10,pady=10,sticky=E)

wt_input=Entry(window,width=10)
wt_input.grid(row=1,column=1,padx=2,pady=10)

after_wt=Label(window,text="seconds",font=("Arial",10))
after_wt.grid(row=1,column=2,pady=10,sticky=W)

msg=Label(window,text="Message:",font=("arial",14))
msg.grid(row=2,column=0,padx=10,pady=20,sticky=E)

msg_input=Entry(window,width=30)
msg_input.grid(row=2,column=1,padx=2,pady=20,columnspan=2,sticky=W)

msg_button=Button(window,text="Send",font=("arial",12),command=lambda:messenger(hmt_input.get(),wt_input.get(),msg_input.get()))
msg_button.grid(row=3,column=2)


window.mainloop()