CREATE INDEX index_student_id_course_id ON enrollments (student_id, course_id);

/* CREATE INDEX index_course_id ON enrollments (course_id);*/

CREATE INDEX index_department_number_semester_title ON courses (department, number, semester, title);

CREATE INDEX index_course_id_requirement_id ON satisfies (course_id, requirement_id);

CREATE INDEX index_name ON requirements (name);
