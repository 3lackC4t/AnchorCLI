# Maintainer: Cameron Minty <C.S.Minty@proton.me>

pkgname="AnchorCLI"
pkgver="0.0.2"
pkgrel="1"
pkgdesc="Easily execute shell commands with the use of user defined directory aliases"
arch=("any")
source="https://github.com/3lackC4t/AnchorCLI-${pkgver}.tar.gz"
license=('GPL-3.0 License')
depends=('python', 'python-pyyaml')
sha512sums=('SKIP')

build() {
	cd $pkgname
	python setup.py build
}

package() {
	cd "$srcdir/AnchorCLI-$pkgver"
	python setup.py install --root="$pkgdir/" --optimize=1	
}



