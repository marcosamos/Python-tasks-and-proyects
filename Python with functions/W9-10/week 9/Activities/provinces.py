def main():
    provinces_of_canada = read_list("provinces.txt")
    print(provinces_of_canada)

    # Remove the first element
    provinces_of_canada.pop(0)
    #print(provinces_of_canada)

     # Remove the last element
    provinces_of_canada.pop()
    #print(provinces_of_canada)

    # Replace AB  with Alberta
    
    for province in range(len(provinces_of_canada)):
        if provinces_of_canada[province] == "AB":
            provinces_of_canada[province] = "Alberta"


    count = provinces_of_canada.count("Alberta")
    
    print(f"Alberta occurs {count} times in the modified list.")



def read_list(textfile):
    with open(textfile, "rt") as text_file:
        text_list = []
        for list in text_file:
            new_list = list.strip()
            text_list.append(new_list)
        return text_list


if __name__ == "__main__":
    main()