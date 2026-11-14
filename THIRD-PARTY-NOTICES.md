# Third-Party Notices

ZafBot is an independent project. It uses third-party open-source packages listed below. Each package remains the property of its respective authors and is distributed under its own license.

This notice records the direct and transitive Python dependencies identified during the maintainer's review on November 13, 2026. Versions shown are the versions reported by the maintainer's Python environment during that review. A build made in another environment can contain different versions or additional bundled components.

The accompanying `THIRD-PARTY-LICENSES/` directory (or `THIRD-PARTY-LICENSES.zip`) is intended to contain the original license, copyright, AUTHORS, COPYING and NOTICE files collected from the exact Python environment used for the build, plus standard license texts. Run `collect_zafbot_licenses.py` in the build environment to generate it. Review `THIRD-PARTY-LICENSES/COLLECTION-REPORT.txt` before distributing a binary.

## Direct Dependencies

| Package | Version reviewed | License declaration | Project |
|---|---:|---|---|
| BeautifulSoup4 | 4.15.0 | MIT | https://pypi.org/project/beautifulsoup4/ |
| CustomTkinter | 6.0.0 | Conflicting declarations: package metadata says CC0-1.0; upstream LICENSE says MIT | https://pypi.org/project/customtkinter/6.0.0/ |
| InquirerPy | 0.3.4 | MIT | https://pypi.org/project/InquirerPy/ |
| Rich | 15.0.0 | MIT | https://pypi.org/project/rich/ |
| Selenium | 4.52.0 | Apache-2.0 | https://pypi.org/project/selenium/ |
| Requests | 2.33.1 | Apache-2.0 | https://pypi.org/project/requests/ |

## Transitive Dependencies

| Package | Version reviewed | License |
|---|---:|---|
| soupsieve | 2.8.3 | MIT |
| typing_extensions | 4.16.0 | PSF-2.0 |
| darkdetect | 0.8.0 | BSD-3-Clause |
| packaging | 25.0 | Apache-2.0 OR BSD-2-Clause |
| pfzy | 0.3.4 | MIT |
| prompt-toolkit | 3.0.53 | BSD-3-Clause |
| wcwidth | 0.9.4 | MIT |
| markdown-it-py | 4.2.0 | MIT |
| mdurl | 0.1.2 | MIT |
| Pygments | 2.21.0 | BSD-2-Clause |
| charset-normalizer | 3.4.4 | MIT |
| idna | 3.18 | BSD-3-Clause |
| urllib3 | 2.8.0 | MIT |
| certifi | 2026.10.23 | MPL-2.0 |
| trio | 0.34.0 | MIT OR Apache-2.0 |
| trio-websocket | 0.12.2 | MIT |
| attrs | 26.1.0 | MIT |
| outcome | 1.3.0.post0 | MIT OR Apache-2.0 |
| sniffio | 1.3.1 | MIT OR Apache-2.0 |
| sortedcontainers | 2.4.0 | Apache-2.0 |
| wsproto | 1.3.2 | MIT |
| h11 | 0.16.0 | MIT |
| websocket-client | 1.9.2 | Apache-2.0 |

## Package-Specific Notices

- **CustomTkinter 6.0.0:** The published package metadata is inconsistent: PyPI displays “MIT License (Creative Commons Zero v1.0 Universal),” its `setup.cfg` declares CC0-1.0 while also listing the MIT classifier, and the upstream `LICENSE` file contains an MIT notice. Preserve the exact `LICENSE` file from the installed distribution and include both MIT and CC0-1.0 standard license texts in the accompanying license directory. Do not describe this conflict as resolved.
- **BeautifulSoup4:** Preserve its complete `COPYING.txt`, including the notice about incorporated html5lib code.
- **Requests:** Preserve its `LICENSE` and applicable notices under `ext/` if those files are included in the distribution.
- **Selenium:** Preserve both its `LICENSE` and `NOTICE` files.
- **Pygments:** Preserve its `LICENSE` and `AUTHORS` attribution file when present.
- **wcwidth:** Its license file includes a separate permission notice from Markus Kuhn; preserve the complete file.
- **mdurl:** Its license file includes additional copyright and permission text for the Node.js URL implementation by Joyent, Inc. and other Node contributors; preserve the complete file.
- **packaging:** Its project offers Apache-2.0 OR BSD-2-Clause. Either option may be used; preserve the applicable original license file(s) from the distribution.
- **trio, outcome and sniffio:** Each offers MIT OR Apache-2.0. Preserve the license file(s) from the exact distribution.

## MPL-2.0 Source Availability: certifi

The reviewed dependency set includes certifi 2026.10.23, licensed under MPL-2.0. The corresponding source distribution should accompany the executable distribution or be made available through a clearly identified, durable source link. The license-collection script attempts to download the exact installed Certifi source distribution from PyPI into `THIRD-PARTY-LICENSES/SOURCE-CODE/`.

Official project and source distribution: https://pypi.org/project/certifi/2026.10.23/#files
MPL-2.0 text: https://www.mozilla.org/en-US/MPL/2.0/

If the build uses a different Certifi version, use the corresponding source distribution for that version instead.

## Build Tool: PyInstaller

PyInstaller is a build-time tool, not a ZafBot runtime dependency. Its bootloader exception permits distribution of generated executables without imposing PyInstaller's GPL terms on the generated application, provided the licenses of bundled dependencies are respected. See the official terms: https://pyinstaller.org/en/stable/license.html

## Scope and Disclaimer

This list reflects the reviewed Python dependency set, not a forensic inventory of every file in each PyInstaller archive. PyInstaller can bundle the Python interpreter, standard-library components and platform-specific runtime files. The license-collection script records the environment from which it is run; use it with the same Python environment and dependency versions used for the corresponding build.

ZafBot is not affiliated with, endorsed by, or sponsored by the authors or maintainers of the third-party projects listed above. This notice is an attribution and license index, not legal advice.
