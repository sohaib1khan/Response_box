#!/bin/bash

# Function to check for Python
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON=python3
        PIP=pip3
    elif command -v python &> /dev/null; then
        PYTHON=python
        PIP=pip
    else
        echo "Python is not installed. Please install Python to proceed."
        exit 1
    fi
}

# Function to install necessary Python libraries
install_libraries() {
    echo "Installing required Python libraries..."
    $PIP install --upgrade pip
    $PIP install pyinstaller
}

# Function to package the Canned Response Manager app with PyInstaller
package_app() {
    echo "Packaging the Canned Response Manager app with PyInstaller..."

    # Check for the app script
    if [ ! -f "app.py" ]; then
        echo "Error: 'app.py' file is required in the project folder."
        exit 1
    fi

    # Run PyInstaller to create a one-file executable
    $PYTHON -m PyInstaller --onefile --noconsole app.py

    if [ $? -eq 0 ]; then
        echo "Packaging completed successfully."
    else
        echo "An error occurred during packaging."
        exit 1
    fi
}

# Function to display usage instructions
show_instructions() {
    echo -e "\nSetup Complete!\n"
    echo "To run the packaged app, navigate to the 'dist' directory and execute the app file as shown below:"
    echo "For Linux: ./dist/app"
    echo "For Windows: dist\\app.exe (if built on Windows)"
    echo "Make sure to transfer the executable to the target system if needed."
}

# Main script execution
check_python
install_libraries
package_app
show_instructions
