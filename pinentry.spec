#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6 (dshaw@jabberwocky.com)
#
Name     : pinentry
Version  : 1.0.0
Release  : 15
URL      : ftp://ftp.gnupg.org/gcrypt/pinentry/pinentry-1.0.0.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/pinentry/pinentry-1.0.0.tar.bz2
Source99 : ftp://ftp.gnupg.org/gcrypt/pinentry/pinentry-1.0.0.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pinentry-bin
Requires: pinentry-doc
BuildRequires : gtk+-dev
BuildRequires : gtk3-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : ncurses-dev

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
%setup -q -n pinentry-1.0.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491515495
%configure --disable-static --disable-pinentry-qt4 --disable-pinentry-qt4-clipboard
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1491515495
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/pinentry-gtk-2
/usr/bin/pinentry
/usr/bin/pinentry-curses

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files extras
%defattr(-,root,root,-)
/usr/bin/pinentry-gtk-2
