import requests
from datetime import datetime

def visit_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"✓ [{timestamp}] Página visitada exitosamente")
        print(f"  Status Code: {response.status_code}")
        print(f"  URL: {url}")
        return response.status_code
    except requests.exceptions.Timeout:
        print(f"✗ Error: Timeout al intentar acceder a {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"✗ Error al visitar la página: {e}")
        return None

if __name__ == "__main__":
    # ⚠️ CAMBIA ESTA URL POR "
    
    print("=" * 50)
    print("Iniciando visita a la página...")
    print("=" * 50)
    
    visit_page(URL)
    
    print("=" * 50)
    print("Proceso completado")
    print("=" * 50)
