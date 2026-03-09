select * from sakila.actor_info;

select first_name, film_info from sakila.actor_info;

select * from sakila.actor_info where first_name="NICK";

select first_name,film_info from sakila.actor_info where first_name="Zero";

select first_name,film_info from sakila.actor_info where
first_name="nick" and last_name="wahlberg";
select first_name,film_info from sakila.actor_info where
first_name="nick" or last_name="wahlberg";
select first_name,film_info from sakila.actor_info where not
first_name="nick" 

