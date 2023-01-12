# lab05 tests

import labs.lab05 as lab
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


def test_keyboard():
    b1 = lab.Button(0, "H")
    b2 = lab.Button(1, "I")
    k = lab.Keyboard(b1, b2)
    assert k.buttons[0].ey == 'H'
    assert k.press(2) == ''
    assert k.typing([0, 1]) == 'HI'
    assert k.typing([1, 0]) == 'IH'
    assert b1.times_pressed == 2
    assert b2.times_pressed == 3


def test_minty_coin():
    mint = lab.Minty()
    assert mint.year == 2021
    dime = mint.create('Dime')
    assert dime.year == 2021
    lab.Minty.present_year = 2101
    nickel = mint.create('Nickel')
    assert nickel.year == 2021
    assert nickel.worth() == 35
    mint.update() 
    lab.Minty.present_year = 2176
    assert mint.create('Dime').worth() == 35
    assert lab.Minty.create('Dime').worth() == 10
    assert dime.worth() == 115


def test_smart_fridge():
    fridgey = lab.SmartFridge()
    assert fridgey.add_item('Mayo', 1) == 'I now have 1 Mayo'
    assert fridgey.add_item('Mayo', 2) == 'I now have 3 Mayo'
    assert fridgey.use_item('Mayo', 2.5) == 'I have 0.5 Mayo left'
    assert fridgey.use_item('Mayo', 0.5) == 'Oh no, we need more Mayo!'
    assert fridgey.add_item('Eggs', 12) == 'I now have 12 Eggs'
    assert fridgey.use_item('Eggs', 15) == 'Oh no, we need more Eggs!'
    assert fridgey.add_item('Eggs', 1) == 'I now have 1 Eggs'


def test_vending_machine():
    v = lab.VendingMachine('candy', 10)
    assert v.vend() == 'Nothing left to vend. Please restock.'
    assert v.add_funds(15) == 'Nothing left to vend. Please restock. Here is your $15.'
    assert v.restock(2) == 'Current candy stock: 2'
    assert v.vend() == 'Please update your balance with $10 more funds.'
    assert v.add_funds(7) == 'Current balance: $7'
    assert v.vend() == 'Please update your balance with $3 more funds.'
    assert v.add_funds(5) == 'Current balance: $12'
    assert v.vend() == 'Here is your candy and $2 change.'
    assert v.add_funds(10) == 'Current balance: $10'
    assert v.vend() == 'Here is your candy.'
    assert v.add_funds(15) == 'Nothing left to vend. Please restock. Here is your $15.'

    w = lab.VendingMachine('soda', 2)
    assert w.restock(3) == 'Current soda stock: 3'
    assert w.restock(3) == 'Current soda stock: 6'
    assert w.add_funds(2) == 'Current balance: $2'
    assert w.vend() == 'Here is your soda.'


# def test_cat():
     
# def test_noisy_cat():

# def test_account():

# def test_free_checking():