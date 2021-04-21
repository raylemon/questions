import tkinter as tk


def on_select(event: tk.Event):
    sv_label.set(
        f"{event.widget.curselection()} - {event.widget.get(lst.curselection())}"
    )


window = tk.Tk()
sv_list = tk.StringVar(value=[{"f_name": "toto", "l_name": "toto"}])
sv_label = tk.StringVar()

box = tk.Frame(window)
lst = tk.Listbox(
    box, selectmode="single", listvariable=sv_list, exportselection=False
)  # browse, single, multiple, extended
lst.pack(side="left", fill="y")

scroll = tk.Scrollbar(box, orient="vertical")
scroll.pack(side="right", fill="y")

box.pack(expand="yes", fill="y")
label = tk.Label(window, textvariable=sv_label)
label.pack()

lst.bind("<<ListboxSelect>>", on_select)
lst.config(yscrollcommand=scroll.set)
scroll.config(command=lst.yview)

if __name__ == "__main__":
    window.mainloop()
