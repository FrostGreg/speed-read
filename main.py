import tkinter as tk
from tkinter import ttk
from time import sleep
class display:
    def __init__(self, root):
        self.root = root
        self.text = tk.Entry(root)
        self.text.grid(row=1, column=1)

        self.word = tk.Label(root, text="")
        self.word.grid(row=2, column=1)

        self.submit = tk.Button(root, text="submit", command=self.submit_action)
        self.submit.grid(row=3, column=1)

    def submit_action(self):
        user_in = self.text.get()
        arr = user_in.split()
        for word in arr:
            self.word.configure(text=word)
            self.root.update()
            sleep(0.3)



def main():
    root = tk.Tk()
    root.geometry("320x500")
    root.title("Speed Read")
    newDisplay = display(root)
    root.mainloop()


if __name__ == '__main__':
    main()

