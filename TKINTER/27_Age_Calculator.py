from datetime import date  
  
def calculate_age(birthday):  
  
    today = date.today()  
  
    day_check = ((today.month, today.day) < (birthday.month, birthday.day))  
  
    year_diff  = today.year - birthday.year  
  
    age_in_years = year_diff - day_check  
  
    remaining_months = abs(today.month - birthday.month)  
  
    remaining_days = abs(today.day - birthday.day)  
  
    print("Age:", age_in_years, "Years", remaining_months, "Months and", remaining_days, "days")  
  
if __name__ == "__main__":  
  
    print("Simple Age Calculator")  
  
    birthYear = int(input("Enter the birth year: "))  
    birthMonth = int(input("Enter the birth month: "))  
    birthDay = int(input("Enter the birth day: "))  
  
    dateOfBirth = date(birthYear, birthMonth, birthDay)  
  
    calculate_age(dateOfBirth)  