import datetime as dt

seasonal_shift_info = {
	'summer': {
		'dates': {
				'start': dt.datetime(dt.date.today().year, 5, 1), 
				'end':  dt.datetime(dt.date.today().year, 7, 31)
				},
		'shift_info': {
				'Sunday': {
					'a_shift': 9,
					'b_shift': 9
					}, 
				'Monday': {
					'a_shift': 6,
					'b_shift': 7,
					'c_shift': 3
				},
				'Tuesday': {
					'a_shift': 7,
					'b_shift': 7,
					'c_shift': 3
				},
								
				'Wednesday': {
					'a_shift': 7,
					'b_shift': 7,
					'c_shift': 3
				},
				'Thursday': {
					'a_shift': 7,
					'b_shift': 7,
					'c_shift': 3
				},
				'Friday': {
					'a_shift': 7,
					'b_shift': 7,
					'c_shift': 3
				},
				'Saturday': {
					'a_shift': 7,
					'b_shift': 7,
					'c_shift': 3
				},
			},
		},

	'winter': {
		'dates': {
			'start': dt.datetime(dt.date.today().year, 8, 1), 
			'end':  dt.datetime(dt.date.today().year + 1, 4, 30)
			},
		'shift_info': {
				'Sunday': {
					'a_shift': 9,
					'b_shift': 9
					}, 
				'Monday': {
					'a_shift': 6,
					'b_shift': 6,
					'c_shift': 3
					},
				'Tuesday': {
					'a_shift': 6,
					'b_shift': 6,
					'c_shift': 3
					},				
				'Wednesday': {
					'a_shift': 6,
					'b_shift': 6,
					},
				'Thursday': {
					'a_shift': 6,
					'b_shift': 6,
					'c_shift': 3
				},
				'Friday': {
					'a_shift': 8,
					'b_shift': 8,
					'c_shift': 3
				},
				'Saturday': {
					'a_shift': 11,
					'b_shift': 11,
					'c_shift': 4
				},
			},
		},
	}

#June info
mentor_info = {
	'Devon': {
		'hard_dates': [1]+[2]+[4]+[6]+[8]+[9]+[11]+[13]+[15]+[16]+[18]+[20]+[22]+[23]+[25]+[27]+[29]+[30],
		'hours_wanted': 14,
		'soft_dates' : []
	},
	'Kate D': {
		'hard_dates': [7]+[11]+[14]+[21]+[25]+[28],
		'hours_wanted': 20,
		'soft_dates' : []
	},
	'Delcie':{
		'hard_dates': [3],
		'hours_wanted': 20, 
		'soft_dates' : []
	},
	'Braxton': {
		'hard_dates': [10],
		'hours_wanted': 20, 
		'soft_dates' : []
	},
	'Mitch': {
		'hard_dates': [11]+[17],
		'hours_wanted': 20,
		'soft_dates' : []
	},
	'Levi': {
		'hard_dates': [24],
		'hours_wanted': 20,
		'soft_dates' : []
	},
	'Kate S': {
		'hard_dates': [4]+[5]+[12]+[18]+[19]+[25]+[26],
		'hours_wanted': 15,
		'soft_dates' : [] 
	}
}