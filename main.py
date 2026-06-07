from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>เว็บแรกของฉัน</title>
        <style>
            body { 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white; 
                font-family: sans-serif;
                text-align: center;
                padding-top: 100px;
            }
            h1 { font-size: 3em; }
            button {
                padding: 15px 30px;
                font-size: 1.2em;
                background: #ff6b6b;
                border: none;
                border-radius: 10px;
                color: white;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>🎉 สำเร็จแล้ว!</h1>
        <p>นี่คือเว็บแรกที่รันบน GitHub Codespace</p>
        <p>พอร์ต 8001 ทำงานปกติ</p>
        <button onclick="alert('คุณเก่งมาก!')">กดฉันสิ</button>
    </body>
    </html>
    """
