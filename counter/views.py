from app import app, db
from counter.models import *


@app.route('/')
def init():
    counter = Counter.query.first()
    if not counter:
        counter = Counter(1)
        db.session.add(counter)
        db.session.commit()
    else:
        if not counter.counter:
            counter.counter = 1
        else:
            counter.counter += 1
        db.session.commit()
    return "<h1>Counters: " + str(counter.counter) + "</h1>"
