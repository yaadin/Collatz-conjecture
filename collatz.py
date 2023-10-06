import matplotlib.pyplot as plt
def calculate(n,x):
	count = 0
	y.append(n)
	x.append(count)
	y.append((3 * n)+1)
	n = (3 * n) + 1
	x.append(count)
	while n != 1:
	    if n % 2 == 0:
	        y.append(n // 2)
	        n = n//2
	    else:
	        y.append((3 * n) + 1)
	        n = (3 * n) + 1
	    count += 1
	    x.append(count)

counter = 0
while counter < 43:
	calculate


y = []
totalx = []
calculate(8,x,y)
print(x)
print(y)

z =[1] * len(x)
# print(z)
fig, ax = plt.subplots()
y_value = 1
plt.xlabel('Number of Iterations')

plt.ylabel('Current N')

plt.title('3n+1 problem')

plt.plot(x, y, linestyle='-', color='blue', linewidth=1)

ax.axhline(y=y_value, color='r', linestyle='--', label='y = 1')


plt.grid(True)

plt.show()


