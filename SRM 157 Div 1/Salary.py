import datetime
import time

class Salary(object):
    
    def howMuch(self, arrival, departure, wage):
        # Property instantiations
        arrival_temp = []
        departure_temp = []
        arrival_hour = departure_hour = total = 0
        # Input check
        if len(arrival) != len(departure):
            print("invalid input")
            return
        # If tuple contains more than one element, iterate and compare results from each tuple
        count = len(arrival)
        for i in range(count):
            # Convert arrival time to hours
            arrival_temp = time.strptime(arrival[i],'%H:%M:%S')
            arrival_sec = (datetime.timedelta(hours=arrival_temp.tm_hour,minutes=arrival_temp.tm_min,seconds=arrival_temp.tm_sec).total_seconds())
            arrival_hour = arrival_sec/3600
            print('Arrival', arrival_hour)
            # Convert departure time to hours
            departure_temp = time.strptime(departure[i],'%H:%M:%S')
            departure_sec = (datetime.timedelta(hours=departure_temp.tm_hour,minutes=departure_temp.tm_min,seconds=departure_temp.tm_sec).total_seconds())
            departure_hour = departure_sec/3600
            print('Departure', departure_hour)
            # Calculate total salary
            if arrival_hour <= 6:
                if departure_hour <= 6:
                    # 1.5 times wage for AM hours
                    total += (departure_hour - arrival_hour) * 1.5 * wage
                elif departure_hour <= 18:
                    # 1.5 times wage for AM hours
                    total += (6 - arrival_hour) * 1.5 * wage
                    # Add remaining regular paid wage
                    total += (departure_hour - 6) * wage
                else:
                    total += (6 - arrival_hour) * 1.5 * wage
                    total += (18 - 6) * wage
                    total += (departure_hour - 18) * 1.5 * wage
            elif arrival_hour <= 18:
                if departure_hour <= 18:
                    total += (departure_hour - arrival_hour) * wage
                else:
                    total += (18 - arrival_hour) * wage
                    total += (departure_hour - 18) * 1.5 * wage
            else:
                total += (departure_hour - arrival_hour) * 1.5 * wage
        print('---------------------------------------------------')
        print('Total paid:', int(total))
        
        return int(total)

x = Salary()
test_a = ("01:05:47", "16:48:12")
test_b = ("09:27:30", "21:17:59")

test_c = ("08:00:00", "13:00:00", "19:27:32")
test_d = ("12:00:00", "17:00:00", "20:48:10")

x.howMuch(test_a, test_b, 2000)
