import datetime
import unittest
import schedule


class TestSchedule(unittest.TestCase):
    maxDiff = None

    def test_schedule(self):
        schedule_start = datetime.datetime(2024, 12, 25, 9, 0)
        schedule_end = datetime.datetime(2024, 12, 25, 14, 0)
        trainer_bookings = []
        search_window = 15
        results = schedule.booking_time_discovery(schedule_start, schedule_end, trainer_bookings, search_window)
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15), datetime.datetime(2024, 12, 25, 9, 30), datetime.datetime(2024, 12, 25, 9, 45),
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15), datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15), datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15), datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 13, 15), datetime.datetime(2024, 12, 25, 13, 30), datetime.datetime(2024, 12, 25, 13, 45),
        ]
        self.assertEqual(expected, results)

    def test_schedule_one_booking(self):
        start_date = datetime.datetime(2024, 12, 25, 9, 0)
        end_date = datetime.datetime(2024, 12, 25, 14, 0)
        search_window = 15
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0),),
        ]
        results = schedule.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15), datetime.datetime(2024, 12, 25, 9, 30), datetime.datetime(2024, 12, 25, 9, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15), datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15), datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 13, 15), datetime.datetime(2024, 12, 25, 13, 30), datetime.datetime(2024, 12, 25, 13, 45),
        ]
        self.assertEqual(expected, results)

        search_window = 30
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 30),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 30),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 30),
            datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 13, 30),
        ]
        results = schedule.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertEqual(expected, results)

        end_date = datetime.datetime(2024, 12, 25, 13, 0)
        search_window = 60
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 10, 0),),
        ]
        expected = [
            datetime.datetime(2024, 12, 25, 10, 0),
            datetime.datetime(2024, 12, 25, 11, 0),
            datetime.datetime(2024, 12, 25, 12, 0),
        ]
        results = schedule.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertEqual(expected, results)

        end_date = datetime.datetime(2024, 12, 25, 12, 0)
        search_window = 60
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 14, 0),),
        ]
        expected = [
            datetime.datetime(2024, 12, 25, 9, 0),
            datetime.datetime(2024, 12, 25, 10, 0),
            datetime.datetime(2024, 12, 25, 11, 0),
        ]
        results = schedule.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertEqual(expected, results)

    def test_schedule_two_bookings(self):
        start_date = datetime.datetime(2024, 12, 25, 9, 0)
        end_date = datetime.datetime(2024, 12, 25, 14, 0)

        search_window = 60
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0),),
            (datetime.datetime(2024, 12, 25, 12, 15), datetime.datetime(2024, 12, 25, 13, 0),),
        ]

        expected = [
            datetime.datetime(2024, 12, 25, 9, 0),
            datetime.datetime(2024, 12, 25, 11, 0),
            datetime.datetime(2024, 12, 25, 13, 0),
        ]

        results = schedule.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertEqual(expected, results)

        # two from start working day
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 11, 0),),
            (datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 10, 0),),
        ]
        search_window = 15

        expected = [
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15), datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15), datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
            datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 13, 15), datetime.datetime(2024, 12, 25, 13, 30), datetime.datetime(2024, 12, 25, 13, 45),
        ]
        results = schedule.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertEqual(expected, results)

        # two in the end of the day
        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 14, 0),),
            (datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 13, 0),),
        ]

        expected = [
            datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 9, 15), datetime.datetime(2024, 12, 25, 9, 30), datetime.datetime(2024, 12, 25, 9, 45),
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15), datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15), datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45)
        ]
        results = schedule.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertEqual(expected, results)

        # two by edges

        trainer_bookings = [
            (datetime.datetime(2024, 12, 25, 9, 0), datetime.datetime(2024, 12, 25, 10, 0),),
            (datetime.datetime(2024, 12, 25, 13, 0), datetime.datetime(2024, 12, 25, 14, 0),),
        ]

        expected = [
            datetime.datetime(2024, 12, 25, 10, 0), datetime.datetime(2024, 12, 25, 10, 15), datetime.datetime(2024, 12, 25, 10, 30), datetime.datetime(2024, 12, 25, 10, 45),
            datetime.datetime(2024, 12, 25, 11, 0), datetime.datetime(2024, 12, 25, 11, 15), datetime.datetime(2024, 12, 25, 11, 30), datetime.datetime(2024, 12, 25, 11, 45),
            datetime.datetime(2024, 12, 25, 12, 0), datetime.datetime(2024, 12, 25, 12, 15), datetime.datetime(2024, 12, 25, 12, 30), datetime.datetime(2024, 12, 25, 12, 45),
        ]
        results = schedule.booking_time_discovery(start_date, end_date, trainer_bookings, search_window)
        self.assertEqual(expected, results)