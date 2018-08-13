--liquibase formatted sql

--changeset nadalete:02
--comment: insert into the LOG table a set of test data
insert into log_log (user_name, created_datetime, source_host, target_host, api_url) values ('nadalete', current_timestamp, '192.168.0.140', '10.15.16.78', 'https://inova.cps.edu.br/cvlattes/1');
insert into log_log (user_name, created_datetime, source_host, target_host, api_url) values ('sakaue', current_timestamp, '192.168.0.141', '10.15.16.78', 'https://inova.cps.edu.br/cvlattes/456');
insert into log_log (user_name, created_datetime, source_host, target_host, api_url) values ('italo', current_timestamp, '192.168.0.142', '10.15.16.78', 'https://inova.cps.edu.br/cvlattes/34');
insert into log_log (user_name, created_datetime, source_host, target_host, api_url) values ('mauro', current_timestamp, '192.168.0.143', '10.15.16.78', 'https://inova.cps.edu.br/cvlattes/987');

--rollback DELETE * FROM LOG_LOG;