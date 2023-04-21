import tkinter as tk
import random

def display_label_frame():
    head_label_frame.grid(row=0, column=0, padx=25, pady=15)
    body_label_frame.grid(row=1, column=0, padx=25, pady=15)
    foot_label_frame.grid(row=2, column=0, padx=17)

def display_head_widget():
    warrior_label = tk.Label(head_label_frame, text=f'Warrior: {0}', background = '#EED202', foreground= 'white', font = ('Arial Nova' , 14, 'bold') , width= 10, height= 1)
    computer_label = tk.Label(head_label_frame, text=f'{0} :Computer', background = '#EED202', foreground= 'white', font = ('Arial Nova' , 14, 'bold') , width= 10, height= 1)
    space_label = tk.Label(head_label_frame, text = '<-->', foreground= 'white', background= '#EED202')

    warrior_label.grid(row=0, column=0, padx=30)
    computer_label.grid(row=0, column=2, padx=30)
    space_label.grid(row=0, column=1)


def display_body_widget():
    global box, box1, box2, box3, box4, box5, box6, box7, box8, box9
    box = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box.grid(row=0, column=0)
    box1 = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box1.grid(row=0, column=0)
    box2 = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box2.grid(row=0, column=1)
    box3 = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box3.grid(row=0, column=2)
    box4 = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box4.grid(row=1, column=0)
    box5 = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box5.grid(row=1, column=1)
    box6 = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box6.grid(row=1, column=2)
    box7 = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box7.grid(row=2, column=0)
    box8 = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box8.grid(row=2, column=1)
    box9 = tk.Button(body_label_frame, text='', background= '#B03060', font=('Arial Nova', 12, 'bold'), width=7, height=3)
    box1.grid(row=2, column=2)

def display_footer_widget():
    reset = tk.Button(foot_label_frame, text='New Game', background='#EED202', font=('Arial Nova' , 14, 'bold'), width=10, height=1)
    reset.grid(row=0, column=3)

def position_clicked(event):
    player_play(event)

def player_play(box):
    pass

if __name__=='__main__':
    root = tk.Tk()
    root.title('Tiki Warrior')
    root.geometry('450x400')
    root.iconbitmap('tttoe.ico')
    root.resizable(0, 0)
    root.config(background = '#E89362')

    head_label_frame = tk.LabelFrame (root, borderwidth=2, text='', background='#EED202')
    body_label_frame = tk.LabelFrame (root, borderwidth=2)
    foot_label_frame = tk.LabelFrame (root, borderwidth=2, background= '#EED202')

    display_label_frame()
    display_head_widget()
    display_body_widget()
    display_footer_widget()


    root.mainloop()