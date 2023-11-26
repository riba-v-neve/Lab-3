import tkinter as tk
import pygame
from random import choice, shuffle

#funcions
def block_generation():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    random_list = []
    for i in range(2):
        random_list.append(choice(numbers))
    for i in range(3):
        random_list.append(choice(letters))
    shuffle(random_list)
    return(random_list)
           
def key_gereration():
    key = ''
    for i in range(3):
        block = block_generation()
        for i in range(5):
            key += block[i]
        key += '-'
    print_key.configure(text=key[:-1])

def close():
    window.destroy()


window = tk.Tk()
window.title('The Last Of Us KeyGen')

# the location of the window and its dimensions
width = 600
height = 400
screenwidth = window.winfo_screenwidth() 
screenheight = window.winfo_screenheight()
x = (screenwidth/2) - (width/2)
y = (screenheight/2) - (height/2)

window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(width=False, height=False)

# background
background = tk.PhotoImage(file = 'the_last_of_us_bg.png')
label1 = tk.Label(window, image = background) 
label1.place(x = -2, y = -1) 

# music
pygame.mixer.init()

def play():
    pygame.mixer_music.load('The_Last_of_Us_-_Theme_8bit.wav')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops = -1)

play()

# buttons and text
print_key = tk.Label(window, text='XXXXX-XXXXX-XXXXX', font=("Arial Bold", 15))
print_key.place(anchor='center', x=445, y=140)

generate_button = tk.Button(window, text='Generate a key', command=key_gereration, cursor='hand2')
generate_button.place(x=400, y=180)

close_button = tk.Button(window, text='Close', command=close, cursor='hand2')
close_button.pack(expand=True, anchor='se', padx=20, pady=20)

window.mainloop()