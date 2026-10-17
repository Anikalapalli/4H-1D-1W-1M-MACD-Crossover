import os
import smtplib
from email.message import EmailMessage
from google import genai  # సరికొత్త లైబ్రరీ

# గిట్‌హబ్ సీక్రెట్స్ నుండి కీలను తీసుకోవడం
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GMAIL_USER = os.environ.get("GMAIL_USER")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASS")

def generate_macro_report():
    # సరికొత్త క్లైంట్ ఇనిషియలైజేషన్
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    prompt = """
    ప్రపంచ ప్రఖ్యాత ఇన్‌స్టిట్యూషనల్ ఇన్వెస్టర్లు మరియు హెడ్జ్ ఫండ్స్ తరహాలో, గ్లోబల్ ఎకానమీలోని 11 ప్రధాన సెక్టార్లలో 
    (ఇన్‌ఫర్మేషన్ టెక్నాలజీ, ఎనర్జీ, ఫైనాన్షియల్స్, హెల్త్‌కేర్ & ఫార్మా, కన్స్యూమర్ గూడ్స్, మెటల్స్ & మైనింగ్, ఆటోమొబైల్స్, 
    రియల్ ఎస్టేట్, అగ్రికల్చర్, యుటిలిటీస్ మరియు టెలికాం) రాబోయే 2 లేదా 3 నెలల్లో బయటి ప్రపంచానికి తెలియకముందే 
    రాబోయే కీలకమైన మార్పులపై, ముందస్తు సంకేతాలపై (Leading Indicators) మరియు FIIల పెట్టుబడుల సరళిపై (Alpha Strategies) 
    తెలుగులో అత్యంత లోతైన మరియు ప్రొఫెషనల్ విశ్లేషణను అందించండి.
    """
    
    # సరికొత్త మోడల్
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
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
    print("గ్లోబల్ మార్కెట్ విశ్లేషణ ప్రారంభమవుతోంది...")
    report = generate_macro_report()
    print("విశ్లేషణ పూర్తయింది, ఇమెయిల్ పంపుతోంది...")
    send_email(report)
    print("ఇమెయిల్ విజయవంతంగా పంపబడింది!")
