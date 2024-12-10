# utils.py
import threading

# Create a thread-local storage object
_thread_locals = threading.local()

def set_current_project_name(project_name):
    """Set the current project name in thread-local storage."""
    _thread_locals.project_name = project_name

def get_current_project_name():
    """Get the current project name from thread-local storage."""
    return getattr(_thread_locals, 'project_name', None)
