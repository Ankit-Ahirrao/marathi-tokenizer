def whitespace_tokenizer(text):
    return text.split()

text = "मी शाळेत जातो"
tokens = whitespace_tokenizer(text)
print(tokens)  # Output: ['मी', 'शाळेत', 'जातो']