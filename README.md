# 🗂️ Auto Backup & File Organizer Tool

A Python automation tool that organizes files into categorized folders by file type and creates timestamped backups — built for IT Support and Helpdesk use cases to reduce manual file management effort.

---

## 📌 Project Overview

| Field        | Details                                      |
|--------------|-----------------------------------------------|
| **Author**   | Priyanshu Negi                                 |
| **Language** | Python 3.x                                     |
| **Domain**   | IT Support / Automation                        |
| **Type**     | CLI Tool                                       |
| **GitHub**   | [igpriyanshunegi/auto-backup-file-organizer](https://github.com/igpriyanshunegi/auto-backup-file-organizer) |

---

## ⚙️ Features

- ✅ **Auto File Organization** — sorts files into Documents, Images, Videos, Audio, Archives, Scripts, and Others based on file extension
- ✅ **Folder Backup** — creates a timestamped `.zip` backup of any folder
- ✅ **Organize + Backup Combo** — backs up the folder first, then organizes it
- ✅ **Dry Run Mode** — preview all changes before anything is actually moved
- ✅ **Duplicate-Safe Handling** — automatically renames files instead of overwriting existing ones
- ✅ **Action Logging** — every move/backup action is logged with a timestamp for audit-ready documentation
- ✅ **Error Handling** — skips locked/inaccessible files gracefully instead of crashing

---

## 📥 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/igpriyanshunegi/auto-backup-file-organizer.git
```

### 2. Navigate into the folder
```bash
cd auto-backup-file-organizer
```

### 3. No external dependencies required
This tool only uses Python's built-in libraries (`os`, `shutil`, `logging`, `datetime`).

---

## ▶️ How to Run

```bash
python auto_backup_organizer.py
```

You will see a menu:
```
Choose an option:
  1. Organize a folder by file type
  2. Backup a folder (create zip)
  3. Organize + Backup (both)
  4. Exit
```

### Recommended first run:
1. Choose **Option 1**
2. Enter the folder path
3. Type `y` for **Dry Run** to preview changes
4. Review the preview, then confirm to organize for real

---

## 📁 File Categories

| Category   | Extensions |
|------------|-----------|
| Documents  | .pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx, .csv |
| Images     | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp |
| Videos     | .mp4, .mkv, .avi, .mov, .wmv |
| Audio      | .mp3, .wav, .aac, .flac |
| Archives   | .zip, .rar, .7z, .tar, .gz |
| Scripts    | .py, .js, .html, .css, .java, .cpp, .c, .sh, .bat |
| Others     | Any unmatched file type |

---

## 📊 Sample Output

```
============================================================
   AUTO BACKUP & FILE ORGANIZER TOOL
   Author: Priyanshu Negi
============================================================

Choose an option:
  1. Organize a folder by file type
  2. Backup a folder (create zip)
  3. Organize + Backup (both)
  4. Exit

Enter choice (1-4): 1
Enter folder path to organize: C:\Users\user1\PycharmProjects\Auto backup organizer
Dry run first? (y/n): y

============================================================
Organizing folder: C:\Users\user1\PycharmProjects\Auto backup organizer
Mode: DRY RUN (preview only)
============================================================

  [PREVIEW] Would move: sample1.pdf  -->  Documents/
  [PREVIEW] Would move: sample2.pdf  -->  Documents/
  [PREVIEW] Would move: photo1.png   -->  Images/
  [PREVIEW] Would move: photo2.png   -->  Images/

------------------------------------------------------------
SUMMARY
------------------------------------------------------------
  Documents   : 2 file(s)
  Images      : 2 file(s)
------------------------------------------------------------

Proceed with actual organizing? (y/n): y
```

---

## 📁 Project Structure

```
auto-backup-file-organizer/
│
├── auto_backup_organizer.py    # Main script
├── organizer_log_*.log         # Auto-generated logs (created on run)
└── README.md                   # Project documentation
```

---

## 💡 Use Cases

- IT Support staff cleaning up shared drives or downloads folders
- Helpdesk teams maintaining organized backups before system changes
- Anyone needing a quick automated file management/backup solution
- Learning Python file handling, automation, and logging

---

## 🔗 Connect

- **GitHub** : [github.com/igpriyanshunegi](https://github.com/igpriyanshunegi)
- **LinkedIn** : [linkedin.com/in/igpriyanshunegi](https://www.linkedin.com/in/igpriyanshunegi)
- **Email** : priyanshun898@gmail.com
