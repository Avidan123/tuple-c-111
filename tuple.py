from tkinter import *

root=Tk()
root.title("tuple")
root.geometry("800x800")

months=("january","february","march","april","may","june","july","august","september",
        "october","november","december")
profit=(63753,54637,48265,46782,29763,46735,29384,29837,27864,19238,28734,98234)

max_profit=Label(root)
max_profit.place(relx=0.5,rely=0.1,anchor=CENTER)

min_profit=Label(root)
min_profit.place(relx=0.5,rely=0.2,anchor=CENTER)

def max_p():
    p=max(profit)
    max_index=profit.index(p)
    max_month=months[max_index]
    max_profit["text"]="month of maximum profit="+max_month+"  and profit of the month is "+str(p)
    
def min_p():
    pmin=min(profit)
    pmin_index=profit.index(pmin)
    min_month=months[pmin_index]
    min_profit["text"]="minimum profit month=  "+min_month+"  and profit is=  "+str(pmin)

btn1=Button(root,text="press to know max profit",command=max_p)
btn1.place(relx=0.5,rely=0.3,anchor=CENTER)

btn2=Button(root,text="press for minimum profit month and profit value ",command=min_p)
btn2.place(relx=0.5,rely=0.4,anchor=CENTER)

root.mainloop()



