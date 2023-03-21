#query if you want to find the fractional
def fact(query):
    return 1 if (query==1 or query==0) else query * fact(query - 1);

query = 5
print("Factorial of",query,"is",)
fact(query)