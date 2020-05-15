from .gateway import ReservationGateway
from projections.utils import into_list_of_tuples, count_empty_seats, change_floor_panel


class ReservationController:
    def __init__(self):
        self.gateway = ReservationGateway()

    def make_reservation(self, pid, seat_count):
        record = self.gateway.make_reservation(pid)

        floor_string = record[5]
        floor_plan = into_list_of_tuples(floor_string)
        empty_seats = count_empty_seats(floor_plan)

        if seat_count > empty_seats:
            return (0, 0)
            # Work

        else:
            return (floor_string, floor_plan)

    def save_reservation(self, uid, pid, seats, floor):
        self.gateway.save_reservation(uid, pid, seats)

        new_floor = floor
        for seat in seats:
            new_floor = change_floor_panel(seat, new_floor)

        self.gateway.change_floor_plan(new_floor, pid)

    def list_reservations(self, uid):
        return self.gateway.list_reservations(uid)

    def cancel_reservations(self, uid):
        pass