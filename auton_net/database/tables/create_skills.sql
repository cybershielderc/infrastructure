CREATE TABLE IF NOT EXISTS `skills`
(
    `tg_id`      INT(20)                                      DEFAULT '0',
    `time`       FLOAT(20)                                    DEFAULT '0.5' COMMENT 'Experience Time, In Years',
    `skill_name` TEXT(32) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT 'Solidity',
    PRIMARY KEY (`tg_id`)
);