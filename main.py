import customtkinter
from threading import Thread
import time
from bot_scripts.main import gather_fish
# def start_fishing():
#   thread = Thread(target=gather_fish, args=(True,)) 
#   thread.start()

# def stop_fishing():
#   thread = Thread(target=gather_fish, args=(False,)) 



def start_fish_script():
    Thread(target=gather_fish, args=(True,)).start()


if __name__ == "__main__":
  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("green")

  root = customtkinter.CTk()
  root.geometry("500x350") 
  root.title("Traianik Majestic Fish Bot")

  frame = customtkinter.CTkFrame(master=root)
  frame.pack(pady=20,padx=60,fill="both", expand=True)


  label = customtkinter.CTkLabel(master=frame, text="Majestic Fish Bot")
  label.pack(pady=12, padx=10)

  # entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
  # entry1.pack(pady=12, padx=10)

  # entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password")
  # entry2.pack(pady=12, padx=10) 

  start_btn = customtkinter.CTkButton(master=frame, text="Start Fish Bot", command=start_fish_script)
  start_btn.pack(pady=5, padx=10)

  # start_btn = customtkinter.CTkButton(master=frame, text="Start Fish Bot", command=lambda: Thread(target=gather_fish, args=(True,)).start()) 
  # start_btn.pack(pady=12, padx=10)

  label = customtkinter.CTkLabel(master=frame, text='To stop the bot hold "Q"!')
  label.pack() 

  root.mainloop()