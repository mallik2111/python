with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(',')
        print(f"{row[0]} lives in {row[1]} and studies in {row[2]}")
        with open("cleannames.csv") as file:
            for line2 in file:
                line2 = row
                print(line2)