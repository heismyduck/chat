import tkinter as tk
from tkinter import scrolledtext

def insertHistory(hisMsgEntry):
    mytext = """Some text
            Some more text
            etc...
            Trump has been using Save America to pay for his legal bills, which have added up to $40 million so far this year, according to The Washington Post. The PAC, which had been set up in the days after the November 2020 election when Trump was raising money off of baseless election claims, had shelled out $16 million for legal fees in 2021 and 2022 combined.

Already indicted in New York for allegedly falsifying business records and in Florida over his alleged mishandling of classified documents at his Mar-a-Lago estate once out of office, Trump could soon face further indictments resulting from Special Counsel Jack Smith’s Jan. 6 investigation and from Fulton County, Georgia District Attorney Fanni Willis’ probe into his efforts of overturn that state’s 2020 election results.

It is unclear which PAC received the $60 million, and how much of it was ultimately refunded, if any.

As Rolling Stone reported last week, Trump is having trouble convincing lawyers to take up his defense ahead of a likely Jan. 6-related indictment. The reasons are multiple: the risk of lawyers themselves becoming mired in legal jeopardy, the feeling that Trump’s loss in a case brought in Washington, D.C. is inevitable, and the reputational harm that Trump would cause firms.

Trump does not currently have a legal defense fund. The Times, citing people who have heard the former president discuss the matter, reports that he has told those close to him that only the guilty establish such funds.

During a grievance-filled rally in Erie, Pennsylvania on Saturday, Trump claimed he’d use his own money """
    #hisMsgEntry.insert(tk.INSERT,mytext)
    # hisMsgEntry.insert(1.0, " in ScrolledText")
    # print(hisMsgEntry.get(1.0, tk.END))


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

topFrame = tk.Frame(window2_main, width = appScreen_width * 0.95, height = appScreen_height * 0.8)
bottomFrame = tk.Frame(window2_main, width = appScreen_width * 0.95, height = appScreen_height * 0.15)#, background="red")
topFrame.pack(pady=5)
bottomFrame.pack(pady=1, side=tk.BOTTOM)

hisMsgEntry = scrolledtext.ScrolledText(topFrame, wrap=tk.WORD, height=32)
# hisMsgEntry.config(state='disabled')
insertHistory(hisMsgEntry)
hisMsgEntry.pack(padx=10, pady=3)

#print(bottomFrame.winfo_width())
msgEntry = tk.Entry(bottomFrame, width=45)
msgEntry.grid(row=0, column=0)
# msgEntry2 = scrolledtext.ScrolledText(bottomFrame, width=30, height=2,wrap=tk.WORD, vbar=False)
# msgEntry2.grid(row=0,column=0)


sendButton = tk.Button(bottomFrame, text="Send", bg="red", fg='blue',pady=2, padx=2)
sendButton.grid(row=0, column=1)
# bottomFrame.grid_columnconfigure(0, weight=1)

window2_main.mainloop()

