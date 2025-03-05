from tkinter import *
import base64

root=Tk()
root.geometry('500x500')
root.title('Message Cipher by Shivani Chitikesi')

Label(root, text ='ENCODE DECODE', font = 'arial 20 bold').pack()
Label(root, text ='DataFlair', font = 'arial 20 bold').pack(side =BOTTOM)

text=StringVar()
private_key=StringVar()
mode=StringVar()
result=StringVar()

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c=key[i%len(key)]
        enc.append(chr((ord(message[i])+ord(key_c))%256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message=base64.urlsafe_b64encode(message).decode()
    for i in range(len(message)):
        key_c=key[i%len(key)]
        dec.append(chr((ord(message[i])-ord(key_c))%256))

    return "".join(dec)

def Mode():
    if(mode.get()=='e'):
        result.set(Encode(private_key.get(),text.get()))
    elif(mode.get()=='d'):
        result.set(Decode(private_key.get(),text.get()))
    else:
        result.set('invalid mode')

def Reset():
    text.set("")
    private_key.set("")
    mode.set("")
    result.set("")

def Exit():
    root.destroy()

Label(root, text ='Text', font='arial 12 bold').place(x=60,y=60)
Entry(root,font='arial 10 bold', textvariable=text).place(x=260,y=60)

Label(root, text ='Key', font='arial 12 bold').place(x=60,y=90)
Entry(root,font='arial 10 bold', textvariable=private_key).place(x=260,y=90)

Label(root, text ='Mode', font='arial 12 bold').place(x=60,y=120)
Entry(root,font='arial 10 bold', textvariable=mode).place(x=260,y=120)

Entry(root,font='arial 10 bold', textvariable= result).place(x=260,y=150)

Button(root, text ='Result', font='arial 12 bold',command=Mode).place(x=60,y=150)

Button(root, text ='Reset', font='arial 12 bold',command=Reset).place(x=60,y=210)

Button(root, text ='Exit', font='arial 12 bold',command=Exit).place(x=260,y=210)

root.mainloop()

