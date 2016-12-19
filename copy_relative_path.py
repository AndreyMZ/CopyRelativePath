import sublime, sublime_plugin
import os
from os.path import commonprefix, relpath

class CopyRelativePathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if len(filename) > 0:
            # The shortest relpath for file compared to open folders
            rel_path = min((relpath(filename, folder) for folder in sublime.active_window().folders()), key=len)
            
            if os.sep != '/':
                rel_path = rel_path.replace(os.sep, '/')
            
            sublime.set_clipboard(rel_path)
            sublime.status_message("Copied relative path")

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)
