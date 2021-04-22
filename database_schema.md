//// -- LEVEL 1
//// -- Tables and References

// business rules
// setup a CRON job that creates an entry 
// within finance_payouts table for every 
// financial_income in the 
// finance_active_tutors_sessions Table

// Table Users is entered from a form 
Table users as U {
  id int [pk, increment] // auto-increment
  firebase_id int //this comes from googlefirebase
  first_name varchar
  last_name varchar
  created_at timestamp
  active_flag varbinary
}
//Table user_data is entered from a form 
Table user_data {
  id int [pk, increment]
  name_as_on_tax_return varchar
  business_name varchar
  address varchar
  city varchar
  state varchar
  zip varchar
  tax_classification varchar
  ssn varchar
  ein varchar
  exempt_payee_code varchar
  expemption_from_fatca_code varchar
  checkbox_backup_withholding varbinary
  signature_image varchar
  signature_date datetime
  email varchar
  cell int
  state_certification varchar///TBD
  five_star_rating int
 }
 //Table financial_income is entered from a form 
Table financial_income {
  id int [pk, increment]
  school_name varchar
  amount int
  start_date datetime
  expiration_date datetime
  created_at timestamp
 }
 //Table finance_active_tutors_sessions is entered from a form 
Table finance_active_tutors_sessions{
  id int [pk, increment]
  day varchar
   
  time time
  student varchar
  video_link varchar
  cost int
  screen_shot file 
  verified_show varbinary
 }
  //Table finance_payouts is generaged Hasura CRON job
Table finance_payouts{
  id int [pk, increment]
  first_name u.first_name
  last_name u.last_name
  pay_to_email user_data.email
  pay_amount finance_active_tutors_sessions,cost
  approved varbinary
 }
 
// Business Functions
//CRON Job 1
//For every line in finance_active_tutor_sessions, create a new line in 
//finance_payouts with the necessary data
//CRON Job 2
//For every line in finance_payouts and finance_payouts.approved == true, 
//call Tipalti API with the necessary data

