CREATE TABLE IF NOT EXISTS `developers`
(
    `tg_id`                 BIGINT                                        DEFAULT '0',
    `linked_portfolio_rid`  INT(20)                                       DEFAULT '0',
    `accepted_budget_min`   INT(20)                                       DEFAULT '100',
    `accepted_budget_max`   INT(20)                                       DEFAULT '200',
    `accepted_worktime_min` INT(20)                                       DEFAULT '4' COMMENT 'In Days',
    `accepted_worktime_max` INT(20)                                       DEFAULT '6' COMMENT 'In Days',
    `rating`                FLOAT(20)                                     DEFAULT '1.0',
    `isVerified`            INT(1)                                        DEFAULT '0',
    `isAnonymous`           INT(1)                                        DEFAULT '1',
    `nickname`              TEXT(50) CHARACTER SET utf8 COLLATE utf8_bin  DEFAULT 'Anonymous Developer',
    `connected_wallet`      TEXT(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '0xdead' COMMENT 'ETH 42-character Hexadecimal Address',
    `completed_orders`      INT(20)                                       DEFAULT '0',
    `open_orders`           INT(20)                                       DEFAULT '0',
    `rejected_orders`       INT(20)                                       DEFAULT '0',
    `avg_completion_time`   FLOAT(20)                                     DEFAULT '1.5' COMMENT 'In Hours',
    `isAddressVerified`     INT(1)                                        DEFAULT '0',
    PRIMARY KEY (`tg_id`)
) ENGINE = InnoDB;