import pytest
import subprocess
from q02 import load_word_set, compare_word_sets


def test_load_nonexistent_file():
    # we expect a FileNotFoundError
    with pytest.raises(FileNotFoundError) as excinfo:
        filename = 'test/data/nonexistent-filename.txt'
        items = load_word_set(filename)
    assert "No such file or directory: 'test/data/nonexistent-filename.txt'" in str(excinfo.value)

def test_load_word_1_file():
    filename = 'test/data/words-file-1.txt'
    word_set = load_word_set(filename)
    print(word_set)
    assert len(word_set) == 15
    assert 'now' in word_set
    assert 'come' in word_set
    assert 'banana' in word_set

def test_load_word_2_file():
    filename = 'test/data/words-file-2.txt'
    word_set = load_word_set(filename)
    assert len(word_set) == 8
    assert 'time' in word_set
    assert 'arrow' in word_set
    assert 'banana' in word_set

def test_compare_word_set_bad_comparison():
    # we expect an exception if a bad comparision string is given
    with pytest.raises(Exception) as excinfo:
        result_set = compare_word_sets(set(), set(), 'BAD_COMPARISON_STRING')
    assert "Invalid comparison requested" in str(excinfo.value)

def test_compare_word_set_both():
    left_filename = 'test/data/words-file-1.txt'
    left = load_word_set(left_filename)
    right_filename = 'test/data/words-file-2.txt'
    right = load_word_set(right_filename)
    result_set = compare_word_sets(left, right, 'BOTH')
    assert len(result_set) == 2
    assert result_set == set(['banana', 'time'])

def test_compare_word_set_either():
    left_filename = 'test/data/words-file-1.txt'
    left = load_word_set(left_filename)
    right_filename = 'test/data/words-file-2.txt'
    right = load_word_set(right_filename)
    result_set = compare_word_sets(left, right, 'EITHER')
    assert len(result_set) == 21
    expected_set = set(
        ['an', 'aid', 'banana', 'now', 'country', 'a', 'like', 'flies', 
         'to', 'good', 'come', 'their', 'the', 'of', 'men', 'arrow', 
         'time', 'is', 'all', 'fruit', 'for']
    )
    assert result_set == expected_set

def test_compare_word_set_left():
    left_filename = 'test/data/words-file-1.txt'
    left = load_word_set(left_filename)
    right_filename = 'test/data/words-file-2.txt'
    right = load_word_set(right_filename)
    result_set = compare_word_sets(left, right, 'LEFT')
    assert len(result_set) == 13
    expected_set = set(
        ['of', 'aid', 'good', 'men', 'is', 'to', 'all', 'for', 'come', 
         'their', 'the', 'now', 'country']
    )
    assert result_set == expected_set

def test_compare_word_set_right():
    left_filename = 'test/data/words-file-1.txt'
    left = load_word_set(left_filename)
    right_filename = 'test/data/words-file-2.txt'
    right = load_word_set(right_filename)
    result_set = compare_word_sets(left, right, 'RIGHT')
    print(result_set)
    assert len(result_set) == 6
    expected_set = set(['flies', 'an', 'a', 'fruit', 'arrow', 'like'])
    assert result_set == expected_set

def test_q02_application():
    command = ['python3', 'test/test-question.py', '-c', 'q02_application.py']
    result = subprocess.run(command)
    assert result.returncode == 0