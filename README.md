# Canned Response Manager

A simple Python-based desktop application to create, manage, and use canned responses. This app allows you to add, edit, delete, preview, and copy canned responses, making it ideal for support teams or anyone who frequently uses pre-written messages.

---

## Features

- **Add, Edit, Delete, and Copy Responses**: Easily manage your canned responses with an intuitive GUI.
- **Persistent Storage**: Save responses persistently in a local JSON file (`responses.json`).
- **Preview Responses**: View the details of any stored response before using it.
- **Search Functionality**: Quickly search through stored responses.
- **User-Friendly GUI**: Built with `Tkinter` for simplicity and usability.
- **Cross-Platform Support**: Compatible with Linux, Windows, and macOS.

---

## Requirements

### Libraries
The following Python libraries are required:

- `tkinter` (included with Python)
- `json` (included with Python)
- `os` (included with Python)

If you want to bundle the app into an executable, you’ll also need:

- `PyInstaller`

Install PyInstaller & tk using pip:

```bash
python3 -m venv venv  && source venv/bin/activate
pip install pyinstaller
pip install tk
```

---

## Running the App

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sohaib1khan/Response_box.git
   cd Response_box
   ```

2. **Run the App**:

   Ensure you have Python installed (version 3.6 or higher):

   ```bash
   
   python3 app.py
   ```

---

## Bundling the App into an Executable

You can create a standalone executable for the application so it can be run without Python installed.

### Steps to Bundle the App

1. **Install PyInstaller**:
   
   ```bash
   pip install pyinstaller
   ```

2. **Create the Executable**:
   
   Run the following command to package the app into a single executable file:

   ```bash
   pyinstaller --onefile --noconsole app.py
   ```

   - `--onefile`: Packages everything into a single file.
   - `--noconsole`: Hides the console window (useful for GUI apps).

3. **Locate the Executable**:

   The executable will be in the `dist/` directory inside your project folder.

   - On Linux: `./dist/app`
   - On Windows: `./dist/app.exe`
   - On macOS: `./dist/app`

4. **Run the Executable**:
   
   ```bash
   ./dist/app
   ```

---

## Repository Structure

```plaintext
Response_box/
├── app.py         # Main application file
├── media/         # Media files for demos and icons
│   ├── demo1.png
│   ├── demo2.png
│   ├── demo3.png
│   ├── demo4.png
│   └── responsebox.gif
├── responses.json # Local file to store canned responses (auto-created at runtime)
├── runsetup.sh    # Bash script to set up dependencies and prepare the app
└── README.md      # Documentation file
```

---

## Notes

- Make sure to include the `responses.json` file in the same directory as the `app.py` if you want to retain saved responses.
- For cross-platform builds, use tools like Wine (to build Windows executables on Linux) or build directly on the target platform.

---

## Demo

Check out the following demo to see the app in action:

### App Play
![Response Box in Action](https://github.com/sohaib1khan/Response_box/blob/main/media/responsebox.gif)

### Start-Up
![Demo1 - Start-Up Screen](https://github.com/sohaib1khan/Response_box/blob/main/media/demo1.png)

### Adding Key/Title for Message
![Demo2 - Adding Key/Title](https://github.com/sohaib1khan/Response_box/blob/main/media/demo2.png)

### Adding Message
![Demo3 - Adding a Message](https://github.com/sohaib1khan/Response_box/blob/main/media/dem3.png)

### Review Added Message
![Demo4 - Reviewing Added Message](https://github.com/sohaib1khan/Response_box/blob/main/media/demo4.png)


