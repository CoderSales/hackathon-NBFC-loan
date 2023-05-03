multi() {
    python -m venv .venv
    . $PWD/.venv/Scripts/activate
    pip install --upgrade pip
    python.exe -m pip install --upgrade pip
    pip install -r requirements.txt
    # pip install tensorflow
}

multi