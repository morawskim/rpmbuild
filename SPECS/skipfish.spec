#
# spec file for package skipfish
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

Name:           skipfish
Version:        2.10
Release:        0.4.b
#Whole package licensed with ASL 2.0 license except
#string-inl.h which has BSD type license
#icons which are licensed under LGPLv3
License:        ASL 2.0 and BSD and LGPLv3
Summary:        Web application security scanner
Url:            http://code.google.com/p/skipfish/
Group:          Applications/Internet
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/%{name}/%{name}-%{version}b.tgz
Patch1:         %{name}-makefile.patch
BuildRequires:  pkgconfig(openssl) < 1.1.0
BuildRequires:  libidn-devel
BuildRequires:  zlib-devel
BuildRequires:  pcre-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q -n %{name}-%{version}b
%patch1 -p1
cp -p assets/COPYING COPYING.icons

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_datadir}/%{name}/assets/COPYING
rm -f doc/skipfish.1

%post

%postun

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README
%doc doc/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/assets
%dir %{_datadir}/%{name}/dictionaries
%dir %{_datadir}/%{name}/signatures
%{_datadir}/%{name}/dictionaries/*
%{_datadir}/%{name}/signatures/*
%{_datadir}/%{name}/assets/index.html
%{_bindir}/%{name}
%{_bindir}/sfscandiff
%{_mandir}/man1/%{name}.1*

#Icons are licensed as LGPLv3 http://www.everaldo.com/crystal/
%doc COPYING.icons
%{_datadir}/%{name}/assets/*.png

%changelog
* Sat Jul 21 2018 Marcin Morawski <marcin@morawskim.pl>
-  Skipfix requires libopenssl-devel below 1.1.0

* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 2.10-0.4.b
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Apr 15 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
