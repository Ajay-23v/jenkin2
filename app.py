import sys

def generate_report(course_name, student_count):
    with open("build_report.txt", "w") as file:
        file.write("===================================\n")
        file.write("       COURSE ENROLLMENT REPORT    \n")
        file.write("===================================\n")
        file.write(f"Course Name:      {course_name}\n")
        file.write(f"Students Enrolled: {student_count}\n")
        file.write("===================================\n")
    print("build_report.txt successfully generated.")

if __name__ == "__main__":
    course = sys.argv[1] if len(sys.argv) > 1 else "DevOps Engineering"
    count = sys.argv[2] if len(sys.argv) > 2 else "45"
    generate_report(course, count)
