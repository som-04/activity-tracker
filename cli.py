# cli.py
import argparse
from tracker import ActivityTracker
from analytics import ActivityAnalytics

parser = argparse.ArgumentParser(description="Activity Tracker")
parser.add_argument("--add", help="Add a new activity")
parser.add_argument("--show", action='store_true', help="Show all activities")
parser.add_argument("--latest", action='store_true', help="Show latest activity")
parser.add_argument("--filter", help="Filter activities by keyword")
parser.add_argument("--date", help="Filter activities by date")
parser.add_argument("--analytics", help="Analytics: daily_count | top_keywords | time_distribution")
args = parser.parse_args()

tracker = ActivityTracker()

if args.add:
    tracker.add_activity(args.add)
elif args.show:
    for a in tracker.show_all():
        print(a)
elif args.latest:
    print(tracker.latest())
elif args.filter:
    results = tracker.filter_by_keyword(args.filter)
    for r in results:
        print(r)
elif args.date:
    results = tracker.filter_by_date(args.date)
    for r in results:
        print(r)

elif args.analytics:
    if args.analytics == "daily_count":
        print(activity_count_by_day(tracker.activities))
    elif args.analytics == "top_keywords":
        print(common_keywords(tracker.activities))
    elif args.analytics == "time_distribution":
        print(time_of_day_distribution(tracker.activities))
else:
    parser.print_help()
