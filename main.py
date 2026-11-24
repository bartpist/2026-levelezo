import tkinter as tk
from bi_system import BiSystemInfo

def refresh_event(event=None):
    app.refresh()
    top_text.set(app.top_banner())
    info_list.delete(0, tk.END)
    for line in app.detail_lines():
        info_list.insert(tk.END, line)

def save_event():
    app.save_to_file()
    top_text.set(f"Report saved to system_report.txt (ID: #{app.check_id})")

app = BiSystemInfo()
root = tk.Tk()
root.title("Bi-System Checker")
root.geometry("500x260")

top_text = tk.StringVar()
top_text.set("Initializing")

top_label = tk.Label(root, textvariable=top_text)
top_label.pack(pady=10)

info_list = tk.Listbox(root, width=56, height=6)
info_list.pack(pady=6)

button_frame = tk.Frame(root)
button_frame.pack(pady=8)

refresh_button = tk.Button(button_frame, text="Refresh System Info", command=refresh_event)
refresh_button.pack(side=tk.LEFT, padx=8)

save_button = tk.Button(button_frame, text="Save System Info", command=save_event)
save_button.pack(side=tk.LEFT, padx=6)
root.bind("<Return>", refresh_event)

refresh_event()
root.mainloop()