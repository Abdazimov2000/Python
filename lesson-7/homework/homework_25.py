def student_data(name, age=18, **details):
    print(f"Name: {name}")
    print(f"Age: {age}")
    for key, value in details.items():
        print(f"{key}: {value}")
student_data('Asadbek',Location = 'Almalyk', Field = 'Economics')
