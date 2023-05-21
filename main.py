import tkinter as tk
import time

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter by Maksym Kashuba")
        self.X = 620
        self.Y = 520
        self.N = 62
        self.M = 11
        self.counter = 0
        self.state = False

        self.create_widgets()
        self.configure_window()

    def setCounter(self, counter):
        self.counter = counter
        print("counter", self.counter)
        self.on_scale_change(self.counter)
    def create_widgets(self):
        self.counter_label = tk.Label(self, text='0', font=('Arial', 32), width=10, height=2, bg='white')
        self.threshold_label = tk.Label(self, text=f'Threshold: {self.M}', font=('Arial', 16), width=20, height=1, bg='white')
        self.state_label = tk.Label(self, text=f'State: {self.state}', font=('Arial', 16), width=10, height=1, bg='white')
        self.action_listbox = tk.Listbox(self, font=('Arial', 12), width=62, height=5)
        self.newValue = tk.DoubleVar()
        self.newValue.set(self.counter)
        self.scale = tk.Scale(self, from_=0, to=self.N, bg="pink", font=('Helvetica 15'),
                           variable=self.newValue, command=self.on_scale_change, length=300)
        #   self.scale = tk.Scale(self, from_=0, to=self.N, orient=tk.HORIZONTAL, length=300, showvalue=0, command=self.on_scale_change)
        self.button = tk.Button(self, text='Click me', font=('Arial', 16), width=10, height=2, command=self.on_button_click)
        self.entry = tk.Entry(self, font=('Arial', 16), width=5)
        self.entry.insert(tk.END, str(self.M))
        self.entry_button = tk.Button(self, text='Submit', font=('Arial', 16), width=8, height=1, command=self.on_entry_submit)

        self.counter_label.place(x=50, y=50)
        self.scale.place(x=50, y=200)
        self.threshold_label.place(x=60, y=165)
        self.state_label.place(x=400, y=250)
        self.button.place(x=400, y=50)
        self.entry.place(x=400, y=150)
        self.entry_button.place(x=500, y=150)
        self.action_listbox.place(x=50, y=300)

    def configure_window(self):
        self.geometry(f'{self.X}x{self.Y}')
        self.resizable(False, False)

    def on_button_click(self):
        self.counter += 1
        self.state = not self.state
        self.counter_label.config(text=str(self.counter))
        self.state_label.config(text=f'State: {self.state}')
        if self.counter >= self.M:
            self.counter_label.config(bg='red')
        else:
            self.counter_label.config(bg='white')
        self.action_listbox.insert(tk.END, f'{time.ctime()} - Counter value: {self.counter} - Changed by Button - State: {self.state}')

    def on_scale_change(self, value):
        self.scale.set(self.counter)
        self.counter = int(value)
        self.counter_label.config(text=str(self.counter))
        if self.counter >= self.M:
            self.counter_label.config(bg='red')
        else:
            self.counter_label.config(bg='white')
        self.action_listbox.insert(tk.END, f'{time.ctime()} - Counter value: {self.counter} - Changed by Scale - State: {self.state}')

    def on_entry_submit(self):
        self.M = int(self.entry.get())
        self.threshold_label.config(text=f'Threshold: {self.M}')
        self.action_listbox.insert(tk.END, f'{time.ctime()} - Threshold value: {self.M} - Changed by Entry - State: {self.state}')

    def run(self):
        self.mainloop()