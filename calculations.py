from datetime import datetime

def calculate_stats(quit_date, cigarettes_per_day, daily_cost):
    today = datetime.now().date()
    quit_date = datetime.strptime(quit_date, "%Y-%m-%d").date()

    days_smoke_free = max((today - quit_date).days, 0)
    cigarettes_avoided = days_smoke_free * cigarettes_per_day
    money_saved = days_smoke_free * daily_cost

    return days_smoke_free, cigarettes_avoided, money_saved
