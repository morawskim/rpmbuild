#
# spec file for package easy-rsa2
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/morawskim/rpmbuild/issues
#

Name:           easy-rsa2
Version:        2.2.2
Release:        1
License:        GPLv2
Summary:        Simple shell based CA utility
Url:            https://github.com/OpenVPN/easy-rsa
Group:          Productivity/Networking/Security
Source0:        https://github.com/OpenVPN/easy-rsa/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        make-cadir
Source2:        make-cadir.1.gz
Provides:       easy-rsa
Requires:       openssl
Conflicts:      easy-rsa
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
easy-rsa is a CLI utility to build and manage a PKI CA. In laymen's terms,
this means to create a root certificate authority, and request and sign
certificates, including sub-CAs and certificate revokation lists (CRL).

%prep
%setup -qn easy-rsa-%{version}

%build
aclocal
autoconf
automake --add-missing
./configure --prefix=%{_prefix}

%install
make install DESTDIR=%{buildroot}
%{__rm} -r %{buildroot}/usr/share/doc/easy-rsa
install -m 755 -D -p %{SOURCE1} %{buildroot}/%{_bindir}/make-cadir
install -m 644 -D -p %{SOURCE2} %{buildroot}/%{_mandir}/man1/make-cadir.1.gz

%post

%postun

%files
%defattr(-,root,root)
%doc doc/README-2.0 COPYING COPYRIGHT.GPL
%dir %{_datadir}/easy-rsa
%{_datadir}/easy-rsa/*
%{_bindir}/make-cadir
%{_mandir}/man1/make-cadir.1.gz

%changelog
* Wed Nov 30 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
