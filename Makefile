SLD_VIDEODRIVER=wayland
export SLD_VIDEODRIVER
# LD_LIBRARY_PATH="$(nix-build '<nixpkgs>' -A wayland)/lib"
LD_LIBRARY_PATH="/nix/store/1d6ln69plsmbfp6myvbkx4bf39mg8a47-wayland-1.23.1/lib"
export LD_LIBRARY_PATH

run:
	.venv/bin/python main.py