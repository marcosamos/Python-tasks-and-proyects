import random


def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    print("------------------------------")
    # Add numbers by default argument
    append_random_numbers(randnums)
    print(randnums)
    print("------------------------------")
    # Add number by custom argument
    append_random_numbers(randnums, 3)
    print(randnums)

    # memebr list
    member = []
    # Add words by default argument
    append_random_words(member)
    print(member)
    print("------------------------------")
    # Add words by custom argument
    append_random_words(member,10)
    print(member)




    

# number function
def append_random_numbers(numbers_list, quantity=1):

    for _ in range(quantity):
        computes_random_number = random.uniform(0,50)
        rounding = round(computes_random_number, 1)
        numbers_list.append(rounding)


# word function
def append_random_words(word_list,quantity=1):
    church_membership = ["Pablo","Pedro","Juan","Mateo","Lucas","Marcos",\
        "Sebedeo","Daniel","Tomas","Jose","Brigham","Adan","Hyram","Gordon","Maria"]
    for _ in range(quantity):
        member = random.choice(church_membership)
        word_list.append(member)

    
    



if __name__ == "__main__" : 
    main ()