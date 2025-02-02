import tkinter as tk
from tkinter import messagebox
import mysql.connector
import random
def get_questions():
    connection = mysql.connector.connect(
        host="localhost", 
        user="root",       
        password="auth_socket", 
        database="my_database"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    connection.close()
    return questions

def get_random_question(questions):
    return random.choice(questions)


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.questions = get_questions()
        self.current_question = None
        self.score = 0
        self.question_index = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10)

        self.option_a_btn = tk.Button(self.options_frame, text="Option A", command=lambda: self.check_answer("A"))
        self.option_b_btn = tk.Button(self.options_frame, text="Option B", command=lambda: self.check_answer("B"))
        self.option_c_btn = tk.Button(self.options_frame, text="Option C", command=lambda: self.check_answer("C"))
        self.option_d_btn = tk.Button(self.options_frame, text="Option D", command=lambda: self.check_answer("D"))

        self.option_a_btn.grid(row=0, column=0, padx=10, pady=5)
        self.option_b_btn.grid(row=0, column=1, padx=10, pady=5)
        self.option_c_btn.grid(row=1, column=0, padx=10, pady=5)
        self.option_d_btn.grid(row=1, column=1, padx=10, pady=5)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        self.current_question = get_random_question(self.questions)

        self.question_label.config(text=self.current_question[1])

        self.option_a_btn.config(text=self.current_question[2])
        self.option_b_btn.config(text=self.current_question[3])
        self.option_c_btn.config(text=self.current_question[4])
        self.option_d_btn.config(text=self.current_question[5])

    def check_answer(self, chosen_option):
        correct_option = self.current_question[6]
        if chosen_option == correct_option:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", "Your answer is incorrect!")
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.next_button.config(state=tk.DISABLED)
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    root.mainloop()


