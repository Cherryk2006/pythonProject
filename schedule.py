import datetime
from datetime import timedelta


def booking_time_discovery(schedule_start, schedule_end, trainer_bookings, search_window):

    start_time = schedule_start
    end_time = schedule_end

    all_time_slots = []
    current_time = start_time
    while current_time + timedelta(minutes=search_window) <= end_time:
        all_time_slots.append(current_time)
        current_time += timedelta(minutes=search_window)

    for booking in trainer_bookings :
        booking_start = booking[0]
        booking_end = booking[1]
        all_time_slots = [slot for slot in all_time_slots if not (booking_start <= slot < booking_end or booking_start < slot + timedelta(minutes=search_window) <= booking_end)]

    return all_time_slots


if __name__ == '__main__':
    schedule_start = datetime.datetime(2024, 12, 25, 9, 0)
    schedule_end = datetime.datetime(2024, 12, 25, 14, 0)
    search_window = 60
    trainer_bookings = [
        (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0),),
    ]

    available_slots = booking_time_discovery(schedule_start, schedule_end, trainer_bookings, search_window)
    print("Available slots for booking:")
    for slot in available_slots:
        print(slot)