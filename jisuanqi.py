def add(x, y):
   """���"""

   return x + y

def subtract(x, y):
   """���"""

   return x - y

def multiply(x, y):
   """���"""

   return x * y

def divide(x, y):
   """���"""

   return x / y

# �û�����
print("ѡ�����㣺")
print("1�����")
print("2�����")
print("3�����")
print("4�����")

choice = input("�������ѡ��(1/2/3/4):")

num1 = int(input("�����һ������: "))
num2 = int(input("����ڶ�������: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("�Ƿ�����")
