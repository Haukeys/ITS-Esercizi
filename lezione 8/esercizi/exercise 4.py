from abc import ABC, abstractmethod
#inizializare una classe astrata Person
class Person(ABC):

    def __init__(self, name:str, age:int)->None:
        self.name=name
        self.age=age

    @abstractmethod
    def get_role(self)->str:
        pass

    def __str__(self):
        return f"Name:{self.name}, Age: {self.age}, Role: {self.get_role()}"

#inizzializare una classe Student sotto classe di Person
class Student(Person):
        
        def __init__(self, name:str, age:int, student_id:str)->None:
             super().__init__(name, age)
             self.student_id=student_id
             self.courses:list[Course] = []
            
        def get_role(self)->str:
             return "Student"
        
        def enroll(self, course:"Course")->None:
            if course not in self.courses:
                 self.courses.append(course)
                 
        
        def __str__(self)->str:
             return super().__str__()+f"ID: {self.student_id}"

class Professor(Person):

    def __init__(self, name:str, age:int, professor_id:str, department:"Department")->None:
          super().__init__(name, age)
          self.professor_id=professor_id
          self.department:"Department" = department
          self.courses:list[Course] = []
    
    def get_role(self):
        return "Professor"
    
    def assign_to_course(self, course:"Course")-> None:
        if course not in self.courses:
            self.courses.append(course)

    def set_department(self, department:"Department")->None:
         self.department=department    
    
    def __str__(self):
        return super().__str__()+f"ID: {self.professor_id}, Department: {self.department}"

class Course:

    def __init__(self, name:str, code:str)->None:
        self.course_name=name
        self.course_code=code
        self.students:list[Student] = []
        self.professor:Professor = None

    def add_student(self, student:Student)->None:
         
         if student not in self.students:
            self.students.append(student)
    
    def set_professor(self, professor:Professor)-> None:
         
         self.professor=professor

    def __str__(self) -> str:
        if self.professor:
            professor_name:str = self.professor.name
            return f"Course name: {self.course_name}, COurse ID: {self.course_code}, Professor: {self.professor}."
        else:
            return f"Course name: {self.course_name}, COurse ID: {self.course_code}, Professor: 'Non ancora assegnato'."
         
class Department:
    def __init__(self, name:str)-> None:
          self.department_name:str = name
          self.professors:list[Professor]=[]
          self.courses:list[Course]=[]

    def add_course(self, course:Course)->None:
         if course not in self.courses:
                 self.courses.append(course)

    def add_professor(self, professor:Professor)->None:
         if professor not in self.professors:
                 self.professors.append(professor)

    def __str__(self):
        return f"Department: {self.department_name}"
    
class University:
    def __init__(self, name=str)->None:
        self.university_name:str=name
        self.departments:list[Department]=[]
        self.students:list[Student]=[]

    def add_department(self, department:Department)->None:
         self.departments.append(department)

    def add_student(self, student:Student)->None:
         self.students.append(student)

if __name__=='__main__':
     univ:University=University("Sapienza")

     cs_dep:Department=Department("Informatica")
     lt_dep:Department=Department("Lettere")

     univ.add_department(cs_dep)
     univ.add_department(lt_dep)

     python_cs:Course=Course("Programazione in Python", "PY101")
     antica_cs:Course=Course("Lettere antiche", "LT101")

     cs_dep.add_course(python_cs)
     lt_dep.add_course(antica_cs)

     mc_prof:Professor=Professor("Marco Cascio",18,"MC100")
     me_prof:Professor=Professor("Marco Esposito",30,"ME150")

     cs_dep.add_professor(mc_prof)
     lt_dep.add_professor(me_prof)

     mc_prof.set_department(cs_dep)
     me_prof.set_department(lt_dep)

     mc_prof.assign_to_course(python_cs)
     me_prof.assign_to_course(antica_cs)

     python_cs.set_professor(mc_prof)
     antica_cs.set_professor(me_prof)

     student_leandro:Student=Student("Leandro Pazienza",27,"PZN")
     student_cristiano:Student=Student("Cristiano Coccia",21,"CR7")

     univ.add_student(student_leandro)
     univ.add_student(student_cristiano)

     student_cristiano.enroll(python_cs)
     student_leandro.enroll(antica_cs)

     