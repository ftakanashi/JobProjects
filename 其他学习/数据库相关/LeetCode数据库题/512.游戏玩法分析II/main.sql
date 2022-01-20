# Solution 1
# Write your MySQL query statement below

# 第一种写法
select a.player_id, a.device_id from activity a
join
(select player_id, min(event_date) as min_date from activity group by player_id) b
on
a.player_id=b.player_id and a.event_date=b.min_date;

# 第二种写法
select a.player_id, a.device_id from activity a, (select player_id, min(event_date) as min_date from activity group by player_id) b
where a.player_id=b.player_id and a.event_date=b.min_date;