try:
    a = int(input('Enter a number:'))
    b = int(input('Enter b number:'))
    r = a / b
    print(r)
except Exception as e:
    print(e)
# --------------------------------------------------------------
print("=============================================")
try:
    k = int(input('Enter number k='))
    l = 10 / k
except ZeroDivisionError as f:
    print('We are in exception block')
    print('enter number', f)
else:
    print('We are in else block')
    print(f"{10}/{k}=", l)
    print(f"10/{k}=", l)
finally:
    print('We are in finally block Done')
