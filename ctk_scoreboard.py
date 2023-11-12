import customtkinter
import tkinter as tk
import csv

class ScoreboardApp:
    def __init__(self, root, score):
        self.root = root
        self.score = score
        root.title("Arcade Scoreboard")
        
        self.score_dict = {}
        self.csv_filepath = "scoreboard.csv"
        with open(self.csv_filepath, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            # Assuming the first row contains column headers
            headers = next(csv_reader, None)

            for row in csv_reader:
                if row:  # Skip empty rows
                    name = row[0]
                    score = float(row[1])  # Assuming scores are numeric, adjust if needed
                    self.score_dict[name] = score
        self.score_dict = dict(sorted(self.score_dict.items(), key=lambda item: item[1], reverse=True))
        self.create_widgets()
    
    def create_widgets(self):
        # Label for displaying the scoreboard
        self.scoreboard_label = customtkinter.CTkLabel(self.root, text="Scoreboard", font=("Helvetica", 30))
        self.scoreboard_label.pack(pady=10)
        
        # Listbox to display scores
        #self.score_listbox = tk.Listbox(self.root, width=75, height=25)
        self.score_frame = customtkinter.CTkScrollableFrame(self.root, width=200, height=50)
        self.score_frame.pack()
        
        for name in self.score_dict:
            txt = f"{name}: {self.score_dict.get(name)}"
            self.score_entry = customtkinter.CTkLabel(self.score_frame, text=txt)
            self.score_entry.pack()
        
        # Entry fields for name and score
        self.name_label = customtkinter.CTkLabel(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = customtkinter.CTkEntry(self.root)
        self.name_entry.pack()
        
        # Add score button
        self.add_score_button = customtkinter.CTkButton(self.root, text="Add Score", command=self.add_score)
        self.add_score_button.pack(pady=10)
        

    def add_score(self):
        name = self.name_entry.get()
        score = self.score
        
        if name and score:
            name = name[:10]
            existing_score = self.score_dict.get(name)
            
            if existing_score != None:    
                if score <= self.score_dict.get(name):
                    print("Can only override a score with same name if the new score is higher")
                    return
            
            self.score_dict[name] = score
            txt = f"{name}: {self.score_dict.get(name)}"
            # Sort the score dict
            self.score_dict = dict(sorted(self.score_dict.items(), key=lambda item: item[1], reverse=True))
            
            # Clear existing contents of the CSV file
            with open(self.csv_filepath, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows([])  # Writing an empty list to clear the file

            # Write the dictionary to the CSV file
            with open(self.csv_filepath, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)

                # Write header
                csv_writer.writerow(['NAME', 'SCORE'])

                # Write data
                for name, score in self.score_dict.items():
                    csv_writer.writerow([name, score])
                    
            self.score_entry = customtkinter.CTkLabel(self.score_frame, text=txt)
            self.score_entry.pack()
            
            # Clear the entry fields
            self.add_score_button.destroy()
            self.name_entry.destroy()
            self.name_label.destroy()

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ScoreboardApp(root, 1200)
    root.mainloop()