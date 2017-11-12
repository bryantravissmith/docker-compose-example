from app import db


class Counter(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    counter = db.Column(
        db.Integer
    )

    def __init__(self, count):
        self.counter = count

    def __repr__(self):
        return '<Count %r>' % self.counter
