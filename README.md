## About

qrgen.py encodes text to a QR code image.

Currently supported formats: svg, png.

Generated QR code has L ECC level. User iput considered to be
alphanumeric.

Theoreticaly alphanumeric text with L error correction level is
limited by 4296 characters. But empirically qrcode library seems to
push the limit down to 2330 characters.

Although qrgen.py is just a couple dozens lines of code and was
written as a part of a larger project for a publishing house, it could
be useful for automation QR codes generation tasks.

## Requirements

0. Python 3
1. [qrcode package](https://pypi.python.org/pypi/qrcode)

## Usage

    Usage: `qrgen.py "Your text" [output format] [output filename]`,
           where [output format] is an image file format,
                 [output filename] is a filename of the output image.

When format and filename are omitted "QR.svg" is generated.

Examples:

       `qrgen.py "qrgen is useful" svg qrgenad.svg`
	   `qrgen.py "qrgen is useful" svg qrgenad`

Both examples end up with _qrgenad.svg_ being generated in the current directory.

## License

See COPYING.

## Contact

Author: Vitaly R. Samigullin  
Email: vrs {at} pilosus {period} org

## TODO

0. Support for PDF, PostScript formats (take a look at CairoSVG or
   svglib for svg to pdf conversion)
1. Different input types (binary, alphanumberic, etc)
2. Different ECC Levels M, Q, H (see [wiki](https://en.wikipedia.org/wiki/QR_code))
