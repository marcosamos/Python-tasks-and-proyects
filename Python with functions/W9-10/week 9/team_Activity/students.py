import csv

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    dictionary = read_dict("students.csv",I_NUMBER_INDEX)
    print(dictionary)
    i_number = str(input("Please enter an I-Number (xxxxxxxxx): "))
    
    name = get_name(dictionary,i_number)
    
    print(name)




def read_dict(file,studen_key_index):

    dictionary = {}

    with open(file, "rt") as student_file:
        reader_file = csv.reader(student_file)

        next(reader_file)

        for row in reader_file:

            key = row[studen_key_index]
            dictionary[key] = row
            #row.pop(0)

    return dictionary


def get_name(dictionary,i_number):

    if len(i_number) > 9:
        return "Invalid I-Number: too many digits" 
    elif  len(i_number) < 8:
        return "Invalid I-Number: too few digits"
    
    else:

        for key,list in dictionary.items():
            name = list[1]
        
            if key == i_number:
            
                return name
        
    return "No such student"




if __name__ == "__main__":
    main()