letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "John").replace("<|Date|>", "10th Oct 2023"))