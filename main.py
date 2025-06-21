import tkinter as tk
from tkinter import messagebox
import random
root = tk.Tk()
root.title("Quiz generator")

tk.Label(root, text="Quiz generator", font=("Aerial", 20)).grid(row=0, column=0)
tk.Label(root, text="", font=("Aerial", 10)).grid(row=1, column=1)
tk.Label(root, text="Copy and paste your notes here:  ").grid(row=2, column=0)
paragraph = tk.Entry(root, width= 40)
paragraph.grid(row=2, column=1)

tk.Label(root, text="How many questions do you want?  ").grid(row=3, column=0)
question_count = tk.Entry(root, width=10)
question_count.grid(row=3, column=1)

tk.Label(root).grid(row=4, column=0)
tk.Label(root).grid(row=6, column=0)



def submitter():
    global notes, answer, question
    counter = 1
    total_questions = []
    notes = paragraph.get().split(".")
    if int(question_count.get()) > len(notes):
        messagebox.showerror("Error", f"Maximum number of questions based on your notes is {len(notes)}")
        return
    else:    
        notes = random.sample(notes, int(question_count.get()))
    unaskable = ["the", "is", "are", "was", "were",
        "of", "at", "in", "to", "by",
        "and", "but", "or", "if", "then",
        "on", "with", "as", "for", "from",
        "a", "an", "he", "she", "it", "they", "you", "we",
        "this", "that", "these", "those", "because", "although",
        "unless", "while", "during", "since", "before",
        "be", "do", "to", "an", "if", "or"]
    
    for note in notes:
        if note != "":
            split_note = note.split(" ")
            answer_unreplaced = random.choice(split_note)
            answer = answer_unreplaced.replace(".", "").replace(",", "").replace(";", "").replace(":", "")
            answer = answer.replace("-", "").replace("!","").replace("?", "").replace(";", "").lower()
            while answer in unaskable or len(answer) <= 2:
                answer_unreplaced = random.choice(split_note)
                answer = answer_unreplaced.replace(".", "").replace(",", "").replace(";", "").replace(":", "")
                answer = answer.replace("-", "").replace("!","").replace("?", "").replace(";", "")

            split_note[split_note.index(answer_unreplaced)] = "........"
            question = ""
            for word in split_note:
                if question == "":
                    question += word
                else:
                    question += " " + word
            total_questions.append({
                "count" : counter,
                "question" : question,
                "answer" : answer
            })
        counter +=1
    print(total_questions)
    for q in total_questions:
        tk.Label(root, text= f'{q["count"]}- {q["question"]}', wraplength=400).grid(row=q["count"]+10, column=0)
        globals()[f"entry{q['count']}"] = tk.Entry(root, width=10)
        (globals()[f"entry{q['count']}"]).grid(row=q["count"]+10, column=1)

        def make_command(count, answer):
            def command():
                ans_ent = globals()[f"entry{count}"].get()
                if ans_ent.strip().lower() == answer:
                    globals()[f"btn{count}"].config(bg = "green")
                else:
                    globals()[f"btn{count}"].config(bg = "red")
            return command
        
        globals()[f"command{q['count']}"] = make_command(q["count"], q["answer"])
        globals()[f"btn{q['count']}"] = tk.Button(root, text="check", command=globals()[f"command{q['count']}"])
        globals()[f"btn{q['count']}"].grid(row=q["count"]+10, column=3)

submit = tk.Button(root, text="Submit", command= submitter)
submit.grid(row=5, column=1)

root.mainloop()