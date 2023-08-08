from random import choice
from tkinter import *
WINDOW_N_BUTTON_BG = '#1D5D9B'
TEXT_COLOUR = '#F4D160'
winning_combinations = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {1, 4, 7},
    {2, 5, 8},
    {3, 6, 9},
    {1, 5, 9},
    {3, 5, 7}
]
entered_pos = []
user_combinations = []
comp_combinations = []
button_dict = {}


def clear_window():
    for widget in window.winfo_children():
        widget.destroy()


def who_won():
    for item in winning_combinations:
        if item.issubset(user_combinations):
            clear_window()
            label = Label(window, image=won_image)
            label.grid(row=0, column=0)
            return True
    for item in winning_combinations:
        if item.issubset(comp_combinations):
            clear_window()
            label = Label(window, image=lost_image)
            label.grid(row=0, column=0)
            return False
    if len(entered_pos) == 9:
        clear_window()
        label = Label(window, image=draw_image)
        label.grid(row=0, column=0)
        return False


def x_dark(event, button_index):
    clicked_button = event.widget
    if clicked_button.cget('image') == str(blank_dark):
        clicked_button.config(image=x_image_dark)
        user_combinations.append(button_index)
        entered_pos.append(button_index)
        is_player_winner = who_won()
        if is_player_winner:
            return
        else:
            o()


def x_light(event, button_index):
    clicked_button = event.widget
    if clicked_button.cget('image') == str(blank_light):
        clicked_button.config(image=x_image_light)
        user_combinations.append(button_index)
        entered_pos.append(button_index)
        is_player_winner = who_won()
        if is_player_winner:
            return
        else:
            o()


def o():
    left_pos = [x for x in list(button_dict.keys()) if x not in entered_pos]
    if len(left_pos) == 0:
        return
    rc = choice(left_pos)
    entered_pos.append(rc)
    comp_combinations.append(rc)
    if rc % 2 != 0:
        o_dark(rc)
    else:
        o_light(rc)
    who_won()


def o_dark(rc):
    if button_dict[rc].cget('image') == str(blank_dark):
        button_dict[rc].config(image=o_image_dark)
    else:
        o()


def o_light(rc):
    if button_dict[rc].cget('image') == str(blank_light):
        button_dict[rc].config(image=o_image_light)
    else:
        o()


def create_buttons():
    j, k = 0, 0
    for i in range(1, 10):
        if i % 2 == 0:
            button = Button(image=blank_light, width=130, height=130, relief=FLAT, highlightthickness=0)
            button.grid(row=j, column=k)
            button.bind('<Button-1>', lambda event, idx=i: x_light(event, idx))
            button_dict.update({i: button})

        else:
            button = Button(image=blank_dark, width=130, height=130, relief=FLAT, highlightthickness=0)
            button.grid(row=j, column=k)
            button.bind('<Button-1>', lambda event, idx=i: x_dark(event, idx))
            button_dict.update({i: button})

        if i % 3 == 0:
            j = j + 1
        if k < 2:
            k = k + 1
        else:
            k = 0


window = Tk()
window.config(bg=WINDOW_N_BUTTON_BG)
canvas = Canvas(highlightthickness=0, width=400, height=400)
canvas.grid(row=0, column=0, rowspan=3, columnspan=3)

x_image_dark = PhotoImage(file='images/x_dark.png')
o_image_dark = PhotoImage(file='images/o_dark.png')
x_image_light = PhotoImage(file='images/x_light.png')
o_image_light = PhotoImage(file='images/o_light.png')
blank_dark = PhotoImage(file='images/blank_dark.png')
blank_light = PhotoImage(file='images/blank_light.png')
won_image = PhotoImage(file='images/won.png')
lost_image = PhotoImage(file='images/lost.png')
draw_image = PhotoImage(file='images/draw.png')

create_buttons()

window.mainloop()
