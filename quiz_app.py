import tkinter as tk
from tkinter import messagebox
import mysql.connector

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("MySQL Quiz Application")
        
        # Database Connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="auth_socket",
            database="my_database.sql"
        )
        self.cursor = self.connection.cursor()
        
        # Quiz Variables
        self.current_question = 0
        self.score = 0
        self.questions = self.load_questions()
        
        # UI Components
        self.setup_ui()
    
    def load_questions(self):
        self.cursor.execute("SELECT * FROM quiz_questions")
        return self.cursor.fetchall()
    
    def setup_ui(self):
        # Question Label
        self.question_label = tk.Label(
            self.master, 
            text="", 
            wraplength=400, 
            font=("Arial", 12)
        )
        self.question_label.pack(pady=20)
        
        # Option Buttons
        self.option_vars = []
        for i in range(4):
            var = tk.StringVar()
            option = tk.Radiobutton(
                self.master, 
                text="", 
                variable=var, 
                value=""
            )
            option.pack(pady=10)
            self.option_vars.append((var, option))
        
        # Submit Button
        submit_btn = tk.Button(
            self.master, 
            text="Submit", 
            command=self.check_answer
        )
        submit_btn.pack(pady=20)
        
        self.load_next_question()
    
    def load_next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question[1])
            
            options = [question[2], question[3], question[4], question[5]]
            for i, (var, option) in enumerate(self.option_vars):
                option.config(text=options[i], value=options[i])
                var.set(None)
        else:
            self.show_result()
    
    def check_answer(self):
        selected_answer = None
        for var, _ in self.option_vars:
            if var.get():
                selected_answer = var.get()
                break
        
        if selected_answer:
            correct_answer = self.questions[self.current_question][6]
            if selected_answer == correct_answer:
                self.score += 1
            
            self.current_question += 1
            self.load_next_question()
        else:
            messagebox.showwarning("Warning", "Please select an answer!")
    
    def show_result(self):
        messagebox.showinfo(
            "Quiz Completed", 
            f"Your Score: {self.score}/{len(self.questions)}"
        )
        self.master.quit()

def main():
    root = tk.Tk()
    root.geometry("500x400")
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

