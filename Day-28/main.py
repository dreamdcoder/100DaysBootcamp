import tkinter as tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# start_counter
def start_counter():
    start_button["state"] = "disabled"
    global reps
    reps += 1
    # print(reps)
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    print(work_secs)
    window.deiconify()
    if reps % 8 == 0:
        counter(long_break_secs)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        counter(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
    else:
        counter(work_secs)
        timer_label.config(text=" Work", fg=GREEN)
    window.iconify()



# Counter

def counter(count):
    MM = count // 60
    SS = count % 60
    global timer

    if SS < 10:
        SS = f"0{SS}"
    if MM < 10:
        MM = f"0{MM}"
    canvas.itemconfig(timer_text, text=f"{MM}:{SS}")

    if count > 0:
        timer = window.after(1000, counter, count - 1)
    else:
        start_counter()
        if reps % 2 == 0:
            check_count = reps // 2
            check_label.config(text=check_count * "✔")



# reset

def reset():
    SS = f"00"
    MM = f"00"
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"{MM}:{SS}")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text='')
    global reps
    reps = 0
    start_button["state"] = "normal"


# UI Setup
window = tk.Tk()

window.title("Productivity Manager")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tk.PhotoImage(file="tomato.png")
timer_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = tk.Button(text="Start", highlightthickness=0, command=start_counter)
start_button.grid(row=3, column=0)

check_label = tk.Label(bg=YELLOW, fg=GREEN)
check_label.grid(row=4, column=1)
reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=3, column=2)

window.mainloop()
