from tkinter import *
from entitySelection import *

#model = SequenceTagger.load('H:\\Product-Recomendation\\custom-ner-models\\Flair\\custom-ner\\best-model-2.pt')


class Ui:
    def __init__(self, window):
        self.customNER = CustomNER()
        self.window = window
        self.InitUi()

    def InitUi(self):
        self.window.title("Product Recomendation Chatbot")
        self.window.resizable(width=FALSE, height=FALSE)

        #Main space where the messages are shown
        self.messagesFrame = Frame(self.window, bd=1, relief="sunken", background="white")
        self.messagesFrame.pack(padx=15, pady=(15,0), fill=None, expand=False)
        self.messages = Listbox(self.messagesFrame, height=30, width=90, borderwidth=0, highlightthickness=0, 
                                font='SF-Pro-Display', background=self.messagesFrame.cget("background"))
        self.messages.pack(pady=5, padx=5)
        self.messages.insert(END, ".")
        self.messages.insert(END, "CUSTOM NER")
        self.messages.insert(END, ".")
        self.messages.insert(END, ".")

        self.userMessage = StringVar()
        self.userMessageSent = StringVar()
        #Box where the user can type input
        self.entryField = Entry(self.window, width=80, textvariable=self.userMessage, font='SF-Pro-Display')
        self.entryField.pack(padx=10, pady=(15, 20))
        #Send text when user hits enter key
        self.entryField.bind("<Return>", self.SendUserMessage)
        #Render the elements
        self.window.update()

	#Checks for user input
    def GetUserInput(self):
        #print("GetUserInput")
        if self.userMessageSent.get():	
            print("GetUserInput")
            utterance = self.userMessageSent.get()
            self.userMessageSent.set('')
            print(utterance)
            result = self.customNER.entitySelection(utterance)
            #self.SendAgentMessage(result)
            self.convertString(result)
            return utterance

    def SendUserMessage(self, event):
        #print("SendUserMessage")
        if self.userMessage.get():
            self.messages.insert(END, '\n' + "YOU : " + self.userMessage.get())
            self.userMessageSent.set(self.userMessage.get())
            self.userMessage.set('')
            #self.GetUserInput()
            #self.SendAgentMessage("OK")
    
    def convertString(self, input_):
        self.messages.insert(END, ".")
        for key in input_.keys():
            outputString = ''
            #print(key, input_[key])
            outputString += (str(key) + " : ")
            for value in input_[key]:
                outputString += (str(value) + " ")
            print(outputString)
            self.SendAgentMessage(outputString)

    def SendAgentMessage(self, agentMessage):
        self.messages.insert(END, '\n' + ">>>>>>>>>>>>> " + str(agentMessage) )
