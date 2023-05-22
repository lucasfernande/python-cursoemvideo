nums = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}° número: '))

    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)

print('~' * 50)
nums[0].sort()
nums[1].sort()
print(f'Os números pares foram: {nums[0]}')
print(f'Os números ímpares foram: {nums[1]}')
