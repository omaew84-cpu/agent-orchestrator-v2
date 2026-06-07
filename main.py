from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>สำเร็จแล้ว!</title>
        <style>
            body {
                margin: 0;
                font-family: sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: center;
                padding-top: 100px;
                min-height: 100vh;
            }
            .card {
                background: rgba(255,255,255,0.15);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
                max-width: 400px;
                margin: 0 auto;
                box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            }
            h1 { font-size: 2.5em; margin-bottom: 20px; }
            .status {
                background: rgba(255,255,255,0.2);
                padding: 10px 20px;
                border-radius: 50px;
                display: inline-block;
                margin: 20px 0;
            }
            button {
                background: #ff6b6b;
                border: none;
                padding: 15px 30px;
                border-radius: 50px;
                color: white;
                font-size: 1.1em;
                cursor: pointer;
                margin-top: 20px;
                transition: transform 0.2s;
            }
            button:hover { transform: scale(1.05); }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🎉 สำเร็จแล้ว!</h1>
            <p>นี่คือเว็บแรกที่รันบน GitHub Codespace</p>
            <div class="status">🟢 พอร์ต 8001 ทำงานปกติ</div>
            <br>
            <button onclick="alert('คุณเก่งมาก! แมวทำได้แล้วนะ ✨')">กดเลย ✨</button>
        </div>
        <p style="margin-top: 40px; opacity: 0.8;">⚡ GitHub Codespaces</p>
        <p style="opacity: 0.6;">🚀 Ready to Code</p>
    </body>
    </html>
    """)

@app.get("/api")
def api_status():
    return {"สถานะ": "กำลังทำงาน", "ng": "v2"}
