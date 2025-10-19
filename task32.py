files = [
    "document.pdf",
    "temp_backup.tmp",
    "image.jpg",
    "cache.tmp",
    "report.docx",
    "old_data.bak"
]

temp_files = [
    "/tmp/" + file
    for file in files
    if file.endswith((".tmp", ".bak"))
]

print(temp_files)