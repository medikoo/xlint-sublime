# xlint-sublime
## [XLint](https://github.com/medikoo/xlint) build system for Sublime Text2

__It's modified version of [Sublime-JSLint](https://github.com/darrenderidder/Sublime-JSLint)__

### Prerequisites

NodeJS must be installed on your system and you must be able to run 'node' from the command line.

### Installation

In your console go to Packages folder of Sublime Text:
* Linux: _~/.config/sublime-text-2/Packages_
* Mac: _~/Library/Application Support/Sublime Text 2/Packages_
* Windows: _%APPDATA%/Sublime Text 2/Packages_ or if it's not there, then try _%APPDATA%/Roaming/Sublime Text 2/Packages_

Clone this project into _XLint_ folder

	$ git clone https://github.com/medikoo/xlint-sublime.git XLint

Install its dependencies:

	$ cd XLint
	$ npm install

Restart Sublime Text

Usage
-----
Any of the following will work:
   * Select 'XLint' under Tools > Build System and run Build.
   * Select Tools > XLint
   * Press ctrl-L
   * Just save a .js file

