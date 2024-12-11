CREATE INDEX index_student_id ON enrollments (student_id);

CREATE INDEX index_course_id ON enrollments (course_id);

CREATE INDEX index_department_number_semester_title ON courses (department, number, semester, title);


