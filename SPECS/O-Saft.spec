#
# spec file for package O-Saft
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

%global perl_vendorlib /usr/lib/perl5/vendor_perl/5.18.2

Name:           O-Saft
Version:        17.06.17
Release:        2
License:        GPL-2
Summary:        O-Saft - OWASP SSL advanced forensic tool
Url:            https://github.com/OWASP/O-Saft
Group:          Productivity/Networking/Security
Source:         https://github.com/OWASP/O-Saft/archive/17.06.17.tar.gz
Requires:       perl-Net-SSLeay >= 1.51
Requires:       perl-IO-Socket-SSL >= 1.37
Requires:       perl-IO-Socket-INET6 >= 1.31
Requires:       perl-Net-DNS >= 0.65
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This tools lists  information about remote target's  SSL  certificate and tests
the remote target according given list of ciphers.

UNIQUE FEATURES
* working in closed environments, i.e. without internet connection
* checking availability of ciphers independent of installed library
* checking for all possible ciphers (up to 65535 per SSL protocol)
* needs just perl without modules for checking ciphers and protocols
* mainly same results on all platforms


Why a new tool for checking SSL  when there already exist a dozens or more good
tools in 2012? Some (but not all) reasons are:
* lack of tests of unusual ciphers
* different results returned for the same check on same target
* missing functionality (checks) according modern SSL/TLS
* lack of tests of unusual (SSL, certificate) configurations
* (mainly) missing feasability to add own tests

%prep
%setup -q

%build

%install
install -m 0755 -d %{buildroot}/%{_bindir}
install -m 0755 -d %{buildroot}/%{perl_vendorlib}/%{name}
./INSTALL.sh     %{buildroot}/%{perl_vendorlib}/%{name} --force

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGES README LICENSE.md docs/
%dir %{perl_vendorlib}/%{name}
%{perl_vendorlib}/%{name}/*
%{perl_vendorlib}/%{name}/.o-saft.pl
%{perl_vendorlib}/%{name}/.o-saft.tcl

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 17.06.17-2
- Rebuild for openSUSE 42.3

* Sat Jul 15 2017 Marcin Morawski <marcin@morawskim.pl>
-  fix build error

* Mon Jul 10 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
