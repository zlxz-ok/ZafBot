Third-Party Notices
ZafBot is an independent project. It uses third-party open-source packages listed below. Each package remains the property of its respective authors and is distributed under its own license.

This notice is intended to accompany ZafBot source and binary distributions. It identifies the Python packages and versions reported in the maintainer's dependency review on November 13, 2026. It is an inventory based on the installed package metadata and dependency information reviewed for ZafBot; it is not a verified software bill of materials (SBOM) for each PyInstaller archive. The contents of each final Linux and Windows build should be checked separately because build environments and bundled runtime components can differ.

The links below point to the upstream projects and their license or notice files. For binary redistribution, include the applicable original license texts and copyright/NOTICE files in the distribution as described in the relevant license. A link in this index does not replace a license text or notice that must be reproduced with a binary distribution.
Direct Dependencies
Package Version reviewed License Upstream license / notice
BeautifulSoup4 4.15.0 MIT COPYING.txt
CustomTkinter 6.0.0 CC0-1.0 in package metadata; MIT in upstream LICENSE (conflicting declarations) PyPI metadata, upstream LICENSE, upstream setup.cfg
InquirerPy 0.3.4 MIT LICENSE
Rich 15.0.0 MIT LICENSE
Selenium 4.52.0 Apache-2.0 LICENSE, NOTICE
Requests 2.33.1 Apache-2.0 LICENSE, additional extension notices

Transitive Dependencies
The following packages were identified in the reviewed dependency tree. Their presence in a particular executable still depends on that build's environment and PyInstaller collection.
Package Version reviewed License Upstream license / notice
soupsieve 2.8.3 MIT Soupsieve repository
typing_extensions 4.16.0 PSF-2.0 LICENSE
darkdetect 0.8.0 BSD-3-Clause Darkdetect repository
packaging 25.0 Apache-2.0 OR BSD-2-Clause Packaging repository and license files
pfzy 0.3.4 MIT pfzy repository
prompt-toolkit 3.0.53 BSD-3-Clause LICENSE
wcwidth 0.9.4 MIT LICENSE
markdown-it-py 4.2.0 MIT LICENSE
mdurl 0.1.2 MIT LICENSE
Pygments 2.21.0 BSD-2-Clause LICENSE, AUTHORS
charset-normalizer 3.4.4 MIT LICENSE
idna 3.18 BSD-3-Clause idna repository
urllib3 2.8.0 MIT LICENSE
certifi 2026.10.23 MPL-2.0 LICENSE, source distribution for version 2026.10.23
trio 0.34.0 MIT OR Apache-2.0 Trio repository
trio-websocket 0.12.2 MIT trio-websocket repository
attrs 26.1.0 MIT attrs repository
outcome 1.3.0.post0 MIT OR Apache-2.0 outcome repository
sniffio 1.3.1 MIT OR Apache-2.0 sniffio repository
sortedcontainers 2.4.0 Apache-2.0 sortedcontainers repository
wsproto 1.3.2 MIT wsproto repository
h11 0.16.0 MIT h11 repository
websocket-client 1.9.2 Apache-2.0 websocket-client repository

Additional Copyright and Attribution Notices
The following package-specific notices must be retained when the corresponding package is included in a distribution:

- BeautifulSoup4: its license file identifies Leonard Richardson and also identifies incorporated html5lib code. Preserve the complete upstream COPYING.txt.
- CustomTkinter: its PyPI metadata and upstream setup.cfg identify CC0-1.0, while the upstream LICENSE file currently contains an MIT notice for Tom Schimansky. Preserve the license file supplied with the exact CustomTkinter 6.0.0 distribution and do not silently replace one declaration with the other.
- Requests: preserve the main license and any applicable notices in its ext directory.
- Selenium: preserve both LICENSE and NOTICE.
- Pygments: preserve its license and applicable author attribution information.
- wcwidth: its license file also contains a separate permission notice from Markus Kuhn. Preserve the complete file, not only the MIT portion.
- mdurl: its license file contains additional copyright and permission text for code based on the Node.js URL implementation by Joyent, Inc. and other Node contributors. Preserve the complete file.
  MPL-2.0 Source Availability: certifi
  ZafBot's reviewed dependency set includes certifi 2026.10.23, which is licensed under MPL-2.0. When this component is included in a binary distribution, recipients must be told how to obtain its corresponding source code. The source distribution for the exact reviewed version is available from:
- https://pypi.org/project/certifi/2026.10.23/#files
  The MPL-2.0 license is available at:
- https://www.mozilla.org/en-US/MPL/2.0/
  No modifications to certifi are represented by this notice. If ZafBot's build uses a different certifi version, update the version and source link to match that build.
  Build Tool: PyInstaller
  PyInstaller is used as a build-time packaging tool, not listed as a ZafBot runtime dependency. PyInstaller's official licensing documentation states that its bootloader exception permits distribution of generated executables without including PyInstaller's license or crediting PyInstaller, provided the licenses of the application's dependencies are respected:
- https://www.pyinstaller.org/en/stable/license.html
  If PyInstaller itself is modified and that modified tool is redistributed, its own license requirements must be reviewed separately.
  Build-Specific Components Not Covered by This Package Inventory
  PyInstaller can also bundle the Python interpreter, parts of the Python standard library, and platform/runtime components. The exact Python version and any bundled Tcl/Tk or other runtime files can differ between Linux and Windows builds. Their applicable license and notice files must be checked against the actual build output before claiming that this inventory is a complete list of everything inside a release archive.
  Project Independence
  ZafBot is not affiliated with, endorsed by, or sponsored by the authors or maintainers of the third-party projects listed above. Product and project names are used only to identify the software components.

This document is a third-party component and license index, not legal advice. It should be reviewed whenever dependency versions or build environments change.
