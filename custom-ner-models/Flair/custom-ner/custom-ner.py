
from UserInterface import*
import threading


class DialogueManager(threading.Thread):

    def __init__(self, window):
        self.ui = Ui(window)
        threading.Thread.__init__(self)
        self.ui.messages.insert(END, "Bot : Hello, how may I help you?")
        self.ui.entryField.focus()

        while 1:
            input = self.ui.GetUserInput()
            self.ui.window.update()




if __name__ == "__main__":

    window = Tk()
    dm = DialogueManager(window)
    window.mainloop()
