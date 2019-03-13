import tkinter as tk

gui = tk.Tk()
gui.title("blarg")
text = tk.Text(gui)
# Insert some text
text.insert(tk.INSERT, "blarg1 ")
text.insert(tk.END, " blarg2 ")
text.insert(tk.END, "blarg3 ")
text.insert(tk.END, "blarg4 ")
text.pack()
# Create some tags
text.tag_add("one", "1.0", "1.8")
text.tag_add("two", "1.10", "1.20")
text.tag_add("three", "1.21", "1.28")
text.tag_add("four", "1.29", "1.36")
#Configure the tags
text.tag_config("one", background="yellow", foreground="blue")
text.tag_config("two", background="black", foreground="green")
text.tag_config("three", background="blue", foreground="yellow")
text.tag_config("four", background="red", foreground="black")
#Start the program
gui.mainloop()