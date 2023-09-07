import datetime as dt
import operator
from calendar import monthrange
from typing import List, Dict, Union, Tuple
from bisect import bisect_left
import numpy as np
from mentor_db import seasonal_shift_info, mentor_info, holidays


#utility functions
def get_truth(inp, relate, cut):
	"""This function lets you access operator through an argument allowing you to avoid logic with many if statements
	You are not required to use it but it can simplify your logic"""
	ops = {'>': operator.gt,
			'<': operator.lt,
			'>=': operator.ge,
			'<=': operator.le,
			'==': operator.eq}
	return ops[relate](inp, cut)



def BinarySearch(a, x):
	"""Binary search algorithm is very useful for efficiently looking up values in a sorted list. It can do so in O(log(N)) compared to 
    O(N) for brute force. In fact it is the mathematically most efficient way of looking up elements in a generic sorted list"""
	i = bisect_left(a, x)
	if i != len(a) and a[i] == x:
		return i
	else:
		return -1

class Mentor():
    """represents Mentor specific scheduling information for a single pay period"""
    def __init__(self, name: str, hours_wanted: int, hard_dates: List[int], soft_dates: List[int], len_pay: int):
        self.name = name
        self.hours_wanted =  hours_wanted
        self.hard_dates = hard_dates
        self.soft_dates = soft_dates

        self.hours_pay = 0
        self.days_left = len_pay - len(hard_dates)
	
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def legal_shift_add(self, shift_len: int):
        """checks if adding new shifts leads to overtime, overtime is defined as more then 40 hours per week over a pay period.
        So an employee can work over 40 hours in a week as long as they don't average over 40 hours per pay period"""
        pass
	
    def __radd__(self, other):
        """Lets operator override the addition argument for mentors. We will have the result spit out the sum of both mentors
	  availabe hours. Hint: You might need a method call here. """
	
    def get_available_hours(self) -> int:
        """get remaining hours this mentor wants in current pay period"""
	
	

class Day():
	"""Class represents a scheduled Day"""

	def __init__(self, date_info: dt.datetime):
		self.date_info = date_info
		self.week_day_map = {'Sunday': 6, 'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5}
		self.weekday = date_info.weekday()
		self.season = self.get_season()
		self.shifts = self.get_shifts(self.season, self.weekday)
		self.mentors_on_shift: Dict[str, Mentor] = {shift: None for shift in self.shifts} 
		self.total_hours = sum(self.shifts.values())
		self.assigned_hours = 0
		self.potential_mentors: List[Mentor] = []
		self.priority_value = 0
		

	def get_mentor_days(self) -> int:
		"""Get number of mentors who can still theoretically work on this day"""
		pass


	def get_available_mentor_hours(self) -> int:
		"""get number of hours mentors could still theoretically work on this day"""
		pass


	def add_potential_mentor(self, mentor: Mentor):
		"""Adds mentor to potential_mentors field"""
		pass

	
	def available_shifts(self) -> bool:
		"""Check if this day has any more shifts available. Returns a bool"""
		pass

	def add_shift(self, mentor: Mentor) -> bool:
		"""Tries to add mentor to next available open shift slot. Returns bool indicating success status.
		Raises error if  empty shift is not available"""
		pass


	def add_lowest_shift(self, mentor: Mentor) -> bool:
		"""adds mentor to shift with lowest number of hours required. Useful for avoiding overtime.
		Returns bool indicating success status"""
		pass

	def remove_shift(self):
		pass

	def get_needed_hours(self) -> int:
		"""returns the number of additional hours needed to be assigned on this day"""
		return self.total_hours - self.assigned_hours

	def get_season(self) -> str:
		"""get season to which this day belongs"""
		for season, season_info in seasonal_shift_info.items():

			start_date = season_info.copy()['dates']['start'].date()
			end_date = season_info.copy()['dates']['end'].date() 

			cur_year = self.date_info.date().year

			if self.date_info.date() >= start_date and self.date_info.date() <= end_date:
				return season
			
			if self.date_info.date().replace(year =cur_year + 1) >= start_date and self.date_info.date().replace(year =cur_year + 1) <= end_date:
				return season
		
		
		raise ValueError('Could not find season that matched given date')
	
	def get_shifts(self, season: str, day: int) -> Dict[str, int]:
		"""get the shifts required for this day"""


class Schedule():

	def __init__(self, year: int, month: int, len_p1: int):
		self.week_day_map = {'Sunday': 6, 'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5}
		self.len_p1 = len_p1
		self.month = month
		self.year = year
		len_month = monthrange(year, month)[1] #get num days in month, used to calc len_p2
		self.m1 = self.create_mentor_info(len_p1, '<=', len_p1)
		self.pay1 = self.create_pay_days(self.m1, dt.datetime(year, month, 1), dt.datetime(year, month, len_p1))
		self.assigned_days: List[Day] = []

		self.assign_all_shifts(self.pay1, self.m1)
		self.m2 = self.create_mentor_info(len_month - len_p1, '>', len_p1)
		self.pay2 = self.create_pay_days(self.m2, start_date = dt.datetime(year, month, len_month - (len_month - len_p1) + 1), end_date= dt.datetime(year, month, len_month), offset = len_p1)
		self.assign_all_shifts(self.pay2, self.m2)

	def get_dates_of_weekday(self, day: str) -> List[int]:
		"""given a day of the week ex: Sunday, return all dates in passed month that correspond to that weekday"""

	def get_all_weekday_dates(self, weekdays: List[str]):
		"""Given a list of weekdays ex [Sunday, Monday], return all date in month that correspond that fall on those days.
	    sort the days and then return them."""


	def hard_date_adj(self, hard_dates: List[int], weekdays: List[str], behavior: str) -> List[int]:
		if len(weekdays) == 0:
			return hard_dates
		
		len_month = monthrange(self.year, self.month)[1]

		allowed_dates = self.get_all_weekday_dates(weekdays)

		if behavior[0] == "Inv":
			res_dates = range(1, len_month + 1)
			res_dates = [date for date in res_dates if date not in allowed_dates]
			return res_dates
		elif behavior[0] == "Pe":
			res_dates = [date for date in hard_dates if date not in allowed_dates]
			return res_dates
		elif behavior[0] == "Re":
			res_dates = list(np.unique(hard_dates + allowed_dates))
			res_dates.sort()
			return res_dates
		else:
			raise ValueError("Got bad behavior keyword {0}".format(behavior))

	def create_mentor_info(self, len_pay: int, comparator: str, end_day: int = 1) -> List[Mentor]:
		"""Create initial default list of mentors for a given pay period"""
		mentor_list = [None for _ in mentor_info]
		idx = 0

		for name, info in mentor_info.items():
			c_info = info.copy()
			new_dates = self.hard_date_adj(info['hard_dates'], info["weekdays"], info["weekday_behavior"])
			c_info['hard_dates'] = [date for date in new_dates if get_truth(date, comparator, end_day)] 
			c_info['name'] = name
			c_info['hours_wanted'] = c_info['hours_wanted'] * 2 #2 weeks
			c_info['len_pay'] = len_pay
			c_info = {'hard_dates': c_info['hard_dates'], 'name': name, 'hours_wanted': c_info['hours_wanted'], 'len_pay': len_pay, 'soft_dates' : c_info['soft_dates']}

            #this is an unpacking operation. If the dict keys match the argument names of a function we can easily dump them into the function call
            #making our lives much easier. This can be a very clean approach to calling methods with many arguments. 
			mentor_list[idx] = Mentor(**c_info) 
			 
			idx += 1
		
		return mentor_list


	def create_pay_days(self, mentors: List[Mentor], start_date: dt.datetime, end_date: dt.datetime, offset: int = 0) -> List[Day]:
		"""Create initial set of empty days for a given pay period
		
		Args:
			start_date: start of pay period
			end_date: end of pay period
			offset: used in second pay period for indexing purposes, should be equal to length of first pay period
		"""
		cur_date = start_date
		num_days = end_date.day - start_date.day + 1
		days: List[Day] = [None for _ in range(num_days)]
		idx  = 0

        #create a list of days for each day in range [cur_date, end_date]. 
		while cur_date <= end_date:
			days[idx] = Day(cur_date)
			cur_date += dt.timedelta(days=1)
			idx += 1
		
		for mentor in mentors:

			#gets all available days in pay period which mentor can work
			available_days = [i for i in range(start_date.day, end_date.day + 1)]
			available_days = [x for x in available_days if x not in mentor.hard_dates] 
			#assign which mentors can work on given day
			for date in available_days:
				days[date - offset - 1].add_potential_mentor(mentor)

		return days

	def prioritize_days(self, pay_days: List[Day]):
		"""We prioritize using mentors available for each days shift over total number of workable shifts over pay period"""
		total_available_days = sum([day.get_mentor_days() for day in pay_days]) #total workable shifts
		for day in pay_days:
			day.priority_value = (day.get_mentor_days() / (total_available_days + 1)) 


        #We can specify how the sort method should work using lambda, the keyword for creating inline anonymous functions.
        #What we are doing here is saying first sort the days in pay_days by the priority value in each day and if there is a tie
        #sort by the negative of that days available mentor hours. Remember the sort method will sort in ascending order so by adding this negative term 
        # we are effectively telling it to sort in descending order. 
        # This is a really powerful tool as it allows us to use sort on any type as long as we specify the criteria for the sort. 
		pay_days.sort(key=lambda day: (day.priority_value,  -day.get_available_mentor_hours())) 

	def assign_shift(self, pay_days: List[Day]) -> Union[int, Mentor]:
		"""assign first shift in highest prio day if possible.
		
		Returns:
			1 if all Mentors lost a day otherwise returns mentor who was assigned. Useful for updating mentor eligibility """
		day = pay_days[0] #ordered list so highest prio day is always first
		update_mentors = True #prevents double updating mentors available days on recursive calls
		highest_prio = -100
		cur_mentor = None


        #update highest_prio and cur_mentor. Priority value can be derived by taking a mentors available hours
        #divided by the number of additional days they can work this month. If a mentor has highest
        # priority make update to current mentor. Bonus points if you can explain the logic behind this algorithm, add explanation as a comment. 
        #Hint: do you need to check all mentors? 


        #If no mentor can work this day update assigned days and del pay_days[0]. Return 1 indicating we are done. 

		success = day.add_shift(cur_mentor)

		#if we can't assign due to overtime we will look for a shift with less hours


		#if we still can't assign we will remove this mentor and try someone else. Will need to recursively call
        # ourselves here. Remember to not update mentor days here as the recursive call will deal with that. 
        # will also need to resort days here as prio values may have changed. Finally assign shift.


		if update_mentors:

			#if all shifts are full or we are out of mentors we are done w/this day. Make sure to update all relevant class fields. 


    def mentor_cleanup(self, mentor_update: Union[int, Mentor], pay_days: List[Day], mentors: List[Mentor]):
        """Removes mentors who are no longer eligible to work this pay period for potential mentors in all days. Should update day.potential mentors"""
        pass

    def assign_all_shifts(self, pay_days: List[Day], mentors: List[Mentor]):
        """Assigns all shifts for given pay period"""
        unassigned_days = len(pay_days)

        #assign shifts in a loop as long as we still have unassigned days. Remember to do all you clean up at the end of each loop.

        self.assigned_days.sort(key=lambda day:(day.date_info.day)) #sort days in calendar order
