'''
finance_tools.py

Contains a suite of personal finance calculation functions.
Each function validates inputs and returns the computed result.
'''

def calculate_emi(principal: float, annual_rate: float, months: int) -> float:
    """
    Calculate Equated Monthly Installment (EMI) for a loan
    Formula: EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
    Where:
        P = principal amount
        r = monthly interest rate (annual rate / 12 / 100)
        n = number of monthly installments
    """
    if principal < 0 or annual_rate < 0 or months <= 0:
        raise ValueError("Principal, rate and months must be non-negative and months > 0")
    monthly_rate = annual_rate / 12 / 100
    if monthly_rate == 0:  # Handle 0% interest case
        return round(principal / months, 2)
    emi = (principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return round(emi, 2)

def calculate_sip(monthly_investment: float, annual_rate: float, months: int) -> float:
    """
    Calculate future value of Systematic Investment Plan (SIP)
    Formula: FV = P * [(1 + r)^n - 1] / r * (1 + r)
    Where:
        P = monthly investment amount
        r = monthly rate of return
        n = number of months
    """
    if monthly_investment < 0 or annual_rate < 0 or months <= 0:
        raise ValueError("Monthly investment, rate and months must be non-negative and months > 0")
    monthly_rate = annual_rate / 12 / 100
    future_value = monthly_investment * (((1 + monthly_rate)**months - 1) / monthly_rate) * (1 + monthly_rate)
    return round(future_value, 2)

def calculate_fd(principal: float, annual_rate: float, years: int) -> float:
    """
    Calculate Fixed Deposit (FD) maturity amount with compound interest
    Formula: A = P * (1 + r)^t
    Where:
        P = principal amount
        r = annual interest rate (decimal)
        t = time in years
    """
    if principal < 0 or annual_rate < 0 or years < 0:
        raise ValueError("Principal, rate, and years must be non-negative")
    amount = principal * (1 + annual_rate / 100)**years
    return round(amount, 2)

def calculate_rd(monthly_deposit: float, annual_rate: float, months: int) -> float:
    """
    Calculate Recurring Deposit (RD) maturity amount
    Simplified formula for monthly compounding:
    A = P * ((1 + r)^n - 1) / r
    Where:
        P = monthly deposit
        r = monthly interest rate
        n = number of months
    """
    if monthly_deposit < 0 or annual_rate < 0 or months <= 0:
        raise ValueError("Deposit, rate and months must be non-negative and months > 0")
    monthly_rate = annual_rate / 12 / 100
    future_value = monthly_deposit * (((1 + monthly_rate)**months - 1) / monthly_rate)
    return round(future_value, 2)

def calculate_retirement(current_savings: float, monthly_contribution: float, annual_rate: float, years: int) -> float:
    """
    Calculate retirement corpus projection
    Combines compound interest on current savings and future value of monthly contributions
    """
    if current_savings < 0 or monthly_contribution < 0 or annual_rate < 0 or years < 0:
        raise ValueError("Savings, contribution, rate, and years must be non-negative")
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    fv_current = current_savings * (1 + monthly_rate)**months
    fv_contributions = monthly_contribution * (((1 + monthly_rate)**months - 1) / monthly_rate)
    return round(fv_current + fv_contributions, 2)

def calculate_home_loan_eligibility(monthly_income: float, monthly_expenses: float, multiplier: float = 60) -> float:
    """
    Calculate home loan eligibility using income multiplier method
    Formula: Eligibility = (Monthly Income - Monthly Expenses) * Multiplier
    Default multiplier of 60 (i.e., 5 years equivalent)
    """
    if monthly_income < 0 or monthly_expenses < 0 or multiplier < 0:
        raise ValueError("Income, expenses, and multiplier must be non-negative")
    disposable_income = monthly_income - monthly_expenses
    return round(disposable_income * multiplier, 2) if disposable_income > 0 else 0.0

def calculate_credit_card_interest(balance: float, annual_rate: float, min_payment_percent: float = 2.0) -> float:
    """
    Calculate total interest paid until balance is cleared with minimum payments
    """
    if balance < 0 or annual_rate < 0 or min_payment_percent < 0:
        raise ValueError("Balance, rate, and payment percent must be non-negative")
    monthly_rate = annual_rate / 12 / 100
    total_interest = 0.0
    remaining = balance
    while remaining > 0:
        interest = remaining * monthly_rate
        total_interest += interest
        remaining += interest
        payment = max(remaining * (min_payment_percent / 100), 25.0)
        payment = min(payment, remaining)
        remaining -= payment
        remaining = round(remaining, 2)
    return round(total_interest, 2)

def calculate_taxable_income(annual_income: float, deductions: float) -> float:
    """
    Calculate taxable income after deductions
    """
    if annual_income < 0 or deductions < 0:
        raise ValueError("Income and deductions must be non-negative")
    taxable = annual_income - deductions
    return max(round(taxable, 2), 0.0)

def calculate_budget(income: float, expenses: float) -> dict:
    """
    Budget planner calculating surplus/deficit and expense ratios
    """
    if income < 0 or expenses < 0:
        raise ValueError("Income and expenses must be non-negative")
    surplus = income - expenses
    expense_ratio = (expenses / income * 100) if income > 0 else 0.0
    return {
        'surplus': round(surplus, 2),
        'expense_ratio': round(expense_ratio, 1),
        'is_deficit': surplus < 0
    }

def calculate_net_worth(assets: float, liabilities: float) -> float:
    """
    Calculate net worth (assets - liabilities)
    """
    if assets < 0 or liabilities < 0:
        raise ValueError("Assets and liabilities must be non-negative")
    return round(assets - liabilities, 2)
