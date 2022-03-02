from names import make_full_name, extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Marcos", "Uc") == "Uc; Marcos"
    assert make_full_name("Agustin", "Iturbide") == "Iturbide; Agustin"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Talavera; Gabriela") == "Talavera"
    assert extract_family_name("Iturbide; Agustin") == "Iturbide"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Talavera; Gabriela") == "Gabriela"
    assert extract_given_name("Iturbide; Agustin") == "Agustin"


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])