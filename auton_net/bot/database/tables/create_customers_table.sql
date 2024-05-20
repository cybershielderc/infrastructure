CREATE TABLE IF NOT EXISTS `customers`
(
    `tg_id`              BIGINT,
    `open_requests`      BIGINT                                        DEFAULT '0',
    `min_budget`         BIGINT                                        DEFAULT '50' COMMENT 'Budget in USDT',
    `max_budget`         BIGINT                                        DEFAULT '100' COMMENT 'Budget in USDT',
    `reputation`         FLOAT(20)                                     DEFAULT '1.0',
    `connected_wallet`   TEXT(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '0xdead' COMMENT 'ETH 42-character Hexadecimal Address',
    `nickname`           TEXT(50) CHARACTER SET utf8 COLLATE utf8_bin  DEFAULT 'Anonymous' COMMENT 'User Set Nickname',
    `isAnonymous`        BIGINT                                        DEFAULT '1',
    `completed_requests` BIGINT                                        DEFAULT '0',
    PRIMARY KEY (`tg_id`)
) ENGINE = InnoDB;