CREATE TABLE IF NOT EXISTS `transactions`
(
    `t_uuid`                TEXT(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '000-ignore',
    `t_hash`                TEXT(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '0xdead',
    `sender_telegram_id`    BIGINT                                        DEFAULT '0',
    `recipient_telegram_id` BIGINT                                        DEFAULT '0',
    `amount_sent`           TEXT(128) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '000-ignore' COMMENT 'Amount in Wei stored as text to avoid the limitations of Int and Bigint',
    `amount_usd`            TEXT(128) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '000-ignore' COMMENT 'Amount in USD (at time of transaction!)',
    PRIMARY KEY (`t_uuid`)
) ENGINE = InnoDB;