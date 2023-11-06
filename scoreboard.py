import tkinter as tk

class ScoreboardApp:
    def __init__(self, root):
        self.root = root
        root.title("Arcade Scoreboard")
        
        self.scores = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Label for displaying the scoreboard
        self.scoreboard_label = tk.Label(self.root, text="Scoreboard", font=("Helvetica", 16))
        self.scoreboard_label.pack(pady=10)
        
        # Listbox to display scores
        self.score_listbox = tk.Listbox(self.root, width=30, height=10)
        self.score_listbox.pack()
        
        # Entry fields for name and score
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.score_label = tk.Label(self.root, text="Score:")
        self.score_label.pack()
        self.score_entry = tk.Entry(self.root)
        self.score_entry.pack()
        
        # Add score button
        self.add_score_button = tk.Button(self.root, text="Add Score", command=self.add_score)
        self.add_score_button.pack(pady=10)
        
    def add_score(self):
        name = self.name_entry.get()
        score = self.score_entry.get()
        
        if name and score:
            score_info = f"{name}: {score}"
            self.scores.append(score_info)
            self.update_scoreboard()
            
            # Clear the entry fields
            self.name_entry.delete(0, tk.END)
            self.score_entry.delete(0, tk.END)
    
    def update_scoreboard(self):
        self.score_listbox.delete(0, tk.END)
        for score in self.scores:
            self.score_listbox.insert(tk.END, score)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScoreboardApp(root)
    root.mainloop()