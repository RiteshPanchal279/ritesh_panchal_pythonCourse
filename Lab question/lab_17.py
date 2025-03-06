# You have a list of employee records, and you need to create a new list that contains
# the names of employees who work in the 'Sales' department, all in uppercase
employees = [
{"name": "John Doe", "department": "Sales"},
{"name": "Jane Smith", "department": "Marketing"},
{"name": "Emily Johnson", "department": "Sales"},
{"name": "Michael Brown", "department": "HR"}
]

my_ans=[]
for dict in employees:
   if dict["department"]=="Sales":
      my_ans.append(dict["name"].upper())

print(my_ans)




# You have a list of email addresses and you want to extract the domain part (the part
# after '@') from each email address.


emails = [
"alice@example.com",
"bob@sample.org",
"charlie@mydomain.net"]

domains = [email.split("@")[1] for email in emails]

print(domains)