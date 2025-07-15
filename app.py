print("Importing Flask")
from flask import Flask, request, send_file

print("Importing pywhatkit")
import pywhatkit as kit

print("Importing pyautogui")
import pyautogui

print("Importing time")
import time

print("All imports done")

app = Flask(__name__)

def whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
    time.sleep(2)
    pyautogui.press("enter")
    return "Message sent"

@app.route('/')
def form():
    return send_file("index.html")

@app.route('/send', methods=['POST'])
def handle_form():
    number = request.form.get('number')
    message = request.form.get('message')
    result = whatsapp_message(number, message)
    return f"<h3>✅ {result} to {number}</h3><a href='/'>Back</a>"
    
if __name__ == '__main__':
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    print(f"✅ Flask is running at http://{ip}:5000 or http://127.0.0.1:5000")
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

