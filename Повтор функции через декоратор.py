
def decorator(func):
	def wrapper(q):
		while q > 0:
			func(q)
			q -= 1
	return wrapper


@decorator
def p(number):
	print(f"Number: {number}")
p(5)
'''____________________________________________________'''
def repeater(repeat=1):
	def decorator(func):
		def wrapper(q):
			while q > 0:
				func(q)
				q -= 1
		return wrapper
	return decorator

@repeater(repeat=13)
def p(number):
	print(f"Number: {number}")
p(3)