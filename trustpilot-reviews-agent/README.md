# TrustPilot Reviews Automation

*Identify your customer's pain points to improve your product or service.*

## Setup Instructions
1. Import the workflow [TrustPilot_Reviews_AI_Automation.json](TrustPilot_Reviews_AI_Automation.json) into your N8N instance.
*Refer the main [README.md](/README.md) file for setting up N8N locally if not already installed.*
2. Open the file [trustpilot_reviews.py](trustpilot_reviews.py) and change the following variable to correctly reflect your company name on TrustPilot:
   ```
   COMPANY_NAME = "[YOUR COMPANY NAME]"
   ```
   to
   ```
   COMPANY_NAME = "homezonefurniture.com"
   ```
   *Note: **"homezonefurniture.com"** is the name of Home Zone Furniture on TrustPilot.*
3. Save the file.
4. Open Terminal, change to the folder where you have cloned this file and run:
```
cd trustpilot-reviews-agent

python trustpilot_reviews.py
```
5. After the program runs successfully, it will create a file called **trustpilot_reviews.xlsx**
6. Copy the contents of this file into a Google Sheet.
7. Make sure your N8N Google Sheets Authentication is setup correctly. If you need assistance, refer the **Support and Assistance** section of the main [README.md](/README.md) file.
8. Run the N8N workflow and ask the Agent a question such as:
```
What are the top 3 pain points customers mention in the reviews
```

## Additional Fun Prompts
Apart from asking the basic question above, you can also gather some interesting insights on your products and services from the reviews by asking the following:
```
Group reviews based on the rating and show the total reviews for each rating.

Provide your analysis of the reviews data. Present in a table form the key statistics.
```