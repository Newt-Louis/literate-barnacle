import subprocess, os, re

ui_input = "ui/forms/main_window.ui"
py_output = "ui/windows/origin_interface/main_window.py"

# 1️⃣ Convert file .ui → .py
subprocess.run(["pyside6-uic", ui_input, "-o", py_output], check=True)

# 2️⃣ Đọc và sửa import icons_rc
with open(py_output, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r"^import icons_rc",
    "from ui.resources import icons_rc",
    content,
    flags=re.MULTILINE
)

# 3️⃣ Ghi lại
with open(py_output, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Converted and fixed imports in {py_output}")
