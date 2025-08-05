def say_hello(name):
    salutations = "Hello, " + name
    print(salutations)

say_hello("VS Code")

def say_day_of_week(date):
    """
    Prints the day of the week for the given date.

    Args:
        date (datetime.date or datetime.datetime): The date to get the day of the week from.
    """
    import datetime
    day_of_week = date.strftime("%A")
    print(f"Today is {day_of_week}")        
