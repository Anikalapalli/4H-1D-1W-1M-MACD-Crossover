import os
import smtplib
from email.message import EmailMessage
import google.generativeai as genai

# మీ జెమిని ఏపీఐ కీని ఇక్కడ నేరుగా ఇవ్వండి
GEMINI_API_KEY = "మీ_జెమిని_ఏపీఐ_కీ_ఇక్కడ_ఇవ్వండి"
GMAIL_USER = "anikalapallijilani@gmail.com" # మీ జిమెయిల్
GMAIL_APP_PASSWORD = "మీ_యాప్_పాస్‌వర్డ్" # మీ జిమెయిల్ యాప్ పాస్‌వర్డ్

genai.configure(api_key=GEMINI_API_KEY)

def generate_macro_report():
    prompt = """
    ప్రపంచ ప్రఖ్యాత ఇన్‌స్టిట్యూషనల్ ఇన్వెస్టర్లు మరియు హెడ్జ్ ఫండ్స్ తరహాలో, గ్లోబల్ ఎకానమీలోని 11 ప్రధాన సెక్టార్లలో 
    (ఇన్‌ఫర్మేషన్ టెక్నాలజీ, ఎనర్జీ, ఫైనాన్షియల్స్, హెల్త్‌కేర్ & ఫార్మా, కన్స్యూమర్ గూడ్స్, మెటల్స్ & మైనింగ్, ఆటోమొబైల్స్, 
    రియల్ ఎస్టేట్, అగ్రికల్చర్, యుటిలిటీస్ మరియు టెలికాం) రాబోయే 2 లేదా 3 నెలల్లో బయటి ప్రపంచానికి తెలియకముందే 
    రాబోయే కీలకమైన మార్పులపై, ముందస్తు సంకేతాలపై (Leading Indicators) మరియు ఆల్ఫా వ్యూహాలపై (Alpha Strategies) 
    తెలుగులో అత్యంత లోతైన మరియు ప్రొఫెషనల్ విశ్లేషణను అందించండి.
    """
    
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(prompt)
    return response.text

def send_email(report_content):
    msg = EmailMessage()
    msg.set_content(report_content)
    msg['Subject'] = '🚀 Elite Alpha & Predictive Macro Strategy Alert - 11 Sectors'
    msg['From'] = GMAIL_USER
    msg['To'] = GMAIL_USER

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    print("మార్కెట్ విశ్లేషణ ప్రారంభమవుతోంది...")
    report = generate_macro_report()
    print("విశ్లేషణ పూర్తయింది, ఇమెయిల్ పంపుతోంది...")
    send_email(report)
    print("ఇమెయిల్ విజయవంతంగా పంపబడింది!")
