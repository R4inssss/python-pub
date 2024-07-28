from app.calculationz import add, subtract, multiply, divide, BankAccount
import pytest


@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected" ,[
    (3, 2, 5),
    (8, 2, 10),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    print("testing add function")
    sum = add(num1, num2)
    assert sum == expected

def test_subtract():
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(3, 3) == 9

def test_divide():
    assert divide(4, 4) == 1

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance) == 55 


def test_bank_transaction(zero_bank_account):
    zero_bank_account.deposit(200)
    zero_bank_account.withdraw(50)
    assert zero_bank_account.balance == 150


