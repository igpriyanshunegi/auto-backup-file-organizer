"""
=============================================================
  Auto Backup & File Organizer Tool
  Author  : Priyanshu Negi
  GitHub  : github.com/igpriyanshunegi
  Version : 1.0
  Purpose : Automated file organization and backup utility
            for IT Support / Helpdesk use cases
=============================================================

Features:
  1. Organizes files in a folder into sub-folders by file type
     (Documents, Images, Videos, Audio, Archives, Scripts, Others)
  2. Creates a timestamped backup (zip) of any folder
  3. Logs every action (move/copy) into a log file for audit trail
  4. Supports dry-run mode (preview changes without making them)
"""

import os
import shutil
import datetime
import logging
import sys

# ─────────────────────────────────────────────
#  FILE TYPE MAPPING
# ─────────────────────────────────────────────
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos":    [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio":     [".mp3", ".wav", ".aac", ".flac"],
    "Archives":  [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts":   [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".sh", ".bat"],
    "Others":    []  # fallback for unmatched extensions
}

# ─────────────────────────────────────────────
#  LOGGER SETUP
# ─────────────────────────────────────────────
def setup_logger():
    log_filename = f"organizer_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    return log_filename

def log_and_print(message, level="info"):
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)


# ─────────────────────────────────────────────
#  GET CATEGORY FOR A FILE
# ─────────────────────────────────────────────
def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


# ─────────────────────────────────────────────
#  ORGANIZE FILES BY TYPE
# ─────────────────────────────────────────────
def organize_folder(target_folder, dry_run=False):
    if not os.path.isdir(target_folder):
        log_and_print(f"[ERROR] Folder not found: {target_folder}", "error")
        return

    log_and_print(f"\n{'='*60}")
    log_and_print(f"Organizing folder: {target_folder}")
    log_and_print(f"Mode: {'DRY RUN (preview only)' if dry_run else 'LIVE'}")
    log_and_print(f"{'='*60}\n")

    moved_count = 0
    skipped_count = 0
    summary = {}

    for item in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item)

        # Skip folders and the script itself
        if os.path.isdir(item_path):
            continue

        category = get_category(item)
        category_folder = os.path.join(target_folder, category)

        if not dry_run:
            os.makedirs(category_folder, exist_ok=True)

        dest_path = os.path.join(category_folder, item)

        # Avoid overwriting existing files
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(item)
            timestamp = datetime.datetime.now().strftime("%H%M%S")
            dest_path = os.path.join(category_folder, f"{base}_{timestamp}{ext}")

        if dry_run:
            log_and_print(f"  [PREVIEW] Would move: {item}  -->  {category}/")
        else:
            try:
                shutil.move(item_path, dest_path)
                log_and_print(f"  [MOVED] {item}  -->  {category}/")
                moved_count += 1
            except Exception as e:
                log_and_print(f"  [SKIPPED] {item} ({e})", "warning")
                skipped_count += 1
                continue

        summary[category] = summary.get(category, 0) + 1

    log_and_print(f"\n{'-'*60}")
    log_and_print("SUMMARY")
    log_and_print(f"{'-'*60}")
    for cat, count in summary.items():
        log_and_print(f"  {cat:<12}: {count} file(s)")
    if not dry_run:
        log_and_print(f"\n  Total moved   : {moved_count}")
        log_and_print(f"  Total skipped : {skipped_count}")
    log_and_print(f"{'-'*60}\n")


# ─────────────────────────────────────────────
#  BACKUP FOLDER (ZIP WITH TIMESTAMP)
# ─────────────────────────────────────────────
def backup_folder(source_folder, backup_destination="."):
    if not os.path.isdir(source_folder):
        log_and_print(f"[ERROR] Source folder not found: {source_folder}", "error")
        return None

    folder_name = os.path.basename(os.path.normpath(source_folder))
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{folder_name}_backup_{timestamp}"
    backup_path = os.path.join(backup_destination, backup_name)

    log_and_print(f"\n{'='*60}")
    log_and_print(f"Creating backup of: {source_folder}")
    log_and_print(f"{'='*60}")

    try:
        archive_path = shutil.make_archive(backup_path, "zip", source_folder)
        size_mb = os.path.getsize(archive_path) / (1024 * 1024)
        log_and_print(f"  [SUCCESS] Backup created: {archive_path}")
        log_and_print(f"  [INFO] Backup size: {size_mb:.2f} MB")
        return archive_path
    except Exception as e:
        log_and_print(f"  [ERROR] Backup failed: {e}", "error")
        return None


# ─────────────────────────────────────────────
#  MENU / MAIN
# ─────────────────────────────────────────────
def print_banner():
    print(f"\n{'='*60}")
    print("   AUTO BACKUP & FILE ORGANIZER TOOL")
    print("   Author: Priyanshu Negi")
    print(f"   {datetime.datetime.now().strftime('%A, %d %B %Y  %H:%M:%S')}")
    print(f"{'='*60}\n")


def main():
    print_banner()
    log_file = setup_logger()
    print(f"Log file created: {log_file}\n")

    print("Choose an option:")
    print("  1. Organize a folder by file type")
    print("  2. Backup a folder (create zip)")
    print("  3. Organize + Backup (both)")
    print("  4. Exit")

    choice = input("\nEnter choice (1-4): ").strip()

    if choice == "1":
        folder = input("Enter folder path to organize: ").strip()
        dry = input("Dry run first? (y/n): ").strip().lower() == "y"
        organize_folder(folder, dry_run=dry)
        if dry:
            confirm = input("\nProceed with actual organizing? (y/n): ").strip().lower()
            if confirm == "y":
                organize_folder(folder, dry_run=False)

    elif choice == "2":
        folder = input("Enter folder path to backup: ").strip()
        dest = input("Enter backup destination (leave blank for current folder): ").strip() or "."
        backup_folder(folder, dest)

    elif choice == "3":
        folder = input("Enter folder path: ").strip()
        dest = input("Enter backup destination (leave blank for current folder): ").strip() or "."
        backup_folder(folder, dest)
        organize_folder(folder, dry_run=False)

    elif choice == "4":
        print("Exiting. Goodbye!")
        sys.exit(0)

    else:
        print("Invalid choice. Please run the script again.")

    print(f"\n{'='*60}")
    print("  Task complete. Check the log file for full details.")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()