#
# spec file for package swaks
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           swaks
Version:        20130209.0
Release:        3
License:        GPLv2+
Summary:        Command-line SMTP transaction tester
Url:            http://www.jetmore.org/john/code/swaks
Group:          Applications/Internet
Source:         http://www.jetmore.org/john/code/swaks/swaks-%{version}.tar.gz
Patch0:         swaks-20130209.0-POD-item-text-cannot-be-a-literal-number.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       perl(Digest::SHA)
Requires:       perl(Net::DNS)
Requires:       perl(Net::SSLeay)
Requires:       perl(Time::HiRes)
Requires:       perl(Authen::SASL)
Requires:       perl(IO::Socket::INET6)

%description
Swiss Army Knife SMTP: A command line SMTP tester.  Swaks can test
various aspects of your SMTP server, including TLS and AUTH.

%prep
%setup -q
%patch0 -p1

%build
exit 0

%install
install -D -p -m 0755 swaks %{buildroot}%{_bindir}/swaks
mkdir -p %{buildroot}%{_mandir}/man1
/usr/bin/pod2man swaks > %{buildroot}%{_mandir}/man1/swaks.1

%post

%postun

%files
%defattr(-,root,root,-)
%{_bindir}/swaks
%{_mandir}/man1/*
%doc LICENSE README doc/Changes.txt doc/recipes.txt doc/ref.txt

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 20130209.0-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Feb 27 2016 Marcin Morawski  <marcin@morawskim.pl>
- Initial attempt

