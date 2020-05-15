from .model import ReservationModel
from db.db import Database


class ReservationGateway:
    def __init__(self):
        self.model = ReservationModel()
        self.db = Database()

    def make_reservation(self, pid):
        with self.db.conn:
            self.db.c.execute('SELECT * FROM projections WHERE id = (?)', (pid,))
            record = self.db.c.fetchone()

        return record

    def save_reservation(self, uid, pid, seats):
        with self.db.conn:
            for seat in seats:
                self.db.c.execute('INSERT INTO reservations(row, seat, user_id, projection_id)VALUES(?,?,?,?)',
                                  (seat[:1], seat[1:], uid, pid))

    def change_floor_plan(self, floor, pid):
        with self.db.conn:
            self.db.c.execute('UPDATE projections SET floor_plan = (?) WHERE id = (?)', (floor, pid))
