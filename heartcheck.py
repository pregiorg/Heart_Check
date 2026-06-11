import tkinter as tk
from tkinter import ttk, messagebox
import time


class HeartCheckApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HeartCheck")
        self.root.geometry("512x400")
        self.root.configure(bg='#1a1a2e')
        
        
        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.rest_rate = tk.StringVar()
        self.first_rate = tk.StringVar()
        self.second_rate = tk.StringVar()
        self.squat_count = 0
        self.seconds = 0
        self.timer_running = False
        self.timer_id = None
        
        
        self.show_welcome_screen()
    
    def clear_screen(self):
        """Clear all widgets from the screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_welcome_screen(self):
        """Display welcome screen"""
        self.clear_screen()
        
        frame = tk.Frame(self.root, bg='#1a1a2e')
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        tk.Label(frame, text="HeartCheck", font=('Arial', 24, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=20)
        
        info_text = """Measure your heart rate twice within a minute:

In the first 15 seconds of a minute, then in the last 15 seconds.

Record the results in the appropriate fields."""
        
        tk.Label(frame, text=info_text, font=('Arial', 11),
                bg='#1a1a2e', fg='white', justify='left').pack(pady=20)
        
        tk.Button(frame, text="Next", command=self.show_info_screen,
                 bg='#3a3a4e', fg='white', font=('Arial', 12),
                 width=20, height=2).pack(pady=10)
    
    def show_info_screen(self):
        """Display instructions screen"""
        self.clear_screen()
        
        frame = tk.Frame(self.root, bg='#1a1a2e')
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        tk.Label(frame, text="Instructions", font=('Arial', 20, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=15)
        
        instructions = """Step 1: Sit quietly for 1 minute, then count your pulse for 15 seconds.

Step 2: Perform 30 squats in 45 seconds at a steady pace.

Step 3: Immediately after squats, measure pulse for 15 seconds.

Step 4: Wait 45 seconds, then measure pulse again for 15 seconds."""
        
        tk.Label(frame, text=instructions, font=('Arial', 10),
                bg='#1a1a2e', fg='white', justify='left').pack(pady=15)
        
        tk.Button(frame, text="Start Test", command=self.show_user_info_screen,
                 bg='#3a3a4e', fg='white', font=('Arial', 12),
                 width=20, height=2).pack(pady=10)
    
    def show_user_info_screen(self):
        """Display user information input screen"""
        self.clear_screen()
        
        frame = tk.Frame(self.root, bg='#1a1a2e')
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        tk.Label(frame, text="Enter Your Information", font=('Arial', 20, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=20)
        
    
        tk.Label(frame, text="Name:", font=('Arial', 11),
                bg='#1a1a2e', fg='white', anchor='w').pack(fill='x', pady=(10, 5))
        tk.Entry(frame, textvariable=self.name, font=('Arial', 11),
                bg='#2a2a3e', fg='white', insertbackground='white').pack(fill='x', pady=(0, 15))
        
        
        tk.Label(frame, text="Age:", font=('Arial', 11),
                bg='#1a1a2e', fg='white', anchor='w').pack(fill='x', pady=(10, 5))
        tk.Entry(frame, textvariable=self.age, font=('Arial', 11),
                bg='#2a2a3e', fg='white', insertbackground='white').pack(fill='x', pady=(0, 15))
        
        tk.Button(frame, text="Continue", command=self.validate_user_info,
                 bg='#3a3a4e', fg='white', font=('Arial', 12),
                 width=20, height=2).pack(pady=20)
    
    def validate_user_info(self):
        """Validate user information and proceed"""
        if not self.name.get().strip():
            messagebox.showerror("Error", "Please enter your name")
            return
        
        try:
            age = int(self.age.get())
            if age < 7 or age > 120:
                messagebox.showerror("Error", "Please enter a valid age (7-120)")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age")
            return
        
        self.show_test_screen('rest')
    
    def show_test_screen(self, phase):
        """Display test screen for different phases"""
        self.clear_screen()
        self.seconds = 0
        self.timer_running = False
        
        frame = tk.Frame(self.root, bg='#1a1a2e')
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        if phase == 'rest':
            tk.Label(frame, text="Resting Heart Rate", font=('Arial', 20, 'bold'),
                    bg='#1a1a2e', fg='white').pack(pady=10)
            tk.Label(frame, text="Sit quietly for 1 minute.\nCount your pulse for 15 seconds.",
                    font=('Arial', 10), bg='#1a1a2e', fg='white').pack(pady=10)
            
           
            self.create_stopwatch(frame)
            
            tk.Label(frame, text="Enter pulse count (15 seconds):", font=('Arial', 10),
                    bg='#1a1a2e', fg='white', anchor='w').pack(fill='x', pady=(10, 5))
            tk.Entry(frame, textvariable=self.rest_rate, font=('Arial', 11),
                    bg='#2a2a3e', fg='white', insertbackground='white').pack(fill='x')
            
            tk.Button(frame, text="Next", command=lambda: self.validate_and_next('rest'),
                     bg='#3a3a4e', fg='white', font=('Arial', 12),
                     width=20, height=2).pack(pady=20)
        
        elif phase == 'squats':
            tk.Label(frame, text="Perform Squats", font=('Arial', 20, 'bold'),
                    bg='#1a1a2e', fg='white').pack(pady=10)
            tk.Label(frame, text="Complete 30 squats in 45 seconds.\nClick the button for each squat.",
                    font=('Arial', 10), bg='#1a1a2e', fg='white').pack(pady=10)
            
            
            self.create_stopwatch(frame)
            
            
            counter_frame = tk.Frame(frame, bg='#2a2a3e')
            counter_frame.pack(fill='x', pady=10)
            self.squat_label = tk.Label(counter_frame, text=f"{self.squat_count}/30",
                                       font=('Arial', 36, 'bold'), bg='#2a2a3e', fg='white')
            self.squat_label.pack(pady=20)
            tk.Label(counter_frame, text="Squats", font=('Arial', 10),
                    bg='#2a2a3e', fg='white').pack(pady=(0, 10))
            
            tk.Button(frame, text="Squat +1", command=self.increment_squat,
                     bg='#4a4a6e', fg='white', font=('Arial', 12),
                     width=20, height=2).pack(pady=10)
            
            tk.Button(frame, text="Next", command=lambda: self.validate_and_next('squats'),
                     bg='#3a3a4e', fg='white', font=('Arial', 12),
                     width=20, height=2).pack(pady=10)
        
        elif phase == 'first':
            tk.Label(frame, text="First Recovery", font=('Arial', 20, 'bold'),
                    bg='#1a1a2e', fg='white').pack(pady=10)
            tk.Label(frame, text="Immediately after squats,\ncount your pulse for 15 seconds.",
                    font=('Arial', 10), bg='#1a1a2e', fg='white').pack(pady=10)
            
            
            self.create_stopwatch(frame)
            
            tk.Label(frame, text="Enter pulse count (15 seconds):", font=('Arial', 10),
                    bg='#1a1a2e', fg='white', anchor='w').pack(fill='x', pady=(10, 5))
            tk.Entry(frame, textvariable=self.first_rate, font=('Arial', 11),
                    bg='#2a2a3e', fg='white', insertbackground='white').pack(fill='x')
            
            tk.Button(frame, text="Next", command=lambda: self.validate_and_next('first'),
                     bg='#3a3a4e', fg='white', font=('Arial', 12),
                     width=20, height=2).pack(pady=20)
        
        elif phase == 'second':
            tk.Label(frame, text="Final Recovery", font=('Arial', 20, 'bold'),
                    bg='#1a1a2e', fg='white').pack(pady=10)
            tk.Label(frame, text="Wait 45 seconds,\nthen count your pulse for 15 seconds.",
                    font=('Arial', 10), bg='#1a1a2e', fg='white').pack(pady=10)
            
            
            self.create_stopwatch(frame)
            
            tk.Label(frame, text="Enter pulse count (15 seconds):", font=('Arial', 10),
                    bg='#1a1a2e', fg='white', anchor='w').pack(fill='x', pady=(10, 5))
            tk.Entry(frame, textvariable=self.second_rate, font=('Arial', 11),
                    bg='#2a2a3e', fg='white', insertbackground='white').pack(fill='x')
            
            tk.Button(frame, text="View Results", command=self.show_results_screen,
                     bg='#3a3a4e', fg='white', font=('Arial', 12),
                     width=20, height=2).pack(pady=20)
    
    def create_stopwatch(self, parent):
        """Create stopwatch widget"""
        stopwatch_frame = tk.Frame(parent, bg='#2a2a3e')
        stopwatch_frame.pack(fill='x', pady=10)
        
        tk.Label(stopwatch_frame, text="Stopwatch", font=('Arial', 10),
                bg='#2a2a3e', fg='white').pack(pady=(10, 5))
        
        self.timer_label = tk.Label(stopwatch_frame, text="0s",
                                    font=('Arial', 32, 'bold'),
                                    bg='#2a2a3e', fg='white')
        self.timer_label.pack(pady=10)
        
        button_frame = tk.Frame(stopwatch_frame, bg='#2a2a3e')
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Start", command=self.start_timer,
                 bg='#2d5016', fg='white', font=('Arial', 10),
                 width=8).pack(side='left', padx=5)
        tk.Button(button_frame, text="Stop", command=self.stop_timer,
                 bg='#6b5b00', fg='white', font=('Arial', 10),
                 width=8).pack(side='left', padx=5)
        tk.Button(button_frame, text="Reset", command=self.reset_timer,
                 bg='#5b0000', fg='white', font=('Arial', 10),
                 width=8).pack(side='left', padx=5)
    
    def start_timer(self):
        """Start the stopwatch"""
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()
    
    def stop_timer(self):
        """Stop the stopwatch"""
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
    
    def reset_timer(self):
        """Reset the stopwatch"""
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.seconds = 0
        if hasattr(self, 'timer_label'):
            self.timer_label.config(text="0s")
    
    def update_timer(self):
        """Update stopwatch display"""
        if self.timer_running:
            self.seconds += 1
            if hasattr(self, 'timer_label'):
                self.timer_label.config(text=f"{self.seconds}s")
            self.timer_id = self.root.after(1000, self.update_timer)
    
    def increment_squat(self):
        """Increment squat counter"""
        if self.squat_count < 30:
            self.squat_count += 1
            self.squat_label.config(text=f"{self.squat_count}/30")
    
    def validate_and_next(self, phase):
        """Validate current phase and move to next"""
        if phase == 'rest':
            if not self.validate_heart_rate(self.rest_rate.get()):
                return
            self.squat_count = 0
            self.show_test_screen('squats')
        elif phase == 'squats':
            if self.squat_count < 30:
                messagebox.showerror("Error", "Please complete 30 squats")
                return
            self.show_test_screen('first')
        elif phase == 'first':
            if not self.validate_heart_rate(self.first_rate.get()):
                return
            self.show_test_screen('second')
    
    def validate_heart_rate(self, value):
        """Validate heart rate input"""
        if not value:
            messagebox.showerror("Error", "Please enter your heart rate")
            return False
        try:
            rate = int(value)
            if rate < 30 or rate > 250:
                messagebox.showerror("Error", "Please enter a valid heart rate (30-250 bpm)")
                return False
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return False
        return True
    
    def calculate_ruffier_index(self):
        """Calculate Ruffier index"""
        p1 = float(self.rest_rate.get())
        p2 = float(self.first_rate.get())
        p3 = float(self.second_rate.get())
        return (p1 + p2 + p3 - 200) / 10
    
    def get_fitness_level(self, index, age):
        """Determine fitness level based on age and index"""
        if age < 30:
            if index < 3:
                return "Excellent", "Outstanding cardiovascular health!"
            elif index < 6:
                return "Good", "Your heart is in good shape!"
            elif index < 10:
                return "Average", "Room for improvement."
            elif index < 15:
                return "Below Average", "Consider more cardio exercise."
            else:
                return "Poor", "Consult a doctor and start gentle exercise."
        elif age < 50:
            if index < 4:
                return "Excellent", "Outstanding cardiovascular health!"
            elif index < 8:
                return "Good", "Your heart is in good shape!"
            elif index < 12:
                return "Average", "Room for improvement."
            elif index < 16:
                return "Below Average", "Consider more cardio exercise."
            else:
                return "Poor", "Consult a doctor and start gentle exercise."
        else:
            if index < 5:
                return "Excellent", "Outstanding cardiovascular health!"
            elif index < 10:
                return "Good", "Your heart is in good shape!"
            elif index < 14:
                return "Average", "Room for improvement."
            elif index < 18:
                return "Below Average", "Consider more cardio exercise."
            else:
                return "Poor", "Consult a doctor and start gentle exercise."
    
    def show_results_screen(self):
        """Display results screen"""
        if not self.validate_heart_rate(self.second_rate.get()):
            return
        
        self.clear_screen()
        
        frame = tk.Frame(self.root, bg='#1a1a2e')
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        tk.Label(frame, text="Test Results", font=('Arial', 20, 'bold'),
                bg='#1a1a2e', fg='white').pack(pady=15)
        
        
        index = self.calculate_ruffier_index()
        level, description = self.get_fitness_level(index, int(self.age.get()))
        
       
        results_frame = tk.Frame(frame, bg='#2a2a3e')
        results_frame.pack(fill='both', expand=True, pady=10)
        
        info_text = f"Name: {self.name.get()}\nAge: {self.age.get()} years\n"
        tk.Label(results_frame, text=info_text, font=('Arial', 10),
                bg='#2a2a3e', fg='white', justify='left').pack(pady=10, padx=20, anchor='w')
        
        tk.Label(results_frame, text=f"Ruffier Index: {index:.2f}",
                font=('Arial', 18, 'bold'), bg='#2a2a3e', fg='white').pack(pady=5)
        
        tk.Label(results_frame, text=f"Level: {level}",
                font=('Arial', 16), bg='#2a2a3e', fg='white').pack(pady=5)
        
        tk.Label(results_frame, text=description,
                font=('Arial', 10), bg='#2a2a3e', fg='white').pack(pady=5)
        
        measurements = f"\nResting: {self.rest_rate.get()} beats (15s)\n"
        measurements += f"After exercise: {self.first_rate.get()} beats (15s)\n"
        measurements += f"Recovery: {self.second_rate.get()} beats (15s)"
        
        tk.Label(results_frame, text=measurements, font=('Arial', 9),
                bg='#2a2a3e', fg='white', justify='left').pack(pady=15, padx=20)
        
        tk.Button(frame, text="Take Another Test", command=self.reset_app,
                 bg='#3a3a4e', fg='white', font=('Arial', 12),
                 width=20, height=2).pack(pady=10)
    
    def reset_app(self):
        """Reset application to start"""
        self.name.set('')
        self.age.set('')
        self.rest_rate.set('')
        self.first_rate.set('')
        self.second_rate.set('')
        self.squat_count = 0
        self.seconds = 0
        self.timer_running = False
        self.show_welcome_screen()


if __name__ == "__main__":
    root = tk.Tk()
    app = HeartCheckApp(root)
    root.mainloop()
