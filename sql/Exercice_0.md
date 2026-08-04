```sql
CREATE DATABASE school;

CREATE TABLE student (
    id INTEGER PRIMARY KEY,

    f_name VARCHAR(63) NOT NULL,
    l_name VARCHAR(127) NOT NULL,
    birthdate DATE NOT NULL,
    age SMALLINT CHECK(age > 0) NOT NULL,
    grade VARCHAR(15) NOT NULL,

    created_at TIMESTAMP CURRENT_TIMESTAMP,
    updated_at TIMESTAMP CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL
)

CREATE TABLE teacher(
    id INTEGER PRIMARY KEY,

    f_name VARCHAR(63) NOT NULL,
    l_name VARCHAR(127) NOT NULL,
    class_id INTEGER NOT NULL,

    created_at TIMESTAMP CURRENT_TIMESTAMP,
    updated_at TIMESTAMP CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL
)

CREATE TABLE class(
    id INTEGER PRIMARY KEY,

    name VARCHAR(31) NOT NULL,

    created_at TIMESTAMP CURRENT_TIMESTAMP,
    updated_at TIMESTAMP CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL
)

CREATE TABLE grade(
    id INTEGER PRIMARY KEY,

    grade NUMERIC(3,1) CHECK(grade >= 0 AND grade <= 20) NOT NULL,
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,

    created_at TIMESTAMP CURRENT_TIMESTAMP,
    updated_at TIMESTAMP CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL
)

CONSTRAINT fk_teacher_class_id
    FOREIGN KEY teacher(class_id)
    REFERENCES class(id)

CONSTRAINT fk_score_student_id
    FOREIGN KEY grade(student_id)
    REFERENCES student(id)

CONSTRAINT fk_score_class_id
    FOREIGN KEY grade(class_id)
    REFERENCES class(id)
```
