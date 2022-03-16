import os

try:
    from win32gui import GetDoubleClickTime as double_click_time
except ImportError:
    def double_click_time():
        return int(os.environ.get("DOUBLE_CLICK_TIME", 500))


__all__ = ("double_click_time",)
