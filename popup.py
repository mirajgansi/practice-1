import tkinter as tk

class PopupWindow:
    root=tk.Tk()
    def __init__(self, master):
        self.master = master
        self.popup = tk.Toplevel(master)
        self.popup.title("Popup Window")
        
        # Example content in the popup window
        label =tk.Label(self.popup, text="This is a pop-up window!")
        label.pack()
        
        # Close button for the popup window
        close_button = tk.Button(self.popup, text="Close", command=self.close_popup)
        close_button.pack()
        
    def close_popup(self):
        self.popup.destroy()
