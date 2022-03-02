from sentences import get_determiner, get_noun,get_verb, get_preposition, get_prepositional_phrase
import pytest

def test_get_determiner():
    assert get_determiner(1) == "one" or "the"
    assert get_determiner(0) == "some" or "many"
    
    
def test_get_noun():
    assert get_noun(1) == "adult" or "bird" or "boy" or "car" or "cat" or \
        "child" or "dog" or "girl" or "man" or "woman"
    assert get_noun(0) == "adults" or "birds" or "boys" or "cars" or "cats" or \
          "children" or "dogs" or "girls" or "men" or "women"

def test_get_verb():
    assert get_verb(1,"past") == "drank" or "ate" or "grew" or "laughed" or "thought" or \
        "ran" or "slept" or "talked" or "walked" or "wrote"
    assert get_verb(1, "present") == "drinks" or "eats" or "grows" or "laughs" or "thinks" or \
        "runs" or "sleeps" or "talks" or "walks" or "writes"
    assert get_verb(0, "present") == "drink" or "eat" or "grow" or "laugh" or "think" or \
        "run" or "sleep" or "talk" or "walk" or "write"
    assert get_verb(1, "future") == "will drink" or "will eat" or "will grow" or "will laugh" or \
        "will think" or "will run" or "will sleep" or "will talk" or \
        "will walk" or "will write"

def test_get_preposition():
    
    assert get_preposition() == "about" or "above" or "across" or "after" or "along" or \
    "around" or "at" or "before" or "behind" or "below" or \
    "beyond" or "by" or "despite" or "except" or "for" or \
    "from" or "in" or "into" or "near" or "of" or \
    "off" or "on" or "onto" or "out" or "over" or \
    "past" or "to" or "under" or "with" or "without"



def test_get_prepositional_phrase():
    phrase_list = []
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    single_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
          "children", "dogs", "girls", "men", "women"]
    sin_deter = ["the", "one"]
    plu_deter = ["some", "many"]

    for i in range(1, 3):
        for i in range(10):
            phrase = get_prepositional_phrase(1)
            phrase_list = phrase.split()
            assert len(phrase_list) == 3
            assert phrase_list[0] in prepositions
            assert phrase_list[1] in sin_deter or plu_deter
            assert phrase_list[2] in single_nouns or plural_nouns
        


 
pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])