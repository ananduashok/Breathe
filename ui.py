import customtkinter as ctk
from calculations import calculate_stats

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class QuitTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Quit Smoking Tracker")
        self.geometry("400x300")

        self.quit_date = "2025-12-26"
        self.cigarettes_per_day = 2
        self.daily_cost = 50

        self.build_dashboard()

    def build_dashboard(self):
        days, cigs, money = calculate_stats(
            self.quit_date,
            self.cigarettes_per_day,
            self.daily_cost
        )

        ctk.CTkLabel(self, text="🚭 Quit Smoking Tracker",
                     font=("Arial", 20)).pack(pady=15)

        ctk.CTkLabel(self, text=f"Smoke-free days: {days}").pack(pady=5)
        ctk.CTkLabel(self, text=f"Cigarettes avoided: {cigs}").pack(pady=5)
        ctk.CTkLabel(self, text=f"Money saved: ₹{money}").pack(pady=5)
