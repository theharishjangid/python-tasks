import csv

with open('ppl.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "Name", "designation", "skill"])
    writer.writerow([1, "efwfaf", "md", "speaking"])
    writer.writerow([2, "wefd", "employee", "coding"])
    writer.writerow([3, "awefdf", "hr", "managerial"])

