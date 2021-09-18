SELECT COUNT(DISTINCT user_id) AS users
FROM `bq-analysis-study.sample.customers`
WHERE FORMAT_DATE("%Y", birthday) BETWEEN "1980" AND "1989"