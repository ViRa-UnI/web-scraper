# original_source_code_downloader.py

```python
import requests

def download_source_code(url, filename):
    response = requests.get(url)
    with open(filename, 'w') as file:
        file.write(response.text)
```
