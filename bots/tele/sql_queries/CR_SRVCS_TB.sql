CREATE TABLE IF NOT EXISTS `services` (
	`id` int(10) NOT NULL auto_increment,
	`user_owner_id` int(10),
	`service_id` int(10),
    `payplan_period` int(10),
	`due_date` datetime,
    `service_created` datetime,
	`paid` numeric(9,2),
	PRIMARY KEY( `id` )
);