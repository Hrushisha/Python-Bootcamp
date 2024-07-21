data=[1,8,'apple','carrot','mango']

fruits=['apple','mango','orange','watermelon']

vegies=['tomato','beans','carrot','onions']

for i in data:
    if i in vegies and i not in fruits:
        print(i)