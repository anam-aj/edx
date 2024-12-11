CREATE INDEX index_student_id ON enrollments (student_id);

CREATE INDEX index_course_id ON enrollments (course_id);

CREATE INDEX index_department ON courses (department);

CREATE INDEX index_number ON courses (number);

CREATE INDEX index_semester ON courses (semester);

CREATE INDEX index_course_id_requirement_id ON satisfies (course_id, requirement_id);

CREATE INDEX index_name ON requirements (name);



/* CREATE INDEX index_course_id ON enrollments (course_id);*/
