def mortgage_calculator(principal, duration_in_years, annual_interest):
    monthly_interest_rate = annual_interest / (100 * 12)
    duration_in_months = duration_in_years * 12
    mortgage_result = principal * (
                      (monthly_interest_rate * ((1 + monthly_interest_rate) ** duration_in_months) )/
                      (((1 + monthly_interest_rate) ** duration_in_months) - 1))
    return mortgage_result


Principal = int(input(f'Type in the principal_ '))
Duration = int(input(f'Type in the duration_ '))
Annual_Interest = float(input(f'Type in the annual interest_ '))
mortgage = mortgage_calculator(principal=Principal,
                               duration_in_years=Duration,
                               annual_interest=Annual_Interest)
print("${:,.2f}".format(mortgage))
