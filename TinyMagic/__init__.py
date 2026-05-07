from .logic import TinyMagicLogic

class TinyMagic(TinyMagicLogic):
    """
    This class exposes the keywords from the obfuscated logic.py
    so they can be called using 'Library  TinyMagic' in Robot Framework.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'