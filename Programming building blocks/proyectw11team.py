with open("hr_system.txt") as hr_file:
    for line in hr_file:
        new = line.strip()
        parts = new.split(" ")

        name = parts[0]
        title = parts[2]
        print(f"{name}, {title}")