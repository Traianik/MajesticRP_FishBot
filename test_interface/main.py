import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk() 
root.geometry("500x350")

def login():
    print('Test')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Majestic Bot Interface")
label.pack(pady=12, padx=10)

# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# entry1.pack(pady=12, padx=10)

# entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password")
# entry2.pack(pady=12, padx=10)

start_btn = customtkinter.CTkButton(master=frame, text="Start Fish Bot", command=gather_fish())
start_btn.pack(pady=12, padx=10)

root.mainloop()