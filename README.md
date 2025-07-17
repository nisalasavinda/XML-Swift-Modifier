# SwiftSwap

*Seamlessly update SWIFT codes inside your XML transaction files with ease!*

---

## 🚀 What is SwiftSwap?

SwiftSwap is a lightweight Python tool designed to automate the tedious task of updating SWIFT codes in bulk XML transaction files. It intelligently scans each XML file for specified institution names and replaces old SWIFT codes with new ones — saving you time and eliminating manual errors.

If you’re dealing with large volumes of XML data and need precision changes on financial identifiers, SwiftSwap is your go-to solution!

---

## ⚙️ Features

- 🔍 **Targeted Search:** Looks for institution names exactly or partially matching your criteria.
- 🔄 **Safe Replacement:** Only updates SWIFT codes when both institution name and old SWIFT code match.
- 📂 **Batch Processing:** Automatically processes every `.xml` file in a folder.
- 💾 **Non-destructive:** Modifies files only when necessary, preserving data integrity.
- 🛠️ **Robust Error Handling:** Catches XML parsing issues and reports file-specific errors.

---

## 📦 Installation

No complicated setup or external libraries — SwiftSwap uses only Python’s built-in modules.

Make sure you have **Python 3.6+** installed.

---

## 🧰 Usage

1. **Clone the repo or download the script**

```bash
git clone https://github.com/yourusername/SwiftSwap.git
cd SwiftSwap
