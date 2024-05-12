CREATE TABLE `customers` IF NOT EXISTS (
	`tg_id` INT(20),
	`open_requests` INT(20) DEFAULT '0',
	`budget` INT(20) DEFAULT '50' COMMENT 'Budget in USDT',
	`reputation` FLOAT(20) DEFAULT '1.0',
	`connected_wallet` TEXT(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '0xdead' COMMENT 'ETH 42-character Hexadecimal Address',
	`nickname` TEXT(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT 'Anonymous' COMMENT 'User Set Nickname',
	`isAnonymous` INT(1) DEFAULT '1',
	`completed_requests` INT(20) DEFAULT '0',
	PRIMARY KEY (`tg_id`)
) ENGINE=InnoDB;