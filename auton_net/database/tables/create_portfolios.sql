CREATE TABLE IF NOT EXISTS `portfolio`
(
    `id`                INT(20) AUTO_INCREMENT COMMENT 'Used as an RID in developers table',
    `portfolio_summary` TEXT(128) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT 'Developer Portfolio Summary',
    `text1`             TEXT(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT 'Text Block #1',
    `text2`             TEXT(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT 'Text Block #2',
    `skills_tgid`       INT(20)                                       DEFAULT '0' COMMENT 'Relationship ID to skills table',
    `contact_tgid`      INT(20)                                       DEFAULT '0' COMMENT 'Relationship',
    PRIMARY KEY (`id`)
);