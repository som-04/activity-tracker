from collections import Counter
from datetime import datetime

class ActivityAnalytics:
    def __init__(self, activities):
        self.activities = activities

    def total_activities(self):
        return len(self.activities)

    def activities_today(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return sum(1 for a in self.activities if a["timestamp"].startswith(today))

    def most_common_keywords(self, top_n=3):
        words = []
        for a in self.activities:
            words.extend(a["activity"].lower().split())
        return Counter(words).most_common(top_n)
