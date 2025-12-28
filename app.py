from database import init_db
from ui import QuitTrackerApp

if __name__ == "__main__":
    init_db()
    app = QuitTrackerApp()
    app.mainloop()
