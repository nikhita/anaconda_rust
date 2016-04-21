
# Copyright (C) 2016 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import sublime

from .anaconda_plugin import anaconda_helpers


def get_settings(view, name, default=None):
    """Get settings
    """

    if view is None:
        return None

    plugin_settings = sublime.load_settings('AnacondaRUST.sublime-settings')
    return view.settings().get(name, plugin_settings.get(name, default))

# reuse anaconda helper functions
active_view = anaconda_helpers.active_view
get_view = anaconda_helpers.get_view


__all__ = ['get_setings', 'active_view', 'get_view']
