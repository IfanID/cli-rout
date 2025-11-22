#!/usr/bin/env python3
"""
Modul ini menyediakan fungsi untuk menampilkan "Message of the Day" (MOTD).

Termasuk ASCII art dan pesan selamat datang untuk antarmuka baris perintah (CLI).
"""

ROUT_ASCII_ART: str = r"""
┌───────────────────────────────────────────┐
│    ██████╗  ██████╗ ██╗   ██╗ ████████╗    │
│    ██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝    │
│    ██████╔╝██║   ██║██║   ██║   ██║       │
│    ██╔══██╗██║   ██║██║   ██║   ██║       │
│    ██║  ██║╚██████╔╝╚██████╔╝   ██║       │
│    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝       │
└───────────────────────────────────────────┘
"""


def display_welcome_message() -> None:
    """
    Menampilkan pesan selamat datang dengan ASCII art.

    Mencetak ASCII art diikuti dengan pesan sapaan ke konsol.
    """
    print(ROUT_ASCII_ART)
    print("Selamat datang di rout CLI!")
