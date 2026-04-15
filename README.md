# 📂 Bulk File Renamer in Python

A simple and efficient Python script to rename multiple files in a directory based on a specified pattern. This tool helps automate file organization and eliminates the need for manual renaming.

---

## 🚀 Features

* 🔍 Filter files using patterns (e.g., `*.txt`, `*.jpg`)
* 🔄 Rename files in bulk with custom naming formats
* 🔢 Automatic numbering with flexible formatting
* ⚡ Fast and lightweight (no external dependencies)
* 🛡️ Basic error handling

---

## 🧠 Use Case

If you have files like:

report_final_v1.txt
report_final_v2.txt

You can rename them to:

document_001.txt
document_002.txt

---

## 🐍 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Large_File_Renamer.git
cd Large_File_Renamer
```

2. Make sure you have Python installed (Python 3.x recommended).

---

## ▶️ Usage

Run the script:

```bash
python Large_File_Renamer.py
```

Then provide:

* 📁 Directory path
* 🔎 File pattern (e.g., `*.txt`)
* ✏️ New naming pattern (e.g., `file_{:03d}.txt`)

---

## 🧾 Example

```
Enter directory path: /Users/yourname/files
Enter file pattern: *.jpg
Enter new naming pattern: image_{:02d}.jpg
```

Output:

```
Renamed: photo1.jpg → image_01.jpg
Renamed: photo2.jpg → image_02.jpg
```

---

## ⚙️ Naming Pattern Guide

| Pattern  | Output Example |
| -------- | -------------- |
| `{}`     | 1, 2, 3        |
| `{:02d}` | 01, 02, 03     |
| `{:03d}` | 001, 002, 003  |

---

## 📁 Project Structure

```
bulk-file-renamer/
│
├── Large_File_Renamer.py
└── README.md
```

---

## ⚠️ Notes

* Make sure your naming pattern includes numbering if needed.
* Existing files with the same name may be overwritten.
* Always test on a small set of files first.

---

## 💡 Future Improvements

* ✅ Preview mode before renaming
* 📂 Recursive renaming (subfolders)
* 🔤 Regex-based file matching
* 🖥️ GUI version

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## ⭐ Support

If you find this useful, please give it a ⭐ on GitHub!
