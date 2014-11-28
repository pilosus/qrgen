#!/usr/bin/env python3

"""Copyright 2014 Vitaly R. Samigullin

This file is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

Foobar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import qrcode # see: https://pypi.python.org/pypi/qrcode
import qrcode.image.svg
import re

def qrgen(text, file_format, file_name):
    """Encode given text to a QR code image."""
    if len(text) > 2330:
        raise ValueError("Text input should not exceed 2330 characters.")

    ff = file_format.lower()
    if ff.startswith('p'):
        extension = 'png'
        img = qrcode.make(text)
    elif ff.startswith('s'):
        extension = 'svg'
        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(text, image_factory=factory)
    else:
        raise ValueError("{0} file format not currently supported.".format(file_format))

    r = re.search("\.{0}$".format(extension), file_name)
    if not r:
        file_name += '.' + extension
            
    try:
        img.save(file_name)
    except FileNotFoundError as error:
        sys.exit(error)

def usage():
    print(
        'usage: qrgen.py "Your text" [output format] [output filename],\n'
        'where [output format] is an image file format,\n' 
        '      [output filename] is a filename of the output image.\n'
        'When format and filename are omitted "QR.svg" is generated.\n'
        'Currently supported formats: png, svg.\n'
        'Example: qrgen.py "qrgen is useful" svg qrgenad.svg'
    )

if __name__ == '__main__':
    args = sys.argv[1:]
    if (len(args) < 1):
        usage()
    elif (len(args) < 2):
        qrgen(args[0], 'svg', 'QR.svg')
    else:
        qrgen(args[0], args[1], args[2])
