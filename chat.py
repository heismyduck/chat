import tkinter as tk
import socket

## hello
def start():
    main = tk.Tk()
    main.title("Chat App")

    appScreen_width = 250
    appScreen_height = 300
    
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    
    main.minsize(appScreen_width,appScreen_height)
    main.maxsize(appScreen_width,appScreen_height)
    
    windowLocated = str(screen_width) + "x" + str(screen_height) + "+"+ str(screen_width//2 - appScreen_width//2) + "+" + str(screen_height//2 - appScreen_height//2)
    main.geometry(windowLocated)

    nameFrame = tk.Frame(main)
    nameFrame.pack(padx=10,pady=10)
    nameLabel = tk.Label(nameFrame, text="Name", pady=5)
    nameLabel.pack()
    nameE = tk.Entry(nameFrame, bd =2)
    nameE.pack()
    nameE.focus()
    nameE.bind("<FocusIn>", handleFocus)
    nameE.bind("<Enter>", handleEnter)

    #nameError = tk.Label(nameFrame, text="asdsad", fg='red', font=("Arial",10))
    #nameError.pack()

    addressFrame = tk.Frame(main)
    addressFrame.pack(padx=10,pady=10)
    addressLabel = tk.Label(addressFrame, text="Address", pady=5)
    addressLabel.pack()
    addressE = tk.Entry(addressFrame, bd =2)
    addressE.pack()
    addressE.bind("<FocusIn>", handleFocus)

    portFrame = tk.Frame(main)
    portFrame.pack(padx=10,pady=10)
    portLabel = tk.Label(portFrame, text="Port", pady=10)
    portLabel.pack()
    portE = tk.Entry(portFrame, bd =2)
    portE.pack()
    portE.bind("<FocusIn>", handleFocus)

    buttonFrame = tk.Frame(main)
    buttonFrame.pack(padx=10,pady=10)
    #B = tk.Button(buttonFrame, text ="Submit", pady=2, command=lambda:get_data(nameE.get(), addressE.get(), portE.get()))
    B = tk.Button(buttonFrame, text ="Submit", pady=2, command=lambda:get_data2(nameE, addressE, portE, main))
    B.pack()

    main.mainloop()


# Define a function to return the Input data
def get_data(name, ipAddress, portNumber):
    if len(name) == 0: print("name is zero")
    if len(ipAddress) == 0: print("ipAddress is zero")
    if len(portNumber) == 0: print("portNumber is zero")
    print(f"{name},{ipAddress},{portNumber}")


def get_data2(name, address, port, main):
    #name.config(bg='grey')
    hasInput = True
    n = name.get()
    a = address.get()
    p = port.get()
    if len(n) == 0: 
        print("name is zero")
        name.config(bg='#ff3333')
        hasInput = False

    if len(a) == 0: 
        print("address is zero")
        address.config(bg='#ff3333')
        hasInput = False
    
    if len(p) == 0: 
        print("port is zero")
        port.config(bg='#ff3333')
        hasInput = False

    if not hasInput: return

    if verify(name, address, port):
        window2(main)
    #print(f"{n},{a},{p}")

def verify(name, address, port):
    checkServer(address,port)
    return False

def handleFocus(event):
    print(event.widget.config(bg='white'))
    print(event)


def handleEnter(event):
    print(event.widget.config(bg='white'))
    print(event)

def window2(main):
    main.destroy()
    window2_main = tk.Tk()
    window2_main.title("Chat App")
    appScreen_width = 500
    appScreen_height = 500
    
    screen_width = window2_main.winfo_screenwidth()
    screen_height = window2_main.winfo_screenheight()
    
    window2_main.minsize(appScreen_width,appScreen_height)
    window2_main.maxsize(appScreen_width,appScreen_height)
    
    windowLocated = str(screen_width) + "x" + str(screen_height) + "+"+ str(screen_width//2 - appScreen_width//2) + "+" + str(screen_height//2 - appScreen_height//2)
    window2_main.geometry(windowLocated)
    connectToServer('127.0.0.1',12345)
    window2_main.mainloop()

def checkServer(address, port):
    s = socket.socket()  
    s.settimeout(3)   # 5 seconds
    try:
        s.connect((address.get(), int(port.get())))         # "random" IP address and port
        if s.recv(1024).decode() != 'SUCCESS':
            print("invaild")
            return False
        ## TO do
        print("vaild")
        s.close()
        return True
    except socket.error:
        print("connect failed", socket.error)
        
    
    return False

def connectToServer(address, port):
    s = socket.socket()  
    s.connect((address, port))
    print (s.recv(1024).decode())
    # close the connection
    s.close()

start()
