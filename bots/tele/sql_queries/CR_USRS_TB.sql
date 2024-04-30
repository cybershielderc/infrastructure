CREATE TABLE IF NOT EXISTS `users` (
	`id` int(10) NOT NULL auto_increment,
	`tg_id` varchar(255),
	`'wallet_address'` varchar(255),
	`dc_id` varchar(255),
    `isVerified` numeric(9,2),
	PRIMARY KEY( `id` )
);