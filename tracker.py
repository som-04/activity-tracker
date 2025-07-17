import json
from datetime import datetime
import os
import argparse


class ActivityTracker:
    def __init__(self, filename="activities.json"):
        self.filename = filename
        self.activities = self.load_activities()

    def load_activities(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_activities(self):
        with open(self.filename, "w") as f:
            json.dump(self.activities, f, indent=4)

    def add_activity(self, activity):
        entry = {
            "activity": activity,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.activities.append(entry)
        self.save_activities()

    def show_all(self):
        return self.activities

    def latest(self):
        return self.activities[-1] if self.activities else None

    def filter_by_keyword(self, keyword):
        return [a for a in self.activities if keyword.lower() in a["activity"].lower()]

    def filter_by_date(self, date):  # date format: YYYY-MM-DD
        return [a for a in self.activities if a["timestamp"].startswith(date)]


