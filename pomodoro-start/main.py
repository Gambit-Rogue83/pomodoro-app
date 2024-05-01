from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    min_remain = math.floor(count / 60)
    sec_remain = count % 60
    if sec_remain < 10:
        sec_remain = f"0{sec_remain}"

    canvas.itemconfig(timer_text, text=f"{min_remain}:{sec_remain}")
    if count > 0:
        timer = window.after(1000, count_down, count -1)
    else:
        start_time()
        add_check = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            add_check += "✔"
            checkmark_label.config(text=add_check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=400, height=350)
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Label
timer_label = Label(text="Timer", font=(FONT_NAME, 55, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)
checkmark_label = Label(text="", font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark_label.grid(column=1, row=3)

#Button
start_btn = Button(text="Start", command=start_time)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", command=reset)
reset_btn.grid(column=2, row=2)




window.mainloop()


