"""
metrics:
	hours wanted per pay period: 5
	availability days: 3
	consecutive days (5 bad 6+ terrible) 3
	variety: every mentor should work with everyone else at least once: 1
	bleed-over: Have at least 1 mentor from the previous day working
"""
import datetime as dt
import operator
from calendar import monthrange
from typing import List, Dict, Union
from bisect import bisect_left
import numpy as np
from bad_db import seasonal_shift_info, mentor_info_june

 



def get_truth(inp, relate, cut):
	ops = {'>': operator.gt,
			'<': operator.lt,
			'>=': operator.ge,
			'<=': operator.le,
			'==': operator.eq}
	return ops[relate](inp, cut)

def BinarySearch(a, x):
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
		"""checks if adding new shifts leads to overtime"""
		return self.hours_pay + shift_len < 80 
		
	def __radd__(self, other):
		return other + self.get_available_hours()
	
	def get_available_hours(self) -> int:
		"""get remaining hours this mentor wants in current pay period"""
		return self.hours_wanted - self.hours_pay
	

class Day():
	"""Class represents a scheduled Day"""

	def __init__(self, date_info: dt.datetime):
		self.date_info = date_info
		self.is_weekday = date_info.weekday() < 5
		self.season = self.get_season()
		self.shifts = self.get_shifts(self.season)
		self.mentors_on_shift = {shift: None for shift in self.shifts} 
		self.total_hours = sum(self.shifts.values())
		self.assigned_hours = 0
		self.potential_mentors: List[Mentor] = []
		self.priority_value = 0
		

	def get_mentor_days(self) -> int:
		"""Get number of mentors who can still theoretically work on this day"""
		return len(self.potential_mentors)

	def get_available_mentor_hours(self) -> int:
		"""get number of hours mentors could still theoretically work on this day"""
		return sum(self.potential_mentors)

	def add_potential_mentor(self, mentor: Mentor):
		"""Adds mentor to potential_mentors field"""
		self.potential_mentors.append(mentor)
	
	def available_shifts(self) -> bool:
		"""Check if this day has any more shifts available. Returns a bool"""
		return None in self.mentors_on_shift.values()

	def add_shift(self, mentor: Mentor) -> bool:
		"""Tries to add mentor to next available open shift slot. Returns bool indicating success status.
		Raises error if  empty shift is not available"""
		for shift, slot in self.mentors_on_shift.items():
			if slot is None:
				legal_add = mentor.legal_shift_add(self.shifts[shift])

				if legal_add:
					self.mentors_on_shift[shift] = mentor
					mentor.hours_pay += self.shifts[shift]
					return True
				return False

		raise ValueError("Tried to fill shift in full day, this should never happen")

	def add_lowest_shift(self, mentor: Mentor) -> bool:
		"""adds mentor to shift with lowest number of hours required. Useful for avoiding overtime.
		Returns bool indicating success status"""
		lowest_hours = 100
		cur_shift = None

		for shift, slot in self.mentors_on_shift.items():
			if slot is None:

				shift_len = self.shifts[shift]
				if shift_len < lowest_hours:
					lowest_hours = shift_len
					cur_shift = shift

		legal_add = mentor.legal_shift_add(lowest_hours)

		if legal_add:
			self.mentors_on_shift[cur_shift] = mentor
			mentor.hours_pay += self.shifts[shift]
			return True
	
		return False

	def remove_shift(self):
		pass

	def get_needed_hours(self) -> int:
		return self.total_hours - self.assigned_hours

	def get_season(self) -> str:
		"""get season to which this day belongs"""
		for season, season_info in seasonal_shift_info.items():

			start_date = season_info['dates']['start'].date()
			end_date = season_info['dates']['end'].date() 

			if self.date_info.date() >= start_date and self.date_info.date() <= end_date:
				return season
		
		raise ValueError('Could not find season that matched given date')
	
	def get_shifts(self, season: str) -> Dict[str, int]:
		"""get the shifts required for this day"""
		if self.is_weekday:
			return seasonal_shift_info[season]['weekday_shifts'].copy()
		return seasonal_shift_info[season]['weekend_shifts'].copy()

class Schedule():

	def __init__(self, year: int, month: int, len_p1: int):
		self.len_p1 = len_p1
		len_month = monthrange(year, month)[1] #get num days in month, used to calc len_p2
		self.mentors = self.create_mentor_info(len_p1, '<=', len_p1)
		self.pay_days = self.create_pay_days(start_date = dt.datetime(year, month, 1), end_date= dt.datetime(year, month, len_p1))
		self.assigned_days: List[Day] = []
		self.assign_all_shifts()
		self.mentors = self.create_mentor_info(len_month - len_p1, '<=', len_month)
		self.pay_days = self.create_pay_days(start_date = dt.datetime(year, month, len_month - len_p1 + 1), end_date= dt.datetime(year, month, len_month), offset = len_p1)
		self.assign_all_shifts()

	def create_mentor_info(self, len_pay: int, comparator: str, end_day: int = 1) -> List[Mentor]:
		"""Create initial default list of mentors for a given pay period"""
		mentor_list = [None for _ in mentor_info_june]
		idx = 0
		for name, info in mentor_info_june.items():
			c_info = info.copy()
			c_info['hard_dates'] = [date for date in info['hard_dates'] if get_truth(date, comparator, end_day)] 
			c_info['name'] = name
			c_info['hours_wanted'] = c_info['hours_wanted'] * 2 #2 weeks
			c_info['len_pay'] = len_pay

			mentor_list[idx] = Mentor(**c_info)
			idx += 1
		
		return mentor_list


	def create_pay_days(self, start_date: dt.datetime, end_date: dt.datetime, offset: int = 0) -> List[Day]:
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

		while cur_date <= end_date:
			days[idx] = Day(cur_date)
			cur_date += dt.timedelta(days=1)
			idx += 1
		
		for mentor in self.mentors:

			#gets all available days in pay period which mentor can work
			available_days = [i for i in range(start_date.day, end_date.day + 1)]
			available_days = [x for x in available_days if x not in mentor.hard_dates] 

			#assign which mentors can work on given day
			for date in available_days:
				days[date - offset - 1].add_potential_mentor(mentor)

		return days

	def prioritize_days(self):
		"""We prioritize using mentors available for each days shift over total number of workable shifts over pay period"""
		total_available_days = sum([day.get_mentor_days() for day in self.pay_days]) #total workable shifts
		for day in self.pay_days:
			day.priority_value = (day.get_mentor_days() / total_available_days) 

		self.pay_days.sort(key=lambda day: (day.priority_value,  -day.get_available_mentor_hours())) #costume sort

	def assign_shift(self) -> Union[int, Mentor]:
		"""assign first shift in highest prio day if possible.
		
		Returns:
			1 if all Mentors lost a day otherwise returns mentor who was assigned. Useful for updating mentor eligibility """
		day = self.pay_days[0] #ordered list so highest prio day is always first
		update_mentors = True #prevents double updating mentors available days on recursive calls
		highest_prio = -100
		cur_mentor = None

		for mentor in day.potential_mentors:
			cur_prio = mentor.get_available_hours() / mentor.days_left

			#update mentor if we get better prio
			if cur_prio > highest_prio:
				highest_prio = cur_prio
				cur_mentor = mentor

		success = day.add_shift(cur_mentor)

		#if we can't assign due to overtime we will look for a shift with less hours
		if not success:
			success = day.add_lowest_shift(cur_mentor)

			#if we still can't assign we will remove this mentor and try someone else
			if not success:
				update_mentors = False #recursive call will update mentor days don't assign in this stack call
				day.potential_mentors.remove(cur_mentor)
				self.prioritize_days() #mentor deletion might change day prio's so lets resort days
				self.assign_shift()

		if update_mentors:

			#if all shifts are full or we are out of mentors we are done w/this day
			if len(day.potential_mentors) == 1 or not day.available_shifts(): #check one b/c have not del assigned mentor yet
				for mentor in day.potential_mentors:
					mentor.days_left -= 1 
				self.assigned_days.append(self.pay_days[0])
				del self.pay_days[0] #remove day
				return 1

			else: 
				cur_mentor.days_left -= 1
				day.potential_mentors.remove(cur_mentor)
				return cur_mentor


	def mentor_cleanup(self, mentor_update: Union[int, Mentor]):
		"""Removes mentors who are no longer eligible to work this pay period for potential mentors in all days"""
		mentors_to_update = []

		if type(mentor_update) is Mentor: #we can just check passed mentor
			if mentor_update.days_left == 0 or mentor_update.get_available_hours() <= 0:
				mentors_to_update.append(mentor_update)
		elif type(mentor_update) is int: #need to check all mentors
			for mentor in self.mentors:
				if mentor.days_left == 0 or mentor.get_available_hours() <= 0:
					mentors_to_update.append(mentor)
		else:
			raise ValueError("got bad datatype {0} must pas int or Mentor".format(type(mentor_update)))

		for day in self.pay_days:
			day.potential_mentors = [mentor for mentor in day.potential_mentors if mentor not in mentors_to_update]

			
	def assign_all_shifts(self):
		"""Assigns all shifts for given pay period"""
		unassigned_days = len(self.pay_days)

		while unassigned_days > 0:
			#not particularly efficient since we end up needing to sort entire list for every single lookup as values change constantly
			#However can't think of easy clean solution that can replicate this functionality and it's not worth the hassle
			#to be to clever about it.
			self.prioritize_days()
			mentor = self.assign_shift()
			self.mentor_cleanup(mentor)
			unassigned_days = len(self.pay_days)
		
		self.assigned_days.sort(key=lambda day:(day.date_info.day)) #sort days in calendar order

	def get_consecutive_day_cost(self, c_days: int) -> int:
		"""Calculates penalty for mentors working to many consecutive shifts, returns int"""
		cost = c_days - 4
		return cost * cost if cost > 0 else 0

	def track_diversity(self, m_vec: np.array, day, mentor_idxs):
		num_mentors = len(mentor_idxs)
		mentors_working = [mentor for mentor in day.mentors_on_shift.values() if mentor != None] #get mentor names
		v_mentors = np.zeros(num_mentors) #tracks mentors working this day as vector
			
		for mentor in mentors_working:
			idx = mentor_idxs[mentor]
			v_mentors[idx] += 1 #update mentor vector representation of this day
			
		for mentor in mentors_working:
			idx = mentor_idxs[mentor]
			m_vec[idx]+= v_mentors #update mentors vector

		#don't think i need a return since pass by reference but check 
	
	def update_c_days(self, day: Day, con_men_days: List[str], final_day: bool = False) -> int:
		"""updates consecutive mentor list and returns cost of any evaluated mentors on passed day"""
		mentors_working = [mentor for mentor in day.mentors_on_shift.values() if mentor != None] #get mentor names
		days_cost = 0

		for mentor in self.mentors:
			if mentor.name in mentors_working and not final_day:
				con_men_days[mentor.name] += 1
			else:
				c_days = con_men_days[mentor.name]
				con_men_days[mentor.name] = 0
				days_cost += self.get_consecutive_day_cost(c_days)

		return days_cost

	def get_hour_cost(self) -> int:
		"""Calculate the penalty for mismatch between mentors desired hours and actual"""
		total_cost = 0
		for mentor in self.mentors:
			diff = mentor.hours_wanted - mentor.hours_pay
			total_cost += diff * diff
		return total_cost

	def calc_score(self):
		first_pay = self.assigned_days[:self.len_p1]
		second_pay = self.assigned_days[self.len_p1:]

		mentor_idxs = {mentor.name: idx for idx, mentor in enumerate(self.mentors)} #assign vector location to each mentor
		con_men_days = {mentor.name: 0 for mentor in self.mentors} #tracks mentors consecutive days worked 

		num_mentors = len(mentor_idxs)
		mentor_vectors = np.zeros(num_mentors, num_mentors) 
		c_cost  = 0

		for day in self.assigned_days:
			self.track_diversity(mentor_vectors, day, mentor_idxs)
			c_cost += self.update_c_days(day, con_men_days)
		
		#Find sum total of unique mentors who have worked together
		#since vectors include their own idx we must remove 1 for each mentor
		shared_shifts = np.count_nonzero(mentor_vectors) - len(mentor_idxs) * 2 #use a scale factor of 2
		hour_cost = self.get_hour_cost()


			


my_sched = Schedule(2022, 6, 15)

for idx, day in enumerate(my_sched.assigned_days):
	print(idx, day.mentors_on_shift)

