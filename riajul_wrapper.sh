
if [[ -x "$(command -v python)" ]]
then
    source .venv/bin/activate
    python3 main.py
    
else
    echo "Looks like you don't have Python installed.
        You can download it here - https://www.python.org/downloads/" >&2
    exit 1     
fi