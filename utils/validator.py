
def validate_volume(volume: float) -> None:
    """
    Validasi volume limbah.

    Args:
        volume (float): Volume limbah.

    Raises:
        ValueError: Jika volume negatif.
    """
    if volume < 0:
        raise ValueError("Volume limbah tidak boleh negatif.")


def validate_status(status: str) -> None:
    """
    Validasi status limbah.

    Args:
        status (str): Status limbah.
    """
    allowed_status = [
        "TERCATAT",
        "DALAM_PENGANGKUTAN",
        "DIPROSES",
        "SELESAI"
    ]
    if status not in allowed_status:
        raise ValueError(f"Status '{status}' tidak valid.")
