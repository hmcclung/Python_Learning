from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN(TEST) = 1
# SHORT_BREAK_MIN(TEST) = 1
# LONG_BREAK_MIN(TEST) = 2
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_button.config(state="active")
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    check_mark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button.config(state="disabled")
    global reps
    global title
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        reps = 0
        title.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 1:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        title.grid(column=2, row=0)
    else:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        title.grid(column=2, row=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            check_mark.config(text=marks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=2, row=1)

timer_reset = Button(text="Reset", fg="Black", font=(FONT_NAME, 14, "bold"), command=reset_timer)
timer_reset.grid(column=3, row=2)

start_button = Button(text="Start", fg="Black", font=(FONT_NAME, 14, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title.grid(column=2, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
check_mark.grid(column=2, row=4)


window.mainloop()
