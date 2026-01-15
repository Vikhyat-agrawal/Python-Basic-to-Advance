# d={
#     'name': 'Alice',
#     'age': 25,
#     'lists': ['Python', 'C++', 'Java' ]
# }
# d['lists'][0]='JavaScript'
# print(d)
s = {8, 7, 12, "Harry", [1,2]}
# You can’t—lists are unhashable, so {8, 7, 12, "Harry", [1, 2]} raises TypeError: unhashable type: 'list' before you even get to mutating it. If you need an immutable container inside the set, use a tuple instead: