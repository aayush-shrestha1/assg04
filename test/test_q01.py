import pytest
import subprocess
from q01 import load_ranked_items, sort_ranked_items, get_ranked_items


def test_load_nonexistent_file():
    # we expect a FileNotFoundError
    with pytest.raises(FileNotFoundError) as excinfo:
        filename = 'test/data/nonexistent-filename.txt'
        items = load_ranked_items(filename)
    assert "No such file or directory: 'test/data/nonexistent-filename.txt'" in str(excinfo.value)

def test_load_boy_names_file():
    filename = 'test/data/boy-names.txt'
    items = load_ranked_items(filename)
    assert len(items) == 1000

    assert type(items[0]) == tuple
    assert items[0] == (795, 'Damir')

    assert type(items[500]) == tuple
    assert items[500] == (779, 'Ray')

    assert type(items[999]) == tuple
    assert items[999] == (625, 'Trevor')


def test_load_girl_names_file():
    filename = 'test/data/girl-names.txt'
    items = load_ranked_items(filename)
    assert len(items) == 1000

    assert type(items[0]) == tuple
    assert items[0] == (290, 'Leia')

    assert type(items[500]) == tuple
    assert items[500] == (404, 'Ivory')

    assert type(items[999]) == tuple
    assert items[999] == (145, 'Remi')

def test_sort_girl_names():
    filename = 'test/data/girl-names.txt'
    items = load_ranked_items(filename)
    assert len(items) == 1000

    # checking not sorting in place here
    sorted_items = sort_ranked_items(items)
    assert len(sorted_items) == 1000
    assert sorted_items != items

    assert type(sorted_items[0]) == tuple
    assert sorted_items[0] == (1, 'Olivia')

    assert type(sorted_items[500]) == tuple
    assert sorted_items[500] == (501, 'Estella')

    assert type(sorted_items[999]) == tuple
    assert sorted_items[999] == (1000, 'Raina')

def test_sort_boy_names():
    filename = 'test/data/boy-names.txt'
    items = load_ranked_items(filename)
    assert len(items) == 1000

    # checking not sorting in place here
    sorted_items = sort_ranked_items(items)
    assert len(sorted_items) == 1000
    assert sorted_items != items

    assert type(sorted_items[0]) == tuple
    assert sorted_items[0] == (1, 'Liam')

    assert type(sorted_items[500]) == tuple
    assert sorted_items[500] == (501, 'Ruben')

    assert type(sorted_items[999]) == tuple
    assert sorted_items[999] == (1000, 'Stefan')

def test_get_boy_name_slices():
    filename = 'test/data/boy-names.txt'
    items = load_ranked_items(filename)
    assert len(items) == 1000
    sorted_items = sort_ranked_items(items)
    assert len(sorted_items) == 1000

    items = get_ranked_items(sorted_items, 1, 2)
    assert len(items) == 2
    assert items[0] == (1, 'Liam')
    assert items[1] == (2, 'Noah')

    items = get_ranked_items(sorted_items, 998, 1000)
    assert len(items) == 3
    assert items[0] == (998, 'Ishaan')
    assert items[2] == (1000, 'Stefan')    

def test_get_girl_name_slices():
    filename = 'test/data/girl-names.txt'
    items = load_ranked_items(filename)
    assert len(items) == 1000
    sorted_items = sort_ranked_items(items)
    assert len(sorted_items) == 1000

    items = get_ranked_items(sorted_items, 1, 2)
    assert len(items) == 2
    assert items[0] == (1, 'Olivia')
    assert items[1] == (2, 'Emma')

    items = get_ranked_items(sorted_items, 998, 1000)
    assert len(items) == 3
    assert items[0] == (998, 'Lavender')
    assert items[2] == (1000, 'Raina')

def test_get_bad_ranks():
    filename = 'test/data/girl-names.txt'
    items = load_ranked_items(filename)
    sorted_items = sort_ranked_items(items)

    # a 0 rank should give an error
    with pytest.raises(Exception) as excinfo:
        items = get_ranked_items(sorted_items, 0, 1)
    assert "Invalid ranks" in str(excinfo.value)

    # a 0 rank should give an error for end as well
    with pytest.raises(Exception) as excinfo:
        items = get_ranked_items(sorted_items, 1, 0)
    assert "Invalid ranks" in str(excinfo.value)

    # begin should not be greater than end
    with pytest.raises(Exception) as excinfo:
        items = get_ranked_items(sorted_items, 2, 1)
    assert "Invalid ranks" in str(excinfo.value)

    # but it is perfectly valid to get a single item, it should be
    # a list of size 1
    items = get_ranked_items(sorted_items, 500, 500)
    assert len(items) == 1
    assert type(items) == list

    # neither begin nor end should be greater than list size N
    N = len(sorted_items)
    with pytest.raises(Exception) as excinfo:
        items = get_ranked_items(sorted_items, 1, N+1)
    assert "Invalid ranks" in str(excinfo.value)

    N = len(sorted_items)
    with pytest.raises(Exception) as excinfo:
        items = get_ranked_items(sorted_items, N+1, N)
    assert "Invalid ranks" in str(excinfo.value)

def test_q01_application():
    command = ['python3', 'test/test-question.py', '-c', 'q01_application.py']
    result = subprocess.run(command)
    assert result.returncode == 0