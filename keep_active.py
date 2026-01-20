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
    # ⚠️ CAMBIA ESTA URL POR LA TUYA
    URL = "https://www.ejemplo.com"
    
    print("=" * 50)
    print("Iniciando visita a la página...")
    print("=" * 50)
    
    visit_page(URL)
    
    print("=" * 50)
    print("Proceso completado")
    print("=" * 50)
```

4. **MUY IMPORTANTE**: Cambia `https://www.ejemplo.com` por la URL de tu página
5. Haz clic en **"Commit changes..."**
6. En el mensaje deja "Create keep_active.py" y haz clic en **"Commit changes"**

## Paso 4: Crear archivo de dependencias

1. Haz clic nuevamente en **"Add file"** → **"Create new file"**
2. Nombre del archivo: `requirements.txt`
3. Escribe solo esto:
```
requests
