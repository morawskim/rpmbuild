#
# spec file for package testssl.sh
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

Name:           testssl.sh
Version:        2.8
Release:        1
License:        GPLv2
Summary:        Testing TLS/SSL encryption anywhere on any port
Url:            https://testssl.sh/
Group:          Productivity/Networking/Security
Source:         https://github.com/drwetter/testssl.sh/archive/v%{version}.tar.gz
Provides:       checkcert.sh
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
testssl.sh is a free command line tool which checks a server's service on any
port for the support of TLS/SSL ciphers, protocols as well as some
cryptographic flaws.

Key features
* Clear output: you can tell easily whether anything is good or bad
* Ease of installation: It works for Linux, Darwin, FreeBSD, NetBSD and
* MSYS2/Cygwin out of the box: no need to install or configure something, no
 gems, CPAN, pip or the like.
* Flexibility: You can test any SSL/TLS enabled and STARTTLS service, not only
 webservers at port 443
* Toolbox: Several command line options help you to run YOUR test and configure
 YOUR output
* Reliability: features are tested thoroughly
* Verbosity: If a particular check cannot be performed because of a missing
 capability on your client side, you'll get a warning
* Privacy: It's only you who sees the result, not a third party
* Freedom: It's 100% open source. You can look at the code, see what's going on
 and you can change it.
* Heck, even the development is open (github)

%prep
%setup -q

%build

%install
%{__install} -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}
%{__install} -Dp -m 755 utils/checkcert.sh %{buildroot}%{_bindir}/checkcert.sh

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG.stable-releases.txt Readme.md CREDITS.md LICENSE
%{_bindir}/%{name}
%{_bindir}/checkcert.sh

%changelog
* Sun Jul 23 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release

