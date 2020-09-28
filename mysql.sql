CREATE TABLE IF NOT EXISTS User(
      username text NOT NULL,
	  fail_email int NOT NULL,
	  fail_shopping int NOT NULL,
	  fail_banking int NOT NULL,
	  
	  time_email_start text NOT NULL,
	  time_email_end text NOT NULL,
	  
	  time_shopping_start text NOT NULL,
	  time_shopping_end text NOT NULL,
	  
	  time_banking_start text NOT NULL,
	  time_banking_end text NOT NULL,
	  
	  email_password text NOT NULL,
	  shopping_password text NOT NULL,
	  banking_password tex NOT NULL,
      primary key (username)
      );
