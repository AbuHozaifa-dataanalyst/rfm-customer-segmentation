

/* =====================================================
   RFM ANALYSIS - ADVANCED VERSION
   ===================================================== */

-- 1️⃣ Clean Base (Safety Layer)
WITH base_data AS (
    SELECT
        customer_id,
        invoice_no,
        invoice_date,
        quantity,
        unit_price,
        TotalAmount
    FROM clean_retail_data
    WHERE customer_id IS NOT NULL
      AND quantity > 0
      AND unit_price > 0
),

-- 2️⃣ Snapshot Date
snapshot AS (
    SELECT DATEADD(DAY, 1, MAX(invoice_date)) AS snapshot_date
    FROM base_data
),

-- 3️⃣ Core RFM Calculation
rfm_base AS (
    SELECT
        customer_id,
        MAX(invoice_date) AS last_purchase_date,
        COUNT(DISTINCT invoice_no) AS frequency,
        SUM(TotalAmount) AS monetary
    FROM base_data
    GROUP BY customer_id
),

-- 4️⃣ Add Recency
rfm_calc AS (
    SELECT
        r.customer_id,
        DATEDIFF(DAY, r.last_purchase_date, s.snapshot_date) AS recency,
        r.frequency,
        r.monetary
    FROM rfm_base r
    CROSS JOIN snapshot s
),

-- 5️⃣ RFM Scoring (Using NTILE)
rfm_scores AS (
    SELECT *,
        NTILE(5) OVER (ORDER BY recency DESC) AS R_score,
        NTILE(5) OVER (ORDER BY frequency ASC) AS F_score,
        NTILE(5) OVER (ORDER BY monetary ASC) AS M_score
    FROM rfm_calc
),

-- 6️⃣ Segment Mapping
rfm_segments AS (
    SELECT *,
        CASE
            WHEN R_score >= 4 AND F_score >= 4 AND M_score >= 4 THEN 'Champions'
            WHEN R_score >= 3 AND F_score >= 3 THEN 'Loyal Customers'
            WHEN R_score >= 4 AND F_score <= 2 THEN 'Potential Loyalists'
            WHEN R_score <= 2 AND F_score >= 3 THEN 'At Risk'
            WHEN R_score <= 2 AND F_score <= 2 THEN 'Lost Customers'
            ELSE 'Others'
        END AS segment
    FROM rfm_scores
)

-- 7️⃣ Final Output
SELECT *
FROM rfm_segments
ORDER BY segment, monetary DESC;