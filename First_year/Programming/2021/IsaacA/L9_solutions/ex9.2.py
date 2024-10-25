d   =   {("Alice", "Bianchi", 1234567): [1, 2, 3],
        ("Mario", "Rossi", 7654321): [3, 4, 5],
        ("Chiara", "Ferri", 3217654): [2, 3, 4, 5],
        ("Aurora", "Valeri", 6541237): [6, 1, 3] 
         }


def add_course(d, s, courseID):
    if s in d:
        d[s].append(courseID)
    else:
        d[s] = [courseID]

def add_courses(d, s, course_list):
    if s in d:
        d[s].extend(course_list)
    else:
        d[s] = course_list
        
def get_courses(d, s):
    return d.get(s, [])

def course_students(d, courseID):
    ls = []
    for s in d:
        if courseID in d[s]:
            ls.append(s)
    return ls


def students_dictionary(d):
    # note sorted does NOT sort in place, instead returns a sorted list 
    
    #The key parameter can be defined as a function to be called on each element of list/tuple/dictionary before sort.
    #The inline function lambda s: s[1] is defined as a value of the key parameter.
    #The lambda function takes input s return s[1] which is the second element of s.
    
    return sorted(d, key= lambda s:s[1])
   
''' ALTERNATIVELY
def students_dictionary(d):

    def lastname(s):
        return s[1]

    return sorted(d, key=lastname)
'''

def course_statistics(d):
    statistics = dict()
    list_val = []
    for c in d.values():
        list_val = list_val + c
    for n in list_val:
        if n in statistics:
            statistics[n] = statistics[n] + 1
        else:
            statistics[n] = 1
    return statistics


def remove_course(d, studentID, courseID):
    found = False
    for s in d:
        if studentID in s:
            if courseID in d[s]:
                if len(d[s]) <= 1:
                    del d[s] 
                    print("Student ", s, "is removed")
                else:
                    d[s].remove(courseID)
                    print("Course ", courseID, "for ", s, "is removed")   
            else:
                print("Course ", courseID, "is not found for ", s)
            found = True
            break 
    if found == False:
        print("Student with ID ", studentID, "is not found")
           

''' Main Program '''
''''''''''''''''''''

ds = course_statistics(d)
n_courses = 7 # let's use a number more than those present in 'd'

for i in range(1, n_courses+1):
    if i not in ds:
        ds[i] = 0    # expand the dictionary with all the remaning courses

#ds.items() items contains pairs of key and value
ls = sorted(ds.items(), key= lambda s:s[1], reverse=True) # sort based on the value in desc order 

for courseID, freq in ls:
    print(courseID, '*'*freq, sep='\t')
