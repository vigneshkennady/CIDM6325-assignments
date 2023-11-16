

### Develop Natural Language statements 

In order to track and store the degree requirement and checklist for the students of WTAMU, we need to take care of below items

Each degree program consists of core curriculum courses, which are categorized into various university core requirements. Students complete these courses, and the details of their completion, including the grade and completion date, are recorded. The core curriculum courses are also associated with multiple university core requirements. Additionally, each degree program is located in a specific department. Overall, this system captures the relationship between degree programs, core curriculum courses, university core requirements, students, and the completion of courses by students."



* Record existing advising service Degree Program in the app which is searchable alphabetically and college and department
* Record the total Core Curriculum Courses hours required by student to complete the degree
* Record the University Core Requirements courses hours to complete the course 
* Capture the sub-group requirement for core curriculum courses hours and Degree requirement core hours
* Capture the number of course hours and grade needed to complete the degree in each sub-group
* Capture the allowed courses allowed in each sub-group

Record the student’s current completion status, hours earned, grade against the group, sub-group and course


### ERD notation using crow-foot

Entities identified



* Student
* DegreeProgram
* Course
* Department
* CoreRequirement
* DegreeSpecificRequirement

Relationships:



* EnrollsIn (between Student and DegreeProgram)
    * Student (1) ----&lt; EnrollsIn >---- (0..1) DegreeProgram
* BelongsTo (between DegreeProgram and Department)
    * DegreeProgram (1) ----&lt; BelongsTo >---- (1) Department
* Requires (between DegreeProgram and CoreRequirement)
    * DegreeProgram (1) ----&lt; Requires >---- (*) CoreRequirement
* Includes (between CoreRequirement and Course)
    * CoreRequirement (1) ----&lt; Includes >---- (*) Course
* Has (between DegreeProgram and DegreeSpecificRequirement)
    * DegreeProgram (1) ----&lt; Has >---- (*) DegreeSpecificRequirement
* Includes (between DegreeSpecificRequirement and Course)
    * DegreeSpecificRequirement (1) ----&lt; Includes >---- (*) Course
* Has (between Course and Department)
    * Course (1) ----&lt; Has >---- (1) Department

Notation Explanation:



* (1) represents "One"
* (*) represents "Many"

----&lt; represents "One" (Crow's foot pointing to the "One" side)

---- represents "Many" (Crow's foot pointing to the "Many" side)

This Crow's Foot notation indicates the cardinality of relationships. For example, "Student (1) ----&lt; EnrollsIn >---- (0..1) DegreeProgram" means that one student can enroll in zero or one degree program, and one degree program can have many enrolled students.


### Three forms of the diagram


### Conceptual ERD:


#### In the Conceptual ERD, we focus on high-level entities and relationships without specifying details like attributes or data types.



* Entities:
    1. Student: Represents a student.
    2. DegreeProgram: Represents a degree program.
    3. Department: Represents an academic department.
    4. CoreRequirement: Represents the core curriculum requirements.
* Relationships:
    5. EnrollsIn: Connects a student to a degree program.
    6. BelongsTo: Connects a degree program to a department.
    7. Requires: Connects a degree program to core curriculum requirements.
    8. Includes: Connects core curriculum requirements to courses.
    9. Has: Connects a degree program to DegreeSpecific requirements.
    10. Includes (DegreeSpecific): Connects DegreeSpecific requirements to courses.
    11. BelongsTo (Course): Connects a course to a department.

Entities:



* Student
* DegreeProgram
* Course
* Department
* CoreRequirement
* DegreeSpecificRequirement

Relationships:



1. EnrollsIn:
    * Student (1) ----&lt; EnrollsIn >---- (0..1) DegreeProgram
2. BelongsTo:
    * DegreeProgram (1) ----&lt; BelongsTo >---- (1) Department
3. Requires:
    * DegreeProgram (1) ----&lt; Requires >---- (*) CoreRequirement
4. Includes:
    * CoreRequirement (1) ----&lt; Includes >---- (*) Course
5. Has:
    * DegreeProgram (1) ----&lt; Has >---- (*) DegreeSpecificRequirement
6. Includes (DegreeSpecific):
    * DegreeSpecificRequirement (1) ----&lt; Includes >---- (*) Course
7. BelongsTo (Course):
    * Course (1) ----&lt; BelongsTo >---- (1) Department
  

![Image](https://github.com/vigneshkennady/CIDM6325-assignments/blob/main/assignment2/assignment2/ConceptualERD.drawio.png)


### Logical ERD:


#### In the Logical ERD, we introduce attributes for each entity and indicate relationships with cardinality.



* Entities with Attributes:
    1. Student: Contains attributes like StudentID, FirstName, LastName, etc.
    2. DegreeProgram: Contains attributes like ProgramID, ProgramName, TotalCredits, etc.
    3. Department: Contains attributes like DepartmentID, DepartmentName, etc.
    4. CoreRequirement: Contains attributes like RequirementID, RequirementName, etc.
    5. DegreeSpecificRequirement: Contains attributes like DegreeSpecificReqID, DegreeSpecificReqName, etc.
    6. Course: Contains attributes like CourseID, CourseName, Credits, etc.
* Relationships with Cardinality:
    7. EnrollsIn: A student enrolls in zero or one degree program, and a degree program can have many enrolled students.
    8. BelongsTo: A degree program belongs to one department, and a department can have many degree programs.
    9. Requires: A degree program requires zero or more core curriculum requirements, and a core curriculum requirement is required by one or more degree programs.
    10. Includes: A core curriculum requirement includes zero or more courses, and a course can be included in one or more core curriculum requirements.
    11. Has: A degree program has zero or more DegreeSpecific requirements, and an DegreeSpecific requirement is associated with one or more degree programs.
    12. Includes (DegreeSpecific): An DegreeSpecific requirement includes zero or more courses, and a course can be included in one or more DegreeSpecific requirements.
    13. BelongsTo (Course): A course belongs to one department, and a department can have many courses.

Entities with Attributes:



* Student (StudentID, FirstName, LastName, etc.)
* DegreeProgram (ProgramID, ProgramName, TotalCredits, etc.)
* Course (CourseID, CourseName, Credits, etc.)
* Department (DepartmentID, DepartmentName, etc.)
* CoreRequirement (RequirementID, RequirementName, etc.)
* DegreeSpecificRequirement (DegreeSpecificReqID, DegreeSpecificReqName, etc.)

Relationships with Cardinality:



2. EnrollsIn:
    * Student (1) ----&lt; EnrollsIn >---- (0..1) DegreeProgram
3. BelongsTo:
    * DegreeProgram (1) ----&lt; BelongsTo >---- (1) Department
4. Requires:
    * DegreeProgram (1) ----&lt; Requires >---- (*) CoreRequirement
5. Includes:
    * CoreRequirement (1) ----&lt; Includes >---- (*) Course
6. Has:
    * DegreeProgram (1) ----&lt; Has >---- (*) DegreeSpecificRequirement
7. Includes (DegreeSpecific):
    * DegreeSpecificRequirement (1) ----&lt; Includes >---- (*) Course

![Image](https://github.com/vigneshkennady/CIDM6325-assignments/blob/main/assignment2/assignment2/Logical.drawio.png)


### Physical ERD:


#### In the Physical ERD, we add data types, primary keys (PK), and foreign keys (FK) to specify the implementation details.



* Example Attributes with Data Types:
    * For each entity, attributes are accompanied by their respective data types (e.g., int, varchar).
* Example Foreign Keys:
    * We indicate where foreign keys are used to establish relationships between entities. Foreign keys are linked to the primary keys in other tables, creating referential integrity.

Example Attributes with Data Types:



* Student (StudentID: int, FirstName: varchar, LastName: varchar, etc.)
* DegreeProgram (ProgramID: int, ProgramName: varchar, TotalCredits: int, etc.)
* Course (CourseID: int, CourseName: varchar, Credits: int, etc.)
* Department (DepartmentID: int, DepartmentName: varchar, etc.)
* CoreRequirement (RequirementID: int, RequirementName: varchar, etc.)
* DegreeSpecificRequirement (DegreeSpecificReqID: int, DegreeSpecificReqName: varchar, etc.)

Example Foreign Keys:



* EnrollsIn (StudentID-FK, ProgramID-FK)
* BelongsTo (ProgramID-FK, DepartmentID-FK)
* Requires (ProgramID-FK, RequirementID-FK)
* Includes (RequirementID-FK, CourseID-FK)
* Has (ProgramID-FK, DegreeSpecificReqID-FK)
* Includes (DegreeSpecificReqID-FK, CourseID-FK)
* BelongsTo (CourseID-FK, DepartmentID-FK)

  ![Image](https://github.com/vigneshkennady/CIDM6325-assignments/blob/main/assignment2/assignment2/physical.drawio.png)


