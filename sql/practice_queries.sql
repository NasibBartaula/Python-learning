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

select * from sakila.actor_info where last_name in ("CHASE","Guiness");
select * from sakila.actor_info where last_name not in ("CHASE","GUINESS");
select concat(first_name," ", last_name) as fullname from sakila.actor_info;
select concat_ws(" ",first_name, last_name) as fullname from sakila.actor_info;
 
select length(actor_id) as its from sakila.actor_info;
select upper(first_name) as nameas from sakila.actor_info;
select lower(last_name) as nameas from sakila.actor_info;

select left(film_info,9) as film from sakila.actor_info;
select right(film_info,9) as film from sakila.actor_info;
select mid(film_info,1,6) as film from sakila.actor_info;

select count(actor_id) as sum from sakila.actor_info;
select sum(actor_id) as sum from sakila.actor_info;
select avg(actor_id) as sum from sakila.actor_info;
select max(actor_id) as sum from sakila.actor_info;
select min(actor_id) as sum from sakila.actor_info;


select * from sakila.payment;
select date(payment_date) from sakila.payment;
select time(payment_date) from sakila.payment;
select monthname(payment_date) from sakila.payment;
select year(payment_date) from sakila.payment;
select hour(payment_date) from sakila.payment;
select minute(payment_date) from sakila.payment;
select customer_id,rental_id,
case
    when amount<1 then "Low payment"
    else "Payment"
end as amout_detail
from sakila.payment;

select * from sakila.payment;   
select customer_id,count(amount) from sakila.payment group by customer_id order by count(amount) asc ;

select * from sakila.actor;
select * from sakila.film_text;

select * from sakila.film_list
except
select * from sakila.nicer_but_slower_film_list;





































