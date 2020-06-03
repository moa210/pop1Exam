# student number 12915798


def balance(init_sum, int_rate, tfl, tax_rate, M):
    acc_balance = init_sum
    int_rate = int_rate
    tax_rate = tax_rate
    free_limit = tfl
    months = M
    for i in range( months ):
        acc_balance = balance_update( acc_balance, tax_rate, int_rate, free_limit )

    print( str( "%.2f" % acc_balance ) )


# helper method takes balance, tax free amount and tax rate (integers)
# returns updated balance after tax deduction
def tax_calculation(acc_balance, tfl, tax_rate):
    if acc_balance <= tfl:
        return acc_balance
    else:
        tax_paid = (acc_balance - tfl) * (tax_rate / 100)
        return acc_balance - tax_paid


# helper method takes balance, interest rate (integers)
# returns updated balance after tax deduction
def add_interest(acc_balance, int_rate):
    return acc_balance + (acc_balance * (int_rate / 100))


# helper method takes balance, tax, rate, interest rate, tax free amount (integers)
# returns updated balance after tax reduction and interest add on has been completed
def balance_update(acc_balance, tax_rate, interest_rate, tfl):
    acc_balance = add_interest( acc_balance, interest_rate )
    acc_balance = tax_calculation( acc_balance, tfl, tax_rate )
    return acc_balance


balance( 10000, 1, 20000, 1, 2 )  # must be approximately 10201
balance( 25000, 2, 20000, 1, 2 )  # must be approximately 25904.5
balance( 19800, 2, 20000, 1, 2 )  # must be approximately 20597.96
