CREATE TABLE IF NOT EXISTS `order`
(
    `order_id`           BIGINT AUTO_INCREMENT,
    `customer`           BIGINT DEFAULT '0' COMMENT 'Telegram ID of the customer that created the order',
    `accepted_developer` BIGINT COMMENT 'Telegram ID of the developer who accepted the order',
    `order_occupied`     BIGINT DEFAULT '0' COMMENT 'Is the order occupied',
    `desired_price`      BIGINT DEFAULT '0' COMMENT 'Desired price set by customer',
    `agreed_price`       BIGINT DEFAULT '0' COMMENT 'Price agreed to by both parties',
    `desired_timeframe`  DOUBLE DEFAULT '1.0' COMMENT 'Desired timeframe in days',
    `agreed_timeframe`   BIGINT DEFAULT '0' COMMENT 'Timeframe agreed to by both parties',
    `desired_revisions`  BIGINT DEFAULT '0' COMMENT 'Desired revisions in which product should be completed',
    `agreed_revisions`   BIGINT DEFAULT '0' COMMENT 'Timeframe agreed to by both parties',
    PRIMARY KEY (`order_id`)
) ENGINE = InnoDB;