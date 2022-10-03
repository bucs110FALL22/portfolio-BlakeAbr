import random
#Part A
classes_per_week = 3

weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)

cost_per_class = cost_per_week / classes_per_week

print("Cost per week:", cost_per_week)
print("Cost per class:", cost_per_class )
## Only two variables I created was classes_per_week and cost_per_class
print(classes_per_week, type(classes_per_week), cost_per_class, type(cost_per_class))


#Part B
my_list = ["Blake", 2, 6.9, "doug dimmadome owner of the dimmsdale dimmadome", 10]
print(random.choice(my_list))


