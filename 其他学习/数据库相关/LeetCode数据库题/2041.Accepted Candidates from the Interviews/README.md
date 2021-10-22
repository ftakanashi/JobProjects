## 题目描述
Table: Candidates
```
+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| candidate_id | int      |
| name         | varchar  |
| years_of_exp | int      |
| interview_id | int      |
+--------------+----------+
```
candidate_id is the primary key column for this table.
Each row of this table indicates the name of a candidate, their number of years of experience, and their interview ID.
Table: Rounds
```
+--------------+------+
| Column Name  | Type |
+--------------+------+
| interview_id | int  |
| round_id     | int  |
| score        | int  |
+--------------+------+
```
(interview_id, round_id) is the primary key column for this table.
Each row of this table indicates the score of one round of an interview.
Write an SQL query to report the IDs of the candidates who have at least two years of experience and the sum of the score of their interview rounds is strictly greater than 16.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:
```
Input: 
Candidates table:
+--------------+---------+--------------+--------------+
| candidate_id | name    | years_of_exp | interview_id |
+--------------+---------+--------------+--------------+
| 11           | Atticus | 1            | 101          |
| 9            | Ruben   | 6            | 104          |
| 6            | Aliza   | 10           | 109          |
| 8            | Alfredo | 0            | 107          |
+--------------+---------+--------------+--------------+
Rounds table:
+--------------+----------+-------+
| interview_id | round_id | score |
+--------------+----------+-------+
| 109          | 3        | 4     |
| 101          | 2        | 8     |
| 109          | 4        | 1     |
| 107          | 1        | 3     |
| 104          | 3        | 6     |
| 109          | 1        | 4     |
| 104          | 4        | 7     |
| 104          | 1        | 2     |
| 109          | 2        | 1     |
| 104          | 2        | 7     |
| 107          | 2        | 3     |
| 101          | 1        | 8     |
+--------------+----------+-------+
Output: 
+--------------+
| candidate_id |
+--------------+
| 9            |
+--------------+
Explanation: 
- Candidate 11: The total score is 16, and they have one year of experience. We do not include them in the result table because of their years of experience.
- Candidate 9: The total score is 22, and they have six years of experience. We include them in the result table.
- Candidate 6: The total score is 10, and they have ten years of experience. We do not include them in the result table because the score is not good enough.
- Candidate 8: The total score is 6, and they have zero years of experience. We do not include them in the result table because of their years of experience and the score.
```

### 解法 内联结 + group by
这道题不知道为什么诡异的出现在我的首页上，第一题下面第二题上面…

顺手做了：
```sql
# Write your MySQL query statement below
select candidate_id
from Candidates join Rounds on Candidates.interview_id = Rounds.interview_id 
where years_of_exp >= 2 
group by candidate_id
having sum(score) >= 16;
```
不确定是不是最优解，总之能AC了。
另外题目明明说了strictly greater than 16，但是SQL还是得写`>=16`。有些用例的输出设置错了…