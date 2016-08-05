#
# spec file for package sslscan
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

Name:           sslscan
Version:        1.8.2
Release:        1
License:        SUSE-GPL-3.0+-with-openssl-exception
Summary:        SSL cipher scanning tool
Url:            https://www.titania-security.com/labs/sslscan
Group:          Productivity/Networking/Diagnostic
Source:         http://netassist.dl.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}.tgz
Patch1:         %{name}-01-Makefile-binutils-gold.diff
Patch2:         %{name}-02-sslscan-spelling-mistake.diff
Patch3:         %{name}-03-sslv2.diff
Patch4:         %{name}-fedora-sslscan-patents.patch
Patch5:         %{name}-tlsv1_2-support.diff
BuildRequires:  openssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SSLScan determines what ciphers are supported on SSL-based services,
such as HTTPS. Furthermore, SSLScan will determine the preferred
ciphers of the SSL service.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if %{defined fedora}
%patch4 -p1
%endif
# requires openssl 1.0.1
%if 0%{?suse_version} > 1220
%patch5 -p1
%endif

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
%{__install} -d "%{buildroot}%{_bindir}"
%{__install} -d "%{buildroot}%{_mandir}/man1"
make install BINPATH="%{buildroot}%{_bindir}" MANPATH="%{buildroot}%{_mandir}" 

%post

%postun

%files
%defattr(-,root,root)
%doc Changelog
%{_bindir}/sslscan
%{_mandir}/man1/sslscan.1.gz

%changelog
* Sun Jul 31 2016 Marcin Morawski <marcin@morawskim.pl>
-  initial packaging
