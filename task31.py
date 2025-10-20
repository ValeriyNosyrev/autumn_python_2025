log_entries = [
    "192.168.1.1 - GET /home 200 1.2s",
    "192.168.1.2 - POST /login 404 0.8s",
    "192.168.1.3 - GET /profile 500 2.1s",
    "192.168.1.4 - GET /about 200 0.5s",
    "192.168.1.5 - POST /submit 403 1.5s"
]

# Извлекаем IP, c кодами ответа, содержащими ошибку

ip_error_codes = [
    entry.split()[0]
    for entry in log_entries
    if entry.split()[4].startswith(('4', '5'))
]

print(ip_error_codes)