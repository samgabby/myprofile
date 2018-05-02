class Ok:

	def __init__(self, text):
		self.text = text


	def __add__(self, other):
		for i in range(len(other.text) + 1):
			script = self.text[:i] + '>' + other.text
			script += '>' + other.text + self.text[i:]
			print(script)



a=input('first word!!!:')
b=input('second word!!!:')


girl=Ok(a)
boy=Ok(b)


result = girl + boy
rasoolt = boy + girl
print(result)
print('\n' * 7)
print(rasoolt)