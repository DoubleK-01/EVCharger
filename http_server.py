from flask import Flask, jsonify, request, abort, make_response, render_template_string, redirect, url_for
import sqlite3

app = Flask(__name__)

# Veritabanı bağlantısı
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn


# Veritabanında kullanıcı oluşturma
def create_user_table():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, api_key TEXT UNIQUE)')
    conn.execute('INSERT OR IGNORE INTO users (api_key) VALUES ("admin")')
    conn.commit()
    conn.close()


# API anahtarı (örneğin, "admin")
API_KEY = "admin"

# Basit bir şarj durumu değişkeni
charging_status = {
    "connected": False,
    "charging": False,
    "voltage": 0,
    "current": 0
}

# Giriş sayfası HTML şablonu
login_page_html = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EV Charger Login</title>
</head>
<body>
    <h2>EV Charger Giriş</h2>
    <form method="post" action="/login">
        <label for="api_key">API Key:</label>
        <input type="text" id="api_key" name="api_key" required>
        <button type="submit">Giriş Yap</button>
    </form>
</body>
</html>
'''

# Ana sayfa - giriş sayfasını göster
@app.route('/', methods=['GET'])
def home():
    return render_template_string(login_page_html)

# Giriş işlemi
@app.route('/login', methods=['POST'])
def login():
    api_key = request.form.get("api_key")
    # SQL sorgusu ile kullanıcıyı doğrula
    conn = get_db_connection()
    # Tehlikeli! Sadece eğitim amacıyla.
    user = conn.execute(f"SELECT * FROM users WHERE api_key = '{api_key}'").fetchone()
    
    #sql injection protection   user = conn.execute('SELECT * FROM users WHERE api_key = ?', (api_key,)).fetchone()
    
    conn.close()
    
    if user:
        # Giriş başarılıysa durumu gösteren sayfaya yönlendir
        return redirect(url_for('get_status'))
    else:
        # Hatalı giriş durumunda uyarı mesajı döndür
        return render_template_string(login_page_html + "<p style='color: red;'>Geçersiz API anahtarı, lütfen tekrar deneyin.</p>")

# Şarj durumunu kontrol et
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(charging_status)

# Şarj başlatma komutu
@app.route('/start_charging', methods=['POST'])
def start_charging():
    api_key = request.headers.get("X-API-KEY")
    if api_key != API_KEY:
        abort(403)
    charging_status["connected"] = True
    charging_status["charging"] = True
    charging_status["voltage"] = 230
    charging_status["current"] = 16
    return jsonify({"message": "Charging started"})

# Şarj durdurma komutu
@app.route('/stop_charging', methods=['POST'])
def stop_charging():
    api_key = request.headers.get("X-API-KEY")
    if api_key != API_KEY:
        abort(403)
    charging_status["charging"] = False
    charging_status["voltage"] = 0
    charging_status["current"] = 0
    return jsonify({"message": "Charging stopped"})

if __name__ == '__main__':
    create_user_table()  # Kullanıcı tablosunu oluştur
    app.run(host='0.0.0.0', port=5000)

