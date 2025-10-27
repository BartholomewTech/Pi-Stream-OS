cat << 'EOF' > setup.sh
#!/bin/bash

# --- Pi-Stream OS Environment Setup ---
# Base OS: Raspberry Pi OS Lite (64-bit)
# Project: Pi-Stream OS (Python + Kivy)

echo "Starting Pi-Stream OS Dependency Installation..."

# 1. Install Minimal Desktop Environment (X11, Window Manager, VNC)
echo "Installing minimal desktop components..."
sudo apt install -y xserver-xorg xinit openbox tightvncserver

# 2. Install Development Tools and Core Libraries
echo "Installing core development tools (git, python, nodejs, curl)..."
sudo apt install -y git python3-pip curl nodejs npm

# 3. Install Media Player and Web Launcher
echo "Installing Media Player (mpv) and Web Browser (Chromium)..."
sudo apt install -y mpv chromium-browser

# 4. Install Kivy Dependencies (for GPU acceleration)
echo "Installing Kivy dependencies and required header files..."
sudo apt install -y build-essential pkg-config libgl1-mesa-dev libgles2-mesa-dev
sudo apt install -y libgstreamer1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-bad python3-dev

# 5. Set up Python Environment (runs in current user's directory: /opt/pistream)
echo "Setting up Python Virtual Environment and installing Kivy..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install kivy python-mpv python-dotenv pillow requests

# 6. Final Configuration for Headless Operation (VNC)
echo "Configuring VNC for remote GUI development..."
# NOTE: VNC Server is started under the current user ('toggle')
vncserver :1 -geometry 1280x720 -depth 24
echo "VNC Server started on port 5901. Connect with VNC Viewer."

echo "Installation Complete. Run 'source venv/bin/activate' to enter environment."
echo "Development will continue in /opt/pistream/"

EOF
