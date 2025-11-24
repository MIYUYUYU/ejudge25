import zipfile
import sys
import io

inp = sys.stdin.read()
zip_file = ''.join(inp.split())
bin_data = bytes.fromhex(zip_file)
with zipfile.ZipFile(io.BytesIO(bin_data),'r') as zf:
    file_count = 0
    file_size = 0
    for info in zf.infolist():
        if not info.filename.endswith('/'):
            file_count += 1
            file_size += info.file_size

    print(f"{file_count} {file_size}")