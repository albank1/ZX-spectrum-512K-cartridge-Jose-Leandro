###########################################################################################################
#
# This Python program is takes the menu.scr, and the roms A.rom, B.rom and inserts into the original rom
#
# menu.scr is the menu for the rom and is in .scr ZX Spectrum screen image
# A.rom, B.rom to O.rom are 16KB Rom images
#
# Written by Alban Killingback 22/2/2025
###########################################################################################################

ROM_SIZE = 0x80000  # 4Mbits 4MB ZX Spectrum paged ROM size
MENU_ADDR = 0x0500  # Injection address in ROM
PAGE_SIZE = 0x4000  # 16 KB per page

# Load the original ROM
with open("original.rom", "rb") as rom_file:
    rom_data = bytearray(rom_file.read())

# Ensure the ROM size is correct
if len(rom_data) != ROM_SIZE:
    raise ValueError(f"Original ROM size must be exactly {ROM_SIZE} bytes, but got {len(rom_data)} bytes.")

# Load the menu screen binary
with open("menu.scr", "rb") as menu_file:
    menu_data = menu_file.read()

# Ensure menu.scr is exactly 6912 bytes
if len(menu_data) != 6912:
    raise ValueError(f"menu.scr must be exactly 6912 bytes, but got {len(menu_data)} bytes.")

# Inject the binary into the ROM at 0x0500
rom_data[MENU_ADDR:MENU_ADDR + len(menu_data)] = menu_data

# Load A.rom at 0x4000
with open("A.rom", "rb") as a_rom_file:
    a_rom_data = a_rom_file.read()
if len(a_rom_data) != PAGE_SIZE:
    raise ValueError(f"A.rom must be exactly {PAGE_SIZE} bytes, but got {len(a_rom_data)} bytes.")
rom_data[0x4000:0x4000 + PAGE_SIZE] = a_rom_data

# Load B.rom at 0x8000
with open("B.rom", "rb") as b_rom_file:
    b_rom_data = b_rom_file.read()
if len(b_rom_data) != PAGE_SIZE:
    raise ValueError(f"B.rom must be exactly {PAGE_SIZE} bytes, but got {len(b_rom_data)} bytes.")
rom_data[0x8000:0x8000 + PAGE_SIZE] = b_rom_data

# Load C.rom at 0xC000
with open("C.rom", "rb") as c_rom_file:
    c_rom_data = c_rom_file.read()
if len(c_rom_data) != PAGE_SIZE:
    raise ValueError(f"C.rom must be exactly {PAGE_SIZE} bytes, but got {len(b_rom_data)} bytes.")
rom_data[0xC000:0xC000 + PAGE_SIZE] = c_rom_data

# Load D.rom at 0x10000
#with open("D.rom", "rb") as d_rom_file:
#    d_rom_data = d_rom_file.read()
#if len(d_rom_data) != PAGE_SIZE:
#    raise ValueError(f"C.rom must be exactly {PAGE_SIZE} bytes, but got {len(b_rom_data)} bytes.")
#rom_data[0x10000:0x10000 + PAGE_SIZE] = d_rom_data

# Load E.rom at 0x14000
#with open("E.rom", "rb") as e_rom_file:
#    e_rom_data = e_rom_file.read()
#if len(e_rom_data) != PAGE_SIZE:
#    raise ValueError(f"C.rom must be exactly {PAGE_SIZE} bytes, but got {len(b_rom_data)} bytes.")
#rom_data[0x14000:0x14000 + PAGE_SIZE] = e_rom_data

# Save the modified ROM
with open("compilation.rom", "wb") as output_file:
    output_file.write(rom_data)

print("Compilation ROM created successfully.")


