from datetime import datetime


def get_current_timestamp() -> str:
    """
    Mendapatkan timestamp saat ini dalam format ISO.

    Returns:
        str: Waktu saat ini (YYYY-MM-DD HH:MM:SS)
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
