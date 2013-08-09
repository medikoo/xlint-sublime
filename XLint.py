import sublime, sublime_plugin, re

class autoXLint(sublime_plugin.EventListener):
	def on_post_save(self, view):
		settings = sublime.load_settings("XLint.sublime-settings")
		if re.search( settings.get( "filename_filter" ), view.file_name() ):
			view.window().run_command( "build" )

class XlintCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command('set_build_system', {
				'file': 'Packages/XLint/XLint.sublime-build'
				})
		self.window.run_command('build')