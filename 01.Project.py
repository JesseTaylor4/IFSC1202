time = int(input("Enter number of days: "))
years = time // 365
time = time % 365
print("years: ", years)
weeks = time // 7
time = time % 7
print("weeks: ", weeks)
print("days: ", time)
