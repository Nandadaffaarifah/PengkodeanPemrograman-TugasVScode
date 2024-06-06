import matplotlib.pyplot as plt

# Data untuk diagram lingkaran
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Buat diagram lingkaran
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Atur proporsi aspek agar lingkaran terlihat seperti lingkaran
plt.axis('equal')

# Tampilkan diagram
plt.show()
import matplotlib.pyplot as plt

# Data untuk diagram garis
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Buat diagram garis
plt.plot(x, y)

# Beri label pada sumbu x dan y
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Tampilkan diagram
plt.show()
import matplotlib.pyplot as plt

# Data untuk diagram titik
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Buat diagram titik
plt.scatter(x, y)

# Beri label pada sumbu x dan y
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Tampilkan diagram
plt.show()
