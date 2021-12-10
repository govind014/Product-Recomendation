from ui import *
import threading
import time

REAL_USER = True


class DialogueManager(threading.Thread):

    def __init__(self, window):
        if REAL_USER:
            self.ui = Ui(window)
            threading.Thread.__init__(self)
            self.ui.messages.insert(END, "BOT : Hello, how may I help you?")
            self.ui.messages.insert(END, ".")
            self.ui.entryField.focus()
        # self.successCounter = 0
        self.done = False
        self.Run()

    def Run(self):
        self.GetUserAction()
        while not self.done:
            #self.Step()
            self.ui.messages.insert(END, ".")
            self.GetUserAction()
            

    def GetUserAction(self):
        # Get user utterance in UI
        userUtterance = ''
        while not userUtterance:
            userUtterance  = self.ui.GetUserInput()
            self.ui.window.update()
        time.sleep(0.1)


# Define window
window = Tk()
dm = DialogueManager(window)
if REAL_USER:
	window.mainloop()