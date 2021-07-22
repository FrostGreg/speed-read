import tkinter as tk
from time import sleep


class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("350x500")
        self.root.title("Speed Read")

        title = tk.Label(self.root, text="Speed Read", font=("Arial", 25))
        title.grid(row=0, column=0, ipadx=80, ipady=50)

        self.text = tk.Entry(self.root)
        self.text.grid(row=1, column=0)

        self.word = tk.Label(self.root, text="", font=("Arial", 15))
        self.word.grid(row=2, column=0, ipady=50)

        self.submit = tk.Button(self.root, text="submit", command=self.submit_action)
        self.submit.grid(row=3, column=0)

        self.root.mainloop()

    def submit_action(self):
        user_in = self.text.get().split()
        self.text.delete(0, tk.END)
        self.submit.configure(state=tk.DISABLED)
        for word in user_in:
            self.word.configure(text=word)
            self.root.update()
            sleep(0.3)
        self.submit.configure(state=tk.ACTIVE)


if __name__ == '__main__':
    Display()
