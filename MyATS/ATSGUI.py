import tkinter as tk
from tkinter import filedialog
from MyATS import ATSSimulator
class ATSGUI:
    def __init__(self,root):
        self.root=root
        self.root.title("MyATS")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.label = tk.Label(self.root, text="MyATS",font=("Arial", 20,"bold"))
        self.label.pack(pady=10)
        self.upload_btn=tk.Button(root, text="Upload Resume ", command=self.upload_file, font=("Arial", 15))
        self.upload_btn.pack(pady=10)
        self.result_label=tk.Label(self.root, text="",font=("Arial", 15), fg="blue")
        self.result_label.pack(pady=10)
        self.root.mainloop()
    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files","*.*")])
        if file_path:
            self.result_label.config(text="Scanning")
            self.root.update()
            simulator = ATSSimulator(file_path)
            match_count=simulator.simulate()
            if isinstance(match_count, str) and "Error" in match_count:
                self.result_label.config(text=match_count, fg="red")
            elif match_count >= 5:
                self.result_label.config(text="Under Review", fg="green")
            else:
                self.result_label.config(text="Application Rejected", fg="red")



