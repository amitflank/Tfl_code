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
								
								'Wendsday': {
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
								
								'Wendsday': {
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
mentor_info_june = {
	'Devon': {
		'hard_dates': [i for i in range (2,6)] + [7] + [i for i in range (9,13)] + [14] + [i for i in range (16,20)] + [21] + [i for i in range (23,27)]+ [28] + [30],
		'hours_wanted': 10,
		'soft_dates' : []
	},
	'Kate D': {
		'hard_dates': [i for i in range(3,8)] + [i for i in range(10,14)] + [17] + [24] + [31],
		'hours_wanted': 20,
		'soft_dates' : []
	},
	'Braxton': {
		'hard_dates': [1],
		'hours_wanted': 20, 
		'soft_dates' : []
	},
	'Delcie':{
		'hard_dates': [8],
		'hours_wanted': 20, 
		'soft_dates' : []
	},
	'Mitch': {
		'hard_dates': [15],
		'hours_wanted': 20,
		'soft_dates' : []
	},
	'Levi': {
		'hard_dates': [22],
		'hours_wanted': 20,
		'soft_dates' : []
	},
	'Kate S': {
		'hard_dates': [1] + [7] + [8] + [14] + [15] + [22] + [28] + [29],
		'hours_wanted': 20,
		'soft_dates' : [] 
	}
}