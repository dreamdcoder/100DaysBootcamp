import random

ppls = input("Enter names of ppl on table separated by ','\n").split(",")
num_of_ppl = int(len(ppls))
payers_index = random.randint(0,num_of_ppl-1)
payer = random.choice(ppls)
print(f"bill will paid by {ppls[payers_index]}")
print(f"bill will paid by {payer}")