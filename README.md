# Ribbex (Fork of https://github.com/haiiliin/pyqtribbon)

[![Tests](https://github.com/rompik/ribbex/actions/workflows/tests.yml/badge.svg)](https://github.com/rompik/ribbex/actions/workflows/tests.yml)
[![PyPI](https://github.com/rompik/ribbex/actions/workflows/publish.yml/badge.svg)](https://github.com/rompik/ribbex/actions/workflows/publish.yml)


[![PyPI license](https://img.shields.io/pypi/l/ribbex.svg)](https://github.com/rompik/ribbex/blob/main/LICENSE)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ribbex.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/ribbex)](https://pypi.org/project/ribbex/)
[![PyPI download month](https://img.shields.io/pypi/dm/ribbex.svg)](https://pypi.org/project/ribbex/)

Ribbon Bar for PyQt6 applications.

- GitHub Repository: [github.com/rompik/ribbex](https://github.com/rompik/ribbex/).
- Documentation: [pyqribbon.readthedocs.io/en/stable](https://pyqribbon.readthedocs.io/en/stable/).
- Python Package Index: [pypi.org/project/ribbex](https://pypi.org/project/ribbex/).
- Read the Docs: [readthedocs.org/projects/pyqribbon](https://readthedocs.org/projects/pyqribbon/).

## Installation

Ribbex is distributed to [PyPI](https://pypi.org/project/ribbex/), you can use pip to install it:

```shell
pip install ribbex
```

You can also install the package from source:

```shell
pip install git+https://github.com/rompik/ribbex.git@main
```

## Python and PyQt6 Requirements

- [Python][py] 3.10+ with [PyQt6][PyQt6]

[py]: https://www.python.org/
[PyQt6]: https://pypi.org/project/PyQt6/

## The Ribbon Bar

The ribbon is first introduced by Microsoft in the 2000's. It is a toolbar with a tabbed interface. According to [Microsoft](https://docs.microsoft.com/en-us/cpp/mfc/ribbon-designer-mfc?view=msvc-170):

- A ribbon is a user interface (UI) element that organizes commands into logical groups. These groups appear on separate tabs in a strip across the top of the window. The ribbon replaces the menu bar and toolbars. A ribbon can significantly improve application usability. For more information, see Ribbons. The following illustration shows a ribbon. A ribbon can significantly improve application usability. For more information, see [Ribbons](https://docs.microsoft.com/en-us/windows/win32/uxguide/cmd-ribbons). The following illustration shows a ribbon.

  ![ribbon_no_callouts](docs/source/_images/ribbon_no_callouts.png)

## Definitions of Ribbon Elements

- **Application button**: The button that appears in the upper-left corner of a ribbon. The Application button replaces the File menu and is visible even when the ribbon is minimized. When the button is clicked, a menu that has a list of commands is displayed.

- **Quick Access toolbar**: A small, customizable toolbar that displays frequently used commands.

- **Category**: The logical grouping that represents the contents of a ribbon tab.

- **Category Default button**: The button that appears on the ribbon when the ribbon is minimized. When the button is clicked, the category reappears as a menu.

- **Panel**: An area of the ribbon bar that displays a group of related controls. Every ribbon category contains one or more ribbon panels.

- **Ribbon elements**: Controls in the panels, for example, buttons and combo boxes. To see the various controls that can be hosted on a ribbon, see RibbonGadgets Sample: Ribbon Gadgets Application.

## Screenshots

![An Example](docs/source/_images/main-interface.png)
