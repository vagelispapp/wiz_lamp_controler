# 💡 WiZ Lamp Controller (Desktop)

A simple custom desktop GUI to control your WiZ smart lamps using their IP addresses — 
built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) 
and [pywizlight](https://github.com/sbidy/pywizlight).

Control multiple lamps from your PC, choose which ones to toggle, adjust brightness, and turn them ON/OFF directly 
all from a modern, lightweight interface.

---

## 🖥 Features

- ✅ Turn individual lamps ON or OFF
- 🎚 Adjust brightness with a vertical slider
- 🖱 Custom checkboxes to select specific lamps (e.g., Floor Lamp, Desk Lamp)
- 🖼 Built with a modern Tkinter UI (`customtkinter`)
- 🛠 Uses `pywizlight` to talk directly to your WiZ bulbs via local IP
- 🧱 Easily portable to `.exe` via `PyInstaller` for Windows users

---

## 📦 Requirements

Make sure you have Python 3.8 or newer installed.

Install dependencies:

```bash
pip install customtkinter pywizlight
