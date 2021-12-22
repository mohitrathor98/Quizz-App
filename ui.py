from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.maxsize(width=500, height=500)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # score label
        self.score = 0
        self.score_label = Label(text=f"Score:{self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        
        # question
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            text= "Question here",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"),
            width=280
        )      
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        # buttons
        correct_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=correct_image, highlightthickness=0, bg=THEME_COLOR)
        self.correct.grid(column=0, row=2)
        
        wrong_image = PhotoImage(file='images/false.png')
        self.wrong = Button(image=wrong_image, highlightthickness=0, bg=THEME_COLOR)
        self.wrong.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=question_text)