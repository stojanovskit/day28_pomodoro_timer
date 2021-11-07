from tkinter import *
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
chk = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global chk
    global reps
    reps = 0
    chk = 0
    check_label["text"] = "✓" * chk
    canvas.itemconfig(canvas_text, text = "00:00")
    timer_label["text"] = "Timer"
    timer_label["fg"] = GREEN
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    global chk
    if reps == 8:
        chk += 1
        check_label["text"] = "✓" * chk
        count_down(20*60)
        timer_label["text"] = "Long Break"
        timer_label["fg"] = RED
    elif reps > 8:
        count_down(0)
    elif reps % 2 == 0:
        count_down(5*60)
        chk += 1
        check_label["text"] = "✓"*chk
        timer_label["text"] = "Break"
        timer_label["fg"] = PINK
    else:
        count_down(25*60)
        timer_label["text"] = "Work"
        timer_label["fg"] = GREEN



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count % 60}"

    canvas.itemconfig(canvas_text, text=f"{math.floor(count / 60)}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
canvas_text = canvas.create_text(101, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text="✓"*chk, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
