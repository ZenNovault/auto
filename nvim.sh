#!/bin/bash
VER=$(curl -s https://api.github.com/repos/neovim/neovim/releases/latest | grep tag_name | head -1 | cut -d'"' -f4)
wget "https://github.com/neovim/neovim/releases/download/${VER}/nvim-linux-x86_64.tar.gz"
tar -xzf nvim-linux-x86_64.tar.gz
sudo rm -rf /opt/nvim-linux-x86_64 2>/dev/null || true
sudo mv nvim-linux-x86_64 /opt/
sudo ln -sf /opt/nvim-linux-x86_64/bin/nvim /usr/local/bin/nvim
rm nvim-linux-x86_64.tar.gz
echo "Neovim ${VER} installed! Run: nvim --version"

