k = int(input('Enter the step\n'))
lst = [10,20,30,40,50]

if k > len(lst):
    print("step is not valid")

new_lst = lst[-k:] + lst[:-k]
print(new_lst)