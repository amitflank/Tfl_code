import datetime as dt

seasonal_shift_info = {
					'summer': {
							'dates': {
									'start': dt.datetime(dt.date.today().year, 5, 1), 
									'end':  dt.datetime(dt.date.today().year, 8, 1)
									},
							'weekday_shifts': {
								'a_shift': 7,
								'b_shift': 7,
								'c_shift': 3
									},
							'weekend_shifts': {
								'a_shift': 10,
								'b_shift': 10,
								'c_shift': 6
									}
								},

					'winter': {
							'dates': {
								'start': dt.date(dt.date.today().year, 8, 2), 
								'end':  dt.date(dt.date.today().year + 1, 4, 30)
									},
							'weekday_shifts': {
								'a_shift': 6,
								'b_shift': 6,
								'c_shift': 3
									},
							'weekend_shifts': {
								'a_shift': 10,
								'b_shift': 10,
								'c_shift': 6
									}
								},
						}

#June info
mentor_info_june = {
	'Sav': {
		'hard_dates': [i for i in range(3,14)] + [i for i in range(24, 28)],
		'hours_wanted': 20,
		'soft_dates' : [] 
	},
	'Kinley': {
		'hard_dates': [i for i in range(1,7)] + [i for i in range(22, 26)], #range not end inclusive so +1 to it
		'hours_wanted': 40, 
		'soft_dates' : []
	},  
	'Kate': {
		'hard_dates': [],
		'hours_wanted': 30,
		'soft_dates' : []
	},
	'Braxton': {
		'hard_dates': [i for i in range(13, 19)],
		'hours_wanted': 40, 
		'soft_dates' : []
	},
	'Delcie':{
		'hard_dates': [i for i in range(1, 17)],
		'hours_wanted': 40, 
		'soft_dates' : []
	},
	'Mitch': {
		'hard_dates': [i for i in range(2, 5)],
		'hours_wanted': 30,
		'soft_dates' : []
	},
	'Devon': {
		'hard_dates': [4] + [i for i in range(17, 20)] + [i for i in range(26, 30)],
		'hours_wanted': 20,
		'soft_dates' : []
	}
}