import sys
import csv
from scheduler import Schedule 
def pad_or_truncate(some_list, target_len):
    return some_list[:target_len] + ['']*(target_len - len(some_list))

def write_to_csv(schedule: Schedule, file_name: str):
    """Writes some schedule to a csv file with passed name"""
    num_mentor = len(schedule.m1)

    with open(file_name, 'w') as output:
        writer = csv.writer(output)
        row = ['date', 'a_shift', 'b_shift', 'c-shift', '', 'Mentor', 'Pay1 hours', 'Pay2 hours', 'Hours Wanted']
        writer.writerow(row)
        for idx, day in enumerate(schedule.assigned_days):
            row = [idx + 1]
            for _, value in day.mentors_on_shift.items():
                if value is None:
                    row.append('Not assigned')
                else:
                    row.append(value)

            #add mentor information we have any mentors left
            if idx < num_mentor:
                row = pad_or_truncate(row, 9)
                row[5] = schedule.m1[idx].name
                row[6] =  schedule.m1[idx].hours_pay
                row[7] = schedule.m2[idx].hours_pay
                row[8] = schedule.m1[idx].hours_wanted
            writer.writerow(row)



def valid_input(idx: int, inp: str) -> bool:
    """checks if passed input is a legal value for the given index."""
    if idx == 0 or idx == 1:
        try:
            int(inp)
            print("got bad filename no action was taken")
            return False
        except ValueError:
            return True
        except:
            return False
    elif idx == 2:
        try: 
            assert int(inp) > 2000 and int(inp) < 3000
            return True
        except:
            print("got bad year value: {0}, no action was taken".format(inp))
            return False
    elif idx == 3:
        try: 
            assert int(inp) >= 1 and int(inp) <= 12
            return True
        except:
            print("got bad month value: {0}, no action was taken".format(inp))
            return False
    elif idx == 4:
        try: 
            assert int(inp) >= 1 and int(inp) <= 31
            return True
        except:
            print("got bad pay period length: {0}, no action was taken".format(inp))
            return False
    else:
        print('must have exactly four input arguments')
        return False 

if __name__ == "__main__":
    valid_in = True
    if len(sys.argv) != 5: #Not a typo, we ignored the call to this file 
        print('must have exactly four input arguments')
    else:    
        for i, arg in enumerate(sys.argv):
            valid_in = valid_input(i, arg) and valid_in

        if valid_in:
            file_name =  sys.argv[1] + '.csv'
            write_to_csv(Schedule(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])), file_name)