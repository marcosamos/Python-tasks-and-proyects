import random
# (------------------------Function---------------------------------)
def main():

    myArray = [
        [1,"past"],
        [0,"past"],
        [1,"present"],
        [0,"present"],
        [1,"future"],
        [0,"future"]]

    for i in range(1):
        for grammatical_number,tense in myArray:
            word = get_determiner(grammatical_number)
            nouns = get_noun(grammatical_number)
            verb = get_verb(grammatical_number,tense)
            print(f"{word} {nouns} {verb}")

    print("-------------------------+-------------------------") 


    for i in range(1):
        for grammatical_number,tense in myArray:
            word = get_determiner(grammatical_number)
            nouns = get_noun(grammatical_number)
            verb = get_verb(grammatical_number,tense)
            prepositional_phrase = get_prepositional_phrase(grammatical_number)
            print(f"{word} {nouns} {verb} {prepositional_phrase}")

    print("-------------------------+-------------------------")

    for i in range(1):
        for grammatical_number,tense in myArray:
            word = get_determiner(grammatical_number)
            nouns = get_noun(grammatical_number)
            verb = get_verb(grammatical_number,tense)
            prepositional_phrase = get_prepositional_phrase(grammatical_number)
            complement = get_complement(grammatical_number,tense)
            print(f"{word} {nouns} {verb} {prepositional_phrase} {complement}")
            

# (------------------------Function---------------------------------)
def get_determiner(grammatical_number):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


# (------------------------Function---------------------------------)
def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if grammatical_number == 1:
        nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats",
          "children", "dogs", "girls", "men", "women"]

    noun = random.choice(nouns)
    return noun    

    
# (------------------------Function---------------------------------)
def get_verb(grammatical_number, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and grammatical_number == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and grammatical_number != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]   

    verb = random.choice(verbs)
    return verb


# (------------------------Function---------------------------------)
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    
    preposition = get_preposition()
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = (f"{preposition} {word} {noun}")
    return prepositional_phrase




# (------------------------Function---------------------------------)
def  get_preposition (): 
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    prepositions =  ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
    return preposition


# complemet funcion

def get_complement(grammatical_number,tense):

    if tense == "past":
        complements = ["and everyone cried","and all of them ran","and they danced"]
    elif tense == "present" and grammatical_number == 1:
        complements = ["and then sleep", "and then swim"]
    elif tense == "present" and grammatical_number != 1:
        complements = ["and then to sing","and all of them play futbol"]
    elif tense == "future":
        complements = ["and everyone will go to the concert", "and all of them will fly", "and they will dance cumbia"]   

    complement = random.choice(complements)
    return complement

# Call main function
if __name__ == "__main__" : 
    main ()