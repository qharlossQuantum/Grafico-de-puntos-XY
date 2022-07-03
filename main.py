import matplotlib.pyplot as plt

print("ingresa un valor para\n")
m=float(input("m="))

plt.plot(1/m,m**0.5,marker ="o")

m=m+4
plt.plot(0.5*m,m**0.5,marker ="o")

plt.grid()
plt.show()