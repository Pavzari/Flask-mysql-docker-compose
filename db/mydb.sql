use pav;

CREATE TABLE `user` (
`id` INTEGER PRIMARY KEY AUTO_INCREMENT,
`name` varchar(100) NOT NULL,
`role` varchar(100) NOT NULL
);

INSERT into `user` (`name`, `role`) values
('Pav', 'Trainee'),
('Rachael', 'Trainee'),
('Jiten', 'Teacher');
