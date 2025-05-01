from flask import Flask, render_template
import os

app = Flask(__name__, 
            static_folder='barberia_scraper/static', 
            template_folder='barberia_scraper/templates')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Configuración para desarrollo local
    # app.run(debug=True, host='127.0.0.1', port=8000)
    
    # Configuración para producción en Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 