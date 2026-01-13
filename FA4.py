names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

total_steps=[]

for person_steps in steps:
    total_steps.append(sum(person_steps))
    
max_steps=max(total_steps)
max_index=total_steps.index(max_steps)
min_steps=min(total_steps)
diff = max_steps-min_steps

for i in range(len(names)):
    print(names[i] ,  "total steps:", total_steps[i]) 
    
print("person with the highest total steps:") 
print(names[max_index], "with", max_steps, "steps")
print("the difference between the highest and lowest:", diff) 

