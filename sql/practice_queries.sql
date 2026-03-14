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

select * from sakila.payment;
select avg(amount) from sakila.payment;

select * from sakila.payment where amount >=4.2;

select * from sakila.payment where amount >
(select avg(amount) from sakila.payment);

select * from sakila.actor
where first_name in (select staff.first_name from sakila.staff);

select * from sakila.actor
where first_name not in (select staff.first_name from sakila.staff);

create view total as
select customer_id , sum(amount) from sakila.payment
group by customer_id;

select * from total;

delimiter &&
create procedure get_it()
begin
	select * from sakila.payment where amount >=4.2;
end &&
delimiter ;
call get_it();    

delimiter &&
create procedure get_limit(in var int)
begin
	select * from sakila.payment limit var;
end &&
delimiter ;
call get_limit(3);    

delimiter &&
create procedure get_credit(out var int)
begin
	select max(amount) into var from sakila.payment;
end &&
delimiter ;
call get_credit(@abc);
select @abc;   

delimiter &&
create procedure get_name(inout var int)
begin
	select payment.amount from sakila.payment where customer_id = var;
end &&
delimiter ;
set @m=2;
call get_name(@m);   
	
select customer_id, SUM(amount) as total_payment
from sakila.payment
group by customer_id;    

select customer_id, rental_id, amount
from sakila.payment
order by amount desc
limit 5;

select date(payment_date) as payment_day,
       SUM(amount) as daily_revenue
from sakila.payment
group by payment_day
order by payment_day;
     



































