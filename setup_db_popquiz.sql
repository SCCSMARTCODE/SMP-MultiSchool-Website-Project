CREATE DATABASE IF NOT EXISTS smp_base_db;

CREATE USER IF NOT EXISTS 'smp_master'@'localhost' IDENTIFIED BY 'smp_pass_master';
GRANT ALL PRIVILEGES ON smp_base_db.* TO 'smp_master'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- smp_master
-- smp_pass_master
-- localhost
-- smp_base_db
