ans = ""
for Number in range(2, 9):
	for i in range(1, 10**(9 // Number)):
		s = "".join(str(i * j) for j in range(1, Number + 1))
		if "".join(sorted(s)) == "123456789":
			ans = max(s, ans)
			
print(ans)