# Definitions
FX	= # Handshake initiate
FV	= # Handshake verify?
FC	= # Sonar data request
BUSY	= # Sonar is busy
REDYFX	= # Handshake received

# Commands to sonar
FX	= "46581500000000000000000000000000000000b3000000000000000000"
FV	= "46561500000000000000000000000000000000b1000000000000000000"
FC	= "464315002c0100000000000000040000000000cf000a4f0079f5be0000"

# Commands to computer
BUSY	= "ff00ff000a0042555359"
REDYFX	= "ff00ff00200052454459465816000100303030303030373937360a4f0079f5be"

# Disclaimer
# The definitions are just assumptions so feel free to correct them.
# The commands may change depending on unknown variables (time, device, etc)
