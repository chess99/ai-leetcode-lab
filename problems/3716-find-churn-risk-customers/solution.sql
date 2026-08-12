-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T02:47:49Z
-- Experiment: ai-leetcode-lab, round 1
WITH ranked AS (
    SELECT se.*,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY event_date DESC, event_id DESC
           ) AS rn
    FROM subscription_events se
), user_stats AS (
    SELECT user_id,
           MAX(CASE WHEN rn = 1 THEN event_type END) AS current_event,
           MAX(CASE WHEN rn = 1 THEN plan_name END) AS current_plan,
           MAX(CASE WHEN rn = 1 THEN monthly_amount END) AS current_monthly_amount,
           MAX(monthly_amount) AS max_historical_amount,
           SUM(event_type = 'downgrade') AS downgrade_count,
           DATEDIFF(MAX(event_date), MIN(event_date)) AS days_as_subscriber
    FROM ranked
    GROUP BY user_id
)
SELECT user_id,
       current_plan,
       current_monthly_amount,
       max_historical_amount,
       days_as_subscriber
FROM user_stats
WHERE current_event <> 'cancel'
  AND downgrade_count >= 1
  AND current_monthly_amount * 2 < max_historical_amount
  AND days_as_subscriber >= 60
ORDER BY days_as_subscriber DESC, user_id;
