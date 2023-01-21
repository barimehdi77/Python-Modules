# Put this at the top of your kata00.py file
kata = (19,42,21)

my_kata = ', '.join(str(x) for x in kata)
print(f"The {len(kata)} numbers are: ", my_kata)
