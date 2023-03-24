import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("bilbo", 3) == "lib_ob"
    assert encrypt_message("bilbo", 9) == "oblib"
    assert encrypt_message("bilbo", 1) == "b_obli"

    with pytest.raises(TypeError):
        encrypt_message("xablau", "0")

    with pytest.raises(TypeError):
        encrypt_message(7777, 1234)
