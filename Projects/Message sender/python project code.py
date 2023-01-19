import requests  # we are importing this module because it will request the server of the website that we will use.
import json      # we are importing this so that we can store and exchange the data.
from tkinter import*   # to import all the components of tkinter.
from tkinter import messagebox     #import showinfo,showerror

def send_sms(number,message):     # now we are using send_sms() function so that it can send messages. 

#this is the url of  "fast2sms" , it is a online website which sends message .
# we are using this so that we can send message with the help of this website.   
    
    url = "https://www.fast2sms.com/dev/bulk"

 
#now we will create a variable which will actually act as dictionary{'key':'value'} so that it will store the values that is required for sending messages.
    
    
    params={
        'authorization':'G62Q7dqDAlXTpNBb01wgiJnrhPHkUzomLyS4t8cFKIevYfVxRaDM51ZI62Rp48J9wYrcOXte3TvFgsmx', #we taken this value from the website which gives
        # the authorisation of using that website for sending message from our code.
        'sender_id':'FSTSMS',    # this is the default  id that we are using for sending message. 
        'message' : message,     # this will hold the message that the user wants to convey.
        'language' : 'english',  # we have opted english as our lamguage as it is a universal laguage.
        'route' : 'p',           # here we are going for promotional message so written 'p' in value.
        'numbers' : number       # this will hold the mobile numbers to which the user wants to send the message and if we have to send message to more than
                                 # one number then we can use commas for separation between them .e.g. 123456789,4577893426,987654312, etc.
    }



   # now again we will use request module so that url and parameters can be taken in consideration together by using get function which will  pass both url and params .
    response=requests.get(url,params=params) # we have created response variable to know what we will get in return. 
    dic=response.json()     # here with the help of json we will get to know the things stored in it like dictionary.  
    print(dic)
    # we now use this dictionary to know whether our message has been sent or not
    return dic.get('return')  # this will basically return true.

# Creating GUI

#this function is for the button function so that we can call our whole output.
def Btn_click():        
    num=textNumber.get()    # this will work for our number
    msg=textMsg.get("1.0",END) # this will work for our message
    r=send_sms(num,msg)
   # if r==True:
      #  showinfo("Send", "Successfully sent")     # if message is succesfully sent then this will be displayed.
    #else:
       # showrerror("Error","Something went wrong") # if message is not succesfully sent then this will be displayed.
        
root=Tk()     # here we are creating main window by using Tk().
root.title("Message Sender")  # creating title of window .
root.geometry("900x700")      # setting size of window.
font=("times new roman",22,"bold") # setting fontfamily,size abd style.

textNumber=Entry(root,font=font,bg="cyan")  # creating textfield and object named Entry(only one line) under root window with same above font.
textNumber.pack(fill=X,pady=20)   # now we want this to appear it in whole X axis ,that's why we are using fill.

textMsg=Text(root,bg='red')      # here we didn't used Entry because we don't want only one line.
textMsg.pack(fill=X)

sendBtn=Button(root, text="Send",command=Btn_click,bg='blue',fg='white',width=15,height=2)  # we are creating button
sendBtn.pack()

root.mainloop()
