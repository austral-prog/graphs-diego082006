t.show()

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [18, 20, 19, 23, 25, 22, 21]

plt.figure(figsize=(8,5))
plt.plot(days, temperature, color="blue", marker="o", linestyle="--", label="Temperature")

plt.title("Weekly Temperature Trends")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()

plt.savefig("imgs/line_plot.png", dpi=300, bbox_inche

subjects = ["Math", "Physics", "Programming", "History"]
hours = [10, 8, 15, 5]

plt.figure(figsize=(8,5))
plt.bar(subjects, hours, color=["red", "blue", "green", "orange"])

plt.title("Study Hours by Subject")
plt.xlabel("Subjects")
plt.ylabel("Hours")

plt.savefig("imgs/bar_chart.png", dpi=300, bbox_inches='tight')plt.show()


scores = np.random.normal(70, 10, 100)

plt.figure(figsize=(8,5))
plt.hist(scores, bins=10, color="purple", edgecolor="black")

plt.title("Distribution of Exam Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.savefig("imgs/histogram.png", dpi=300, bbox_inches='tight')



study_hours = [1,2,3,4,5,6,7,8,9,10]
exam_scores = [50,55,60,62,65,70,72,80,85,90]

plt.figure(figsize=(8,5))
plt.scatter(study_hours, exam_scores, color="green", marker="o", label="Students")

plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()

plt.savefig("imgs/scatter_plot.png", dpi=300, bbox_inches='tight')


activities = ["Study", "Sleep", "Gaming", "Exercise"]
time_spent = [35, 40, 15, 10]

plt.figure(figsize=(8,5))
plt.pie(time_spent, labels=activities, autopct='%1.1f%%')

plt.title("Daily Activities Distribution")

plt.savefig("imgs/custom_plot.png", dpi=300, bbox_inches='tight')
plt.show()
plt.show()plt.show()s='tight')
plt.show()