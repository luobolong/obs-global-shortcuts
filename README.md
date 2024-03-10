This guide provides instructions for setting up the Python script that interacts with OBS through global shortcuts in KDE Plasma.

Before proceeding with this setup, ensure you follow the guidelines provided in the [Arch Wiki](https://wiki.archlinux.org/title/Open_Broadcaster_Software#Global_shortcuts_in_KDE_not_working) to address any issues with global shortcuts in KDE not working with OBS.

## Usage

1. **Clone the Repository**

Clone the `obs-global-shortcuts` repository to your local machine.

```bash
git clone https://github.com/luobolong/obs-global-shortcuts.git --depth=1
```

2. **Install Python 3.9**

Install Python 3.9 using the AUR helper `paru`.

```bash
paru -S python39
```

If you encounter a GPG key error like "gpg: keyserver receive failed: Server indicated a failure", perform the following steps:

1. Visit keyserver.ubuntu.com.
2. Search for and download the necessary GPG keys.
3. Import the keys using the command, replacing `key1.asc` with the actual file name of the key you downloaded:

```bash
gpg --import key1.asc
```

3. **Setting Up the Virtual Environment**

Create and activate a new Python virtual environment named `python39`.

```bash
python -m venv python39
source python39/bin/activate
```

Install the packages by running:

```bash
pip install -r requirements.txt
```

You can deactivate the virtual environment afterward by executing:

```bash
deactivate
```

4. **Configuring the Script**

Make sure to replace `/your/path/to/obs-global-shortcuts`, `'yourpassword'`, and `'yourscene'` with your specific details:

```bash
source /your/path/to/obs-global-shortcuts/python39/bin/activate && (python /your/path/to/obs-global-shortcuts/switch_scene.py --ip 127.0.0.1 --port 4455 --password 'yourpassword' --scene 'yourscene' || true) && deactivate
```

5. **Keyboard Shortcut Configuration in KDE Plasma**

To use the script with a global shortcut in KDE Plasma:

1. Open **System Settings**.
2. Navigate to **Keyboard** > **Shortcuts**.
3. Add a new command using the script command you prepared earlier.