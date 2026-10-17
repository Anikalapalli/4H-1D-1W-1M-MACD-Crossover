import os
import smtplib
from email.message import EmailMessage

# మీ ట్రేడింగ్ బాట్ కి సంబంధించిన పూర్తి కోడ్ ఇక్కడ ఉంటుంది
# ఉదాహరణకు ఏంజెల్ వన్ (Angel One) SmartAPI స్క్రీనర్ లాజిక్

def run_trading_bot():
    print("ట్రేడింగ్ బాట్ స్క్రీనింగ్ ప్రారంభమవుతోంది...")
    # ఇక్కడ మీ లాజిక్ రన్ అవుతుంది
    report = "Nifty 500 MACD Crossover Screening Completed Successfully."
    return report

def send_email(report_content):
    GMAIL_USER = os.environ.get("GMAIL_USER")
    GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASS")
    EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER", GMAIL_USER)

    msg = EmailMessage()
    msg.set_content(report_content)
    msg['Subject'] = '📊 Nifty 500 MACD Crossover Strategy Report'
    msg['From'] = GMAIL_USER
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    print("প্রোগ্রাম రన్ అవుతోంది...")
    result = run_trading_bot()
    send_email(result)
    print("రిపోర్ట్ విజయవంతంగా ఇమెయిల్ చేయబడింది!")
