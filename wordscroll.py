class Ok:

	def __init__(self, text):
		self.text = text


	def __add__(self, other):
		for i in range(len(other.text) + 1):
			script = self.text[:i] + '>' + other.text
			script += '>' + self.text[i:]
			print(script)



a=input('first word!!!:')
b=input('second word!!!:')


girl=Ok(a)
boy=Ok(b)


result = girl + boy
print('\n' * 7)
rasoolt = boy + girl
