def manipulate_data(InputType, data):
  if InputType == 'list':
    return data[::-1]

  if InputType == 'set':
    toAdd = {'A','BEE','CEE'}
    return data.union(toAdd)

  if InputType == 'dictionary':
    return data.keys()

# print manipulate_data('list',['a','n','d','a','e','n'])
# print manipulate_data('set',set(['f','me']))
# print manipulate_data('dictionary',{'a':1})