#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6 (dshaw@jabberwocky.com)
#
Name     : pinentry
Version  : 1.1.0
Release  : 20
URL      : ftp://ftp.gnupg.org/gcrypt/pinentry/pinentry-1.1.0.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/pinentry/pinentry-1.1.0.tar.bz2
Source99 : ftp://ftp.gnupg.org/gcrypt/pinentry/pinentry-1.1.0.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pinentry-bin
Requires: pinentry-doc
BuildRequires : gcr-dev
BuildRequires : gtk3-dev
BuildRequires : libassuan-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libgpg-error-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(gcr-3)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libsecret-1)
Patch1: 0001-add-pinentry-wrapper.patch

%description
PINEntry
---------
This is a collection of PIN or passphrase entry dialogs which
utilize the Assuan protocol as specified in the Libassuan manual.

%package bin
Summary: bin components for the pinentry package.
Group: Binaries

%description bin
bin components for the pinentry package.


%package doc
Summary: doc components for the pinentry package.
Group: Documentation

%description doc
doc components for the pinentry package.


%package extras
Summary: extras components for the pinentry package.
Group: Default

%description extras
extras components for the pinentry package.


%prep
%setup -q -n pinentry-1.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517803131
%configure --disable-static --disable-pinentry-gtk2 --disable-pinentry-qt5 --enable-pinentry-gnome3 --enable-pinentry-curses
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1517803131
rm -rf %{buildroot}
%make_install
## make_install_append content
install -m 0755 pinentry-wrapper %{buildroot}/usr/bin/pinentry
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/pinentry-gnome3
/usr/bin/pinentry
/usr/bin/pinentry-curses

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files extras
%defattr(-,root,root,-)
/usr/bin/pinentry-gnome3
