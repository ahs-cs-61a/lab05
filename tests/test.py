# lab01 tests

import labs.lab01 as lab
from io import StringIO 
import sys


# capturing prints (stdout)
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


def test_falling():
    assert lab.falling(6, 3) == 120
    assert lab.falling(4, 3) == 24
    assert lab.falling(4, 1) == 4
    assert lab.falling(4, 0) == 1


def test_sum_digits():
    assert lab.sum_digits(10) == 1
    assert lab.sum_digits(4224) == 12
    assert lab.sum_digits(1234567890) == 45


def test_double_eights():
    assert lab.double_eights(8) == False
    assert lab.double_eights(88) == True
    assert lab.double_eights(2882) == True
    assert lab.double_eights(880088) == True
    assert lab.double_eights(12345) == False
    assert lab.double_eights(80808080) == False


def test_wears_jacket_with_if():
    assert lab.wears_jacket_with_if(90, False) == False
    assert lab.wears_jacket_with_if(40, False) == True
    assert lab.wears_jacket_with_if(100, True) == True


def test_is_prime():
    assert lab.is_prime(10) == False
    assert lab.is_prime(7) == True
    assert lab.is_prime(1) == False


def test_fizzbuzz():
    print("\n\nfizzbuzz(16) prints:")
    with Capturing() as fizzbuzz_16_output:
        lab.fizzbuzz(16)
    fizzbuzz_16 = ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16']
    for i in range(len(fizzbuzz_16)):
        assert fizzbuzz_16[i] == fizzbuzz_16_output[i]
    assert lab.fizzbuzz(16) is None # print, don't return


def test_has_digit():
    assert lab.has_digit(10, 1) == True
    assert lab.has_digit(12, 7) == False
    assert lab.has_digit(4, 4) == True


def test_unique_digits():
    assert lab.unique_digits(8675309) == 7
    assert lab.unique_digits(1313131) == 2
    assert lab.unique_digits(13173131) == 3
    assert lab.unique_digits(10000) == 2
    assert lab.unique_digits(101) == 2
    assert lab.unique_digits(10) == 2


def test_a_plus_abs_b():
    assert lab.a_plus_abs_b(2, 3) == 5
    assert lab.a_plus_abs_b(2, -3) == 5
    assert lab.a_plus_abs_b(-1, -4) == 3
    assert lab.a_plus_abs_b(-1, 4) == 3


def test_two_of_three():
    assert lab.two_of_three(1, 2, 3) == 5
    assert lab.two_of_three(5, 3, 1) == 10
    assert lab.two_of_three(10, 2, 8) == 68
    assert lab.two_of_three(5, 5, 5) == 50


def test_largest_factor():
    assert lab.largest_factor(15) == 5
    assert lab.largest_factor(80) == 40
    assert lab.largest_factor(13) == 1


def test_hailstone():
    print("\n\nhailstone(10) prints:")
    with Capturing() as hailstone_10_output:
        lab.hailstone(10)
    hailstone_10 = ['10', '5', '16', '8', '4', '2', '1']
    for i in range(len(hailstone_10)):
        assert hailstone_10[i] == hailstone_10_output[i] # incorrect prints
    assert lab.hailstone(10) == 7
    
    print("\n\nhailstone(1) prints:")
    with Capturing() as hailstone_1_output:
        lab.hailstone(1)
    hailstone_1 = ['1']
    for i in range(len(hailstone_1)):
        assert hailstone_1[i] == hailstone_1_output[i] # incorrect prints
    assert lab.hailstone(1) == 1
