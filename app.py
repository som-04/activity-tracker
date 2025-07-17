from flask import Flask, render_template, request, redirect, url_for
from tracker import ActivityTracker
from analytics import ActivityAnalytics

app = Flask(__name__)
tracker = ActivityTracker()
analytics = ActivityAnalytics(tracker.activities)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        activity = request.form.get("activity")
        if activity:
            tracker.add_activity(activity)
        return redirect(url_for("index"))

    all_activities = tracker.show_all()[::-1]  # latest on top
    keyword = request.args.get("keyword", "")
    date = request.args.get("date", "")
    
    if keyword:
        activities = tracker.filter_by_keyword(keyword)
    elif date:
        activities = tracker.filter_by_date(date)
    else:
        activities = tracker.show_all()
    return render_template("index.html", activities=all_activities,keyword=keyword,date=date)


@app.route("/analytics")
def show_analytics():
    total = analytics.total_activities()
    today = analytics.activities_today()
    common = analytics.most_common_keywords(top_n=3)
    return render_template("analytics.html", total=total, today=today, common=common)


if __name__ == "__main__":
    app.run(debug=True)
