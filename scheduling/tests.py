from typing import List, Dict
import pytest
from scheduler import Mentor, Day, Schedule


my_sched = Schedule(2022, 6, 15)
key_match = {'K': "Kinley", 'S': "Sav", 'Ka': "Kate", 'B': "Braxton", 'De': "Delcie",
				'M': "Mitch", 'D': "Devon"}


@staticmethod
@pytest.mark.parametrize("day, expected_mentor_symbol, key_match", [
		(my_sched.pay_days[0], ['S', 'Ka', 'B', 'M', 'D'], key_match),
		(my_sched.pay_days[1], ['S', 'Ka', 'B', 'D'], key_match),
		(my_sched.pay_days[2], ['Ka', 'B', 'D'], key_match),
		(my_sched.pay_days[3], ['Ka', 'B'], key_match),
		(my_sched.pay_days[4], ['Ka', 'B', 'M', 'D'], key_match),
		(my_sched.pay_days[5], ['Ka', 'B', 'M', 'D'], key_match),
		(my_sched.pay_days[6], ['K', 'Ka', 'B', 'M', 'D'], key_match),
		(my_sched.pay_days[7], ['K', 'Ka', 'B', 'M', 'D'], key_match),
		(my_sched.pay_days[8], ['K', 'Ka', 'B', 'M', 'D'], key_match),
		(my_sched.pay_days[9], ['K', 'Ka', 'B', 'M', 'D'], key_match),
		(my_sched.pay_days[10], ['K', 'Ka', 'B', 'M', 'D'], key_match),
		(my_sched.pay_days[11], ['K', 'Ka', 'B', 'M', 'D'], key_match),
		(my_sched.pay_days[12], ['K', 'Ka', 'M', 'D'], key_match),
		(my_sched.pay_days[13], ['S', 'K', 'Ka', 'M', 'D'], key_match),
		(my_sched.pay_days[14], ['S', 'K', 'Ka', 'M', 'D'], key_match),
	])
def test_pay_day_creation(day: Day, expected_mentor_symbol: List[str], key_match: Dict[str, str]):
	expected_mentors = [key_match[key] for key in expected_mentor_symbol]
	assert len(expected_mentors) == len(day.potential_mentors), "Found {0} mentors but expected {1} mentors in potential mentor list".format(day.potential_mentors, expected_mentors)
	for mentor in day.potential_mentors:
		assert mentor.name in expected_mentors, "Found {0} in potential mentors but not in expected mentor list {1}". format(mentor.name, expected_mentors)