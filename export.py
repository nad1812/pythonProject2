def export_data(path):
    count = 0
    with open(path, "r") as file:
        for line in file:
            count += 1
            print(line)