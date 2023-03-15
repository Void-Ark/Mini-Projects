import re 

def style(val) : 
    if val < 10 : 
        return '0'+str(val)
    else : 
        return str(val)

def add_time(start, duration, day=None):
    new_time = ''
    hour, min = map(int, start[:-2].split(':'))
    if start[-2:] == 'PM': 
        hour += 12 
    #print(hour)
    
    d_hour, d_min = map(int, duration.split(':'))
    extra = ''
    
    hour += d_hour + (d_min+min)//60 
    min = (d_min + min)%60 
    #print(hour)
    
    am_pm = 'PM' if hour%24 >= 12 or () else 'AM'
    no_of_days = hour//24
    
    hour %= 12 
    if hour == 0 : hour = 12
    
    
    if not day :  
        if no_of_days <= 0 : 
            new_time = f"{hour}:{style(min)} {am_pm}"
        elif no_of_days == 1 : 
            new_time = f"{hour}:{style(min)} {am_pm} (next day)"
        else : 
            new_time = f"{hour}:{style(min)} {am_pm} ({no_of_days} days later)" 
            
    else : 
        days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
 
        for i in range(len(days)) :
            if re.search(days[i], day, re.IGNORECASE) :
                day = days[(i+no_of_days)%7]
                break 
            else : 
                continue 
            
        if no_of_days <= 0 : 
            new_time = f"{hour}:{style(min)} {am_pm}, {day}"
        elif no_of_days == 1 : 
            new_time = f"{hour}:{style(min)} {am_pm}, {day} (next day)"
        else : 
            new_time = f"{hour}:{style(min)} {am_pm}, {day} ({no_of_days} days later)" 
        
    return new_time

#print(add_time("11:59 PM", "24:05", "Wednesday")) #23+25= 48:04