"""
Standalone launcher for Flag Duel.
Opens index.html in a native window via pywebview (WebView2 on Windows).
Build: pyinstaller "Flag Duel.spec"  ->  dist/Flag Duel.exe
"""
import os
import sys
import webview


def resource_path(rel):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)


def main():
    webview.create_window(
        "Flag Duel",
        resource_path("index.html"),
        width=1100,
        height=860,
        resizable=True,
        confirm_close=False,
    )
    webview.start()


if __name__ == "__main__":
    main()
