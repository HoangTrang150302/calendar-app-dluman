from flask import Flask, Response, redirect, request, render_template

import datetime

from calendar_display import *
from calendar_db import DB

app: Flask = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
  month = None
  year = None
  try:
    month = request.form["month"]
    year = request.form["year"]
  except:
    now = datetime.datetime.now()
    month = now.month
    year = now.year
  return render_template(
    "layout.html",
    data = {
      "month": month,
      "year": year
    }
  )

@app.route("/calendar", methods = ["GET"])
def calendar():
    month, year = (
      request.args.get("month"),
      request.args.get("year")
    )
    calendar = Calendar(int(month), int(year))
    return render_template(
      "components/calendar.html",
      display_calendar = calendar.date_display()
    )

@app.route("/modals/add-modal", methods = ["GET"])
def add_modal_get():
  month, day, year = (
    request.args.get("month"),
    request.args.get("day") or 1,
    request.args.get("year")
  )
  if int(month) < 10:
     month = "0" + month
  if int(day) < 10:
     day = "0" + day
  return render_template(
    "components/add_modal.html",
    data = {"month": month, "day": day, "year": year}
  )

@app.route("/events/new", methods = ["POST"])
def new_event_post():
    return Response(status=200)

if __name__ == "__main__":
    app.run(port = 5001)
