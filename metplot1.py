import matplotlib.pyplot as plt

#data Sample
x= [34, 72, 10, 6, 30]
y=[13, 5, 100, 43, 90]

#Creating a line plot
plt.plot(x,y)
plt.title("A Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Creating a Bar Chart
# Sample data
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

plt.bar(names, scores, color='skyblue')
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

#A pe Chart
# Sample data
activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
hours = [8, 2, 8, 6]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Daily Activities")
plt.show()
print(pie)
