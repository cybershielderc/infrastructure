CREATE TABLE `developers`
(
    `tg_id`                INT(20)                                      DEFAULT '0',
    `linked_portfolio_rid` INT(20)                                      DEFAULT '0',
    `accepted_budget_min`  INT(20)                                      DEFAULT '100',
    `accepted_budget_max`  INT(20)                                      DEFAULT '200',
    `accepted_worktime`    INT(20)                                      DEFAULT '4' COMMENT 'In Days',
    `rating`               FLOAT(20)                                    DEFAULT '1.0',
    `isVerified`           INT(1)                                       DEFAULT '0',
    `isAnonymous`          INT(1)                                       DEFAULT '1',
    `nickname`             TEXT(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT 'Anonymous Developer',
    PRIMARY KEY (`tg_id`)
) ENGINE = InnoDB;