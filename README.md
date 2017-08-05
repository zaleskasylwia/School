# School

# 1 - School

Small system for managing people at school.

# Classes:
## Student

### Attributes:
first_name

last_name

grades - list of grades (for simplification it could be a list of integers)

### Methods:
get_full_name() - return full name

get_average_grade() - return average of grades

__eq__()


## Teacher

### Attributes:
first_name

last_name

subjects - list of subjects that this teacher is able to teach

### Methods:
get_full_name() - return full name

__eq__()


# Class
Used to aggregate Students and Teachers into a class


### Attributes:


name

students

teachers



### Methods:
get_best_student() - return student with highest average grade

get_average_grade() - get average grade of all students

get_class_subjects() - return a list of subjects that are being taught in this class

sort_students(attr) - sorts students alphabetically or by average grade


## School
Used to aggregate classes


### Attributes:
name

classes

### Methods:
get_best_class() - return class with highest average grade

get_all_teachers() - returns all teachers from this school
