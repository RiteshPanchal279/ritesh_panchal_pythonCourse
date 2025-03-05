# Q.1: Managing an Online Store Inventory Scenario:
# You manage an online store that sells various products. You need to keep track of which
# products are in stock and which are out of stock.


in_stock = {'laptop', 'mouse', 'keyboard', 'monitor'}
out_of_stock = {'printer', 'webcam'}

in_stock.add('printer')
in_stock.add('tablet')

# Remove 'printer' from out_of_stock if it was there
out_of_stock.discard('printer')

# Move 'monitor' to out_of_stock
in_stock.remove('monitor')  # Remove from in_stock
out_of_stock.add('monitor')  # Add to out_of_stock

#  Find products that are either in stock or out of stock, but not both
exclusive_products = in_stock.symmetric_difference(out_of_stock)

# Step 6: Calculate available products for sale (all in_stock products)
available_for_sale = in_stock.copy()

# Output results
print("In Stock:", in_stock)
print("Out of Stock:", out_of_stock)
print("Exclusive Products (either in stock or out of stock, but not both):", exclusive_products)
print("Available for Sale:", available_for_sale)


# Q.2: Student Enrollment System Scenario:
# You are developing a student enrollment system for a university. The university offers
# courses in different subjects, and some students are enrolled in multiple courses.

course_A={'Alice', 'Bob', 'Charlie'}
course_B={'Charlie', 'David', 'Eva'}

# sub qs 3
enroled_in_both=course_A.intersection(course_B)
print("The student who is enroled in both:",enroled_in_both)

# sub qs 4
all_student_from_both_course=course_A.union(course_B)

print("List all students who are enrolled in either course_A or course_B:",all_student_from_both_course)

# sub qs 5
student_are_noting_bCourse = course_A.difference(course_B)

print("Identify students who are enrolled in course_A but not in course_B:",student_are_noting_bCourse)

# sub qs 6

student_in_one_course = course_A.symmetric_difference(course_B)

print("Identify students who are enrolled in course_A but not in course_B:",student_in_one_course)





