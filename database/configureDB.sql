
CREATE DATABASE continuum;
USE continuum;

CREATE TABLE users(
	id INT AUTO_INCREMENT,
	username VARCHAR(32),
	salt VARCHAR(32),
	password VARCHAR(64),
	is_admin TINYINT(1),
	PRIMARY KEY(id));


INSERT INTO users (
	username,
	salt,
	password,
	is_admin) VALUES (
	'admin',
	'fIM4STPWMSk2Ka9mewIBqeDhYfAxJhAx',
	'8038bbc5fe831ba83988c22c649a2b20747b07f82f648de6cd03e7291f8c5919',
	1);


CREATE TABLE products(
	id INT AUTO_INCREMENT,
	name VARCHAR(32),
	image VARCHAR(32),
	path VARCHAR(100),
	description VARCHAR(100),
	PRIMARY KEY(id));


INSERT INTO products (
	name,
	image,
	path,
	description) VALUES (
	'AI & Productivity',
	'/static/images/ai.jpg',
	'/course/AI_and_Productivity',
	'How to use AI to improve your daily tasks.'
	),(
	'Problem Solving',
	'/static/images/problem.jpg',
	'/course/Problem_Solving',
	'Critical thinking and problem solving.'
	);