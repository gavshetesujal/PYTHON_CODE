# Step 1: Import the regular expression module
import re

# Step 2: Store the text in a variable
text=""" 
Hello Students!
For any  queries, contact abs@gmail.com or teacher123@collage.edu.com
You can also contact support@yahoo.com ."""

#
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}'

#Step 4: Find all email addresses in the text
emails =re.findall(email_pattern,text)

# Step 5: Display a heading
print("Email addresses found:")

# Step 6: Display each email address
for email in emails:
    print(email)
