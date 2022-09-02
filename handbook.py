"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: We do not expect you to come up with a perfect solution. We are more interested
in how you would approach a problem like this.
"""
import json
import re 

def clean_conditions(conditions):
    """Tidy extraneous information such as extra punctations and words from the text conditions
    """
    for course, condition in conditions.items():
        course_codes = re.findall(r"[A-Z]{4}[0-9]{4}", condition)
        conditions[course] = " ".join(course_codes)
    return conditions

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

TIDY_CONDITIONS = clean_conditions(CONDITIONS)

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """

    # the student has not completed any courses 
    if len(courses_list) == 0:
        if target_course == "COMP1511":
            return True
        return False

    # calculate the total units the student has completed
    total_units = 0
    for course in courses_list:
        total_units += 6

    # get the number of COMP courses taken by the student
    num_comp_courses = 0
    for course in courses_list:
        if course[:4] == "COMP":
            num_comp_courses += 1
    
    # check the condition of the target course
    target_condition = TIDY_CONDITIONS[target_course]
    for course in courses_list:
        if course not in target_condition:
            return False
    
    return True
    




    