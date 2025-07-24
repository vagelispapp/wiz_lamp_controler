
# 💡 WiZ Lamp Controller (Desktop)

A simple custom desktop GUI to control your **WiZ smart lamps** using their IP addresses — built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and [pywizlight](https://github.com/sbidy/pywizlight).

Control multiple lamps from your PC, choose which ones to toggle, adjust brightness, and turn them ON/OFF directly — all from a modern, lightweight interface.

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
```

---

## 🚀 How to Use

1. Replace the IPs of your lamps in the code:

```python
light_floor = wizlight("192.168.1.X")
light_desk = wizlight("192.168.1.X")
```

2. Run the app:

```bash
python wiz_controler.py
```

3. In the GUI:
   - Select which lamps to control (e.g. Floor, Desk).
   - Adjust the brightness with the slider.
   - Click ON or OFF to apply the command.

4. The window will close automatically and your lamps will respond.

---

## 🛠 Build to EXE (Optional)

You can turn this into a Windows `.exe` using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed wiz_controler.py
```

The `.exe` will be created inside the `dist/` folder.

You may include a `.spec` file to customize the build if needed.

---


## 🧠 How It Works

- Lamp preferences (which ones are selected and brightness) are stored in a `settings` dictionary.
- When the user clicks ON or OFF, the app closes and an `asyncio` function sends the appropriate command using `pywizlight`.
- Supports controlling as many lamps as you want — just add their IPs and checkboxes in the code.

---



## 📸 Preview

<img width="388" height="235" alt="image" src="https://github.com/user-attachments/assets/c33e9548-b58e-473d-b5f5-2b2af6b2ab58" />


---



## 🙋 Support & Contributions

Have a feature request, bug, or suggestion? Feel free to open an issue or a pull request!
