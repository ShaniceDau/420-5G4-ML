import sys
from pathlib import Path

import customtkinter as ctk

sys.path.insert(0, str(Path(__file__).resolve().parent / "build"))

import _cpp_backend


def main() -> None:
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Application test Python / C++")
    app.geometry("420x200")

    label = ctk.CTkLabel(
        app,
        text=_cpp_backend.message(),
        font=ctk.CTkFont(size=18),
    )
    label.pack(expand=True)

    app.mainloop()


if __name__ == "__main__":
    main()
