def build_person(first, last, **user_info):
    user_info['First'] = first
    user_info['Last'] = last
    return user_info
ffirst = input('Enter your first name: ').title()
llast = input('Enter your last name: ').title()
llocation = input("Enter your location: ").title()
ffield = input("Enter your field: ").title()
user = build_person(ffirst, llast, Location = llocation, Field = ffield)
print(user)
