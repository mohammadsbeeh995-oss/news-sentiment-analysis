# News Sentiment Analysis

This project analyzes news article headlines to find out whether their tone is **positive**, **neutral**, or **negative**.  
It uses the **TextBlob** library for sentiment analysis and saves the results in an Excel file.

## ⚙️ How It Works
1. Load data with headlines.
2. Calculate sentiment scores using TextBlob (values between -1 and +1).
3. Classify each headline as:
   - Positive (score > 0.1)
   - Negative (score < -0.1)
   - Neutral (otherwise)
4. Save everything to `analysis.xlsx`.

## Example Output
| Headline | Sentiment Score | Label |
|-----------|-----------------|--------|
| NASA launches new rocket | 0.45 | Positive |
| Rocket test fails | -0.61 | Negative |

## Tools Used
- Python
- pandas
- TextBlob
- openpyxl
- Excel (for chart visualization)

---

Created by **Mohammad Sbeeh**
