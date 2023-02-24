import sys, os
from skillshare import Skillshare, splash
import requests

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare("PHPSESSID=caf16216cfe7df03f862accd937d4c3d")
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
