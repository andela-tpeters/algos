def get_algorithm_result(listInput):
  largest = listInput[0]
  for index in range(1,len(listInput) - 1):
    if largest < listInput[index]:
      largest = listInput[index]

  return largest


# print get_algorithm_result([2,5,3,1,88,2,3,112,32,1])