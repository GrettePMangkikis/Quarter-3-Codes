names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

days=["monday", "tuesday", "wednesday", "thursday", "friday"]
daily_totals = []
for day_index in range(len(days)):
    total=0
    for person_index in range(len(steps)):
        total=total+steps[person_index][day_index]
    daily_totals.append(total)
    print(f"{days[day_index]} total steps: {total}")
max_steps=max(daily_totals)
most_active=days[daily_totals.index(max_steps)]
print("Most active day:",most_active)