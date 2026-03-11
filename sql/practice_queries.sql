select * from sakila.actor_info;

select first_name, film_info from sakila.actor_info;

select * from sakila.actor_info where first_name="NICK";

select first_name,film_info from sakila.actor_info where first_name="Zero";

select first_name,film_info from sakila.actor_info where
first_name="nick" and last_name="wahlberg";
select first_name,film_info from sakila.actor_info where
first_name="nick" or last_name="wahlberg";
select first_name,film_info from sakila.actor_info where not
first_name="nick";

select * from sakila.actor_info;
select first_name,last_name from sakila.actor_info where film_info like 'Animation%';
select * from sakila.actor_info order by first_name asc, film_info desc;
select * from sakila.actor_info order by first_name asc, film_info desc limit 2,5;
select * from sakila.actor_info where actor_id between 40 and 50;






































