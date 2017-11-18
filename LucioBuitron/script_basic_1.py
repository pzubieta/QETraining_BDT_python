#VARIABLES STRING
variable1="Long message text"
variable2="Alphanumerial long message text 1234567890"

#VARIABLE INT
variable3=12356
variable4=78901
variable5=10
variable6=100

#OPERATIONS INT
result1=variable3+variable4
result2=variable4//variable3
result3=variable5%variable6

#OPERATION STRING
result4=variable1,variable2
result5=variable1,variable6
result6=result3*result2
results7=result1**2

#PRINT RESULTS
print("result1 (+):", result1)
print("result2 (//):", result2)
print("result3 (%):", result3)
print("result4:", variable1,variable2)
print("result5:", result5)