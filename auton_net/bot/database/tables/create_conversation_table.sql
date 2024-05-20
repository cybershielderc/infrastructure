CREATE TABLE `conversation` (
	`initiator_id` BIGINT() DEFAULT '0',
	`participant_id` BIGINT(),
	`nomfi` BIGINT() DEFAULT '0' COMMENT 'Number of Messages from Initiator',
	`nomfp` BIGINT() DEFAULT '0' COMMENT 'Number of Messages from Participant',
	`conversation_initiated` BIGINT() DEFAULT '0' COMMENT 'Time of Initiation in UNIX (32-bit)',
	`isHolding` BIGINT() DEFAULT '1' COMMENT 'Is conversation paused, 0 for False 1 for True',
	`agreed_price` DOUBLE() DEFAULT '0.00' COMMENT 'Price both parties agreed on, can be set via /setprice or via the Client Menu/Seller Menu',
	PRIMARY KEY (`initiator_id`)
) ENGINE=InnoDB;