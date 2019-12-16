# Part 1
def is_potential_password(num, is_part_two):
  is_valid = False
  num_str = str(num)
  for n in range(len(num_str)-1):
    if num_str[n] > num_str[n+1]:
      return False
    elif num_str[n] == num_str[n+1]:
      is_valid = True
  if is_part_two:
    num_count = {}
    for s in num_str:
      if s in num_count:
        num_count[s] += 1
      else:
        num_count[s] = 1
    if 2 not in num_count.values():
      is_valid = False
  return is_valid

test = [111111, 223450, 123789]
for val in test:
  if is_potential_password(val, False):
    print(val, "is a potential part 1 password")

test2 = [112233, 123444, 111122]
for val in test2:
  if is_potential_password(val, True):
    print(val, "is a potential part 2 password")

real = range(372037,905157)
num_possible = 0
num_special = 0
for val in real:
  if is_potential_password(val, False):
    num_possible += 1
  if is_potential_password(val, True):
    num_special += 1
print(num_possible, num_special)