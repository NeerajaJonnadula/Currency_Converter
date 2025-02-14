def read_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid value. Please enter a positive number.')


def choose_currency(prompt):
    available_currencies = ('INR', 'USD', 'EUR', 'CAD')
    while True:
        currency = input(f'{prompt} currency (INR/USD/EUR/CAD): ').upper()
        if currency not in available_currencies:
            print('Invalid choice. Try again.')
        else:
            return currency


def convert(amount, base_currency, target_currency):
    rates = {
        'INR': {'USD': 0.012, 'EUR': 0.010, 'CAD': 0.016},
        'USD': {'EUR': 0.85, 'CAD': 1.25, 'INR': 82.0},
        'EUR': {'USD': 1.18, 'CAD': 1.47, 'INR': 96.5},
        'CAD': {'USD': 0.80, 'EUR': 0.68, 'INR': 61.0},
    }

    if base_currency == target_currency:
        return amount

    return amount * rates[base_currency][target_currency]


def start_program():
    amount = read_amount()
    from_currency = choose_currency('Base')
    to_currency = choose_currency('Target')
    result = convert(amount, from_currency, to_currency)
    print(f'{amount} {from_currency} is equal to {result:.3f} {to_currency}')


if __name__ == "__main__":
    start_program()
