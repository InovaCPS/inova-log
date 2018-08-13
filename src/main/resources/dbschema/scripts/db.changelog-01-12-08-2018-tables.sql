--liquibase formatted sql

--changeset nadalete:01
--comment: creation the LOG table structure
CREATE TABLE log_log (
	id bigserial NOT NULL,
	user_name varchar(100) NOT NULL,
	created_datetime timestamp NOT NULL,
	source_host varchar(200) NOT NULL,
	target_host varchar(200) NOT NULL,
	api_url varchar(1000) NULL,
	CONSTRAINT LOG_PK PRIMARY KEY (id)
) WITH (
	OIDS=FALSE
);

--rollback DROP TABLE LOG_LOG;