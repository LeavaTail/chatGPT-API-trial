## System Requirements

- Windows 11 (23H2)

## Create develop environment

1. Install Python 3.12 from Microsoft Store
2. Install Python VSCode Extensions
3. Open Command Palette By exter `Ctrl` + `Shift` + `P`
4. `Python: Create Environment.`>`Venv`>`Python 3.12`
5. `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
6. `.\.venv\Scripts\Activate.ps1`
7. `pip install -r requirements.txt`

## Setup voiceroid

1. Download AssistantSeika from https://wiki.hgotoh.jp/documents/tools/assistantseika/assistantseika-001a
2. Execute AssistantSeikaSetup2.msi
3. Copy `WCFClient/WCFClient.dll` to project directory
4. Copy `SeikaSay2/SeikaSay2.exe` to project directory