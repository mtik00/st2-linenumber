#!/usr/bin/env python2.7
__author__ = "Timothy McFadden"
__date__ = "08/27/2014"
__copyright__ = "Timothy McFadden, 2014"
__license__ = "GPLv2"
__version__ = "0.01"

'''Sublime Text 2 plugin for inserting the line numbers of a text document or a selection within it '''
import sublime
import sublime_plugin


class ReplaceWithLineNumberCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selected_regions = self.view.sel()
        for region in selected_regions:
            text = str(self.view.rowcol(region.begin())[0] + 1)
            self.view.replace(edit, sublime.Region(region.begin(), region.end()), text)
