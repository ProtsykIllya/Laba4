from datetime import date
from dateutil.relativedelta import relativedelta
def days_until(year, month, day):
    target = date(year, month, day)
    today = date.today()
    diff = relativedelta(target, today)
    print(f"Це {diff.months} міс. і {diff.days} дн.")
    return (target - today).days