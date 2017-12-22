#
# spec file for package sslsplit
#
# Copyright (c) 2017 Marcin Morawski <marcin@morawskim.pl>.
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

Name:           sslsplit
Version:        0.5.0
Release:        1
License:        BSD
Summary:        Transparent and scalable SSL/TLS interception
Url:            http://www.roe.ch/SSLsplit
Group:          Applications/System
Source:         http://mirror.roe.ch/rel/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  libevent-devel, openssl-devel, check-devel
Requires:       iptables
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SSLsplit is a tool for man-in-the-middle attacks against SSL/TLS encrypted
network connections. Connections are transparently intercepted through a
network address translation engine and redirected to SSLsplit. SSLsplit
terminates SSL/TLS and initiates a new SSL/TLS connection to the original
destination address, while logging all data transmitted. SSLsplit is
intended to be useful for network forensics and penetration testing.

It uses Linux netfilter REDIRECT and TPROXY

%prep
%setup -q

%build
# work around some odd build system option passing
export CFLAGS="%{optflags}"
export DEBUG_CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/
cp -a %{name} %{buildroot}%{_bindir}
cp -a %{name}.1  %{buildroot}%{_mandir}/man1/

%post

%postun

%files
%defattr(-,root,root)
%doc *.md
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/*/*

