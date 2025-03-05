# 1 You are helping a restaurant manage its menu. The restaurant has a regular menu and a special weekend menu. 
# Tasks: 

# 1. Create a set regular_menu with items 'pizza', 'burger', 'salad', and 'pasta'. 

# 2. Create another set weekend_menu with items 'steak', 'salmon', 'pasta', and 'wine'. 

# 3. Find out which items are available on both the regular and weekend menus.

#  4. Determine the items that are only available on the weekend. 

# 5. Add a new item 'dessert' to both menus.

#  6. The restaurant decides to stop offering 'burger'. Remove it from the regular menu.


regular_menu={'pizza', 'burger', 'salad',  'pasta'}
weekend_menu={'steak', 'salmon', 'pasta', 'wine'}

item_both=regular_menu.intersection(weekend_menu)
print("items are available on both the regular and weekend menus: ",item_both)

item_only_in_weekend=weekend_menu.difference(regular_menu)
print("items that are only available on the weekend: ",item_only_in_weekend)

regular_menu.add('dessert')
weekend_menu.add('dessert')

print("After add dessert in regular_menu",regular_menu)
print("After add dessert in weekend_menu",weekend_menu)

regular_menu.remove('burger')
print("After remove burger",regular_menu)



# 2 Event Management System 

# Scenario: You are organizing a large event and need to manage the list of attendees. Some attendees have VIP access, while others do not. 

# Tasks: 1. Create a set of attendees with names 'John', 'Jane', 'Emily', and 'Michael'. 

# 2. Create a frozenset vip_attendees with names 'Jane' and 'Michael'. 

# 3. A new attendee 'Sarah' registers for the event. Add her to the attendees set. 

# 4. Check if 'Emily' is a VIP attendee.

#  5. Find out which attendees have either regular or VIP access but not both. 6. List all attendees with either regular or VIP access.


attendees={'John', 'Jane', 'Emily','Michael'}
vip_attendees={'Jane','Michael'}

attendees.add('Sarah')

is_emily_vip = 'Emily' in vip_attendees
print(f"Is Emily a VIP attendee? {is_emily_vip}")

all_attendees = attendees | vip_attendees  # Union of both sets
print(f"All attendees: {all_attendees}")





