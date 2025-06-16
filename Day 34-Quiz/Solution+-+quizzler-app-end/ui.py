from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#2E8BC0"
TEXT_COLOR = "#ffffff"
CANVAS_BG = "#f8f8f8"
CORRECT_COLOR = "#a8e6cf"
WRONG_COLOR = "#ff8b94"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(
            text="Score: 0",
            fg=TEXT_COLOR,
            bg=THEME_COLOR,
            font=("Arial", 14, "bold")
        )
        self.score_label.grid(row=0, column=1, sticky="e")

        # Question Canvas
        self.canvas = Canvas(width=320, height=280, bg=CANVAS_BG, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            160,
            140,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        # Buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            bd=0,
            command=self.true_pressed,
            activebackground=THEME_COLOR,
            bg=THEME_COLOR
        )
        self.true_button.image = true_image
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            bd=0,
            command=self.false_pressed,
            activebackground=THEME_COLOR,
            bg=THEME_COLOR
        )
        self.false_button.image = false_image
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=CANVAS_BG)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="🎉 You've reached the end of the quiz!")
            self.true_button.config(state="disabled", bg="#ccc")
            self.false_button.config(state="disabled", bg="#ccc")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        new_color = CORRECT_COLOR if is_right else WRONG_COLOR
        self.canvas.config(bg=new_color)
        self.window.after(1000, self.get_next_question)
