CREATE INDEX index_student_id ON enrollments (student_id);

CREATE INDEX index_enrollment_course_id ON enrollments (course_id);

CREATE INDEX index_department ON courses (department);

CREATE INDEX index_number ON courses (number);

CREATE INDEX index_semester ON courses (semester);

CREATE INDEX index_satisfies_course_id ON satisfies (course_id);

CREATE INDEX index_requirement_id ON satisfies (requirement_id);
