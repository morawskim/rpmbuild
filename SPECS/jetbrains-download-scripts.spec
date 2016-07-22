#
# spec file for package jetbrains-download-scripts
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>
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

%global commit0 4d4b96a0d1c78fd2b79aa689010ae78aa833c7f2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           jetbrains-download-scripts
Version:        20160722
Release:        1
License:        GPL
Summary:        scripts to download and install Jetbrains IDE
Url:            https://github.com/morawskim/opensuse-configuration-scripts
Source:         https://github.com/morawskim/opensuse-configuration-scripts/archive/%{shortcommit0}.tar.gz
Requires:       wget
Requires:       tar
Requires:       coreutils
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
scripts to download and install Jetbrains IDE.

%prep
%setup  -qn opensuse-configuration-scripts-%{commit0}

%build
exit 0

%install
##%{__mkdir} -p %{buildroot}%{_sbindir}

%{__install} -D -p -m 0750 jetbrains/clion.sh %{buildroot}%{_sbindir}/install-clion
%{__install} -D -p -m 0750 jetbrains/phpstorm.sh %{buildroot}%{_sbindir}/install-phpstorm
%{__install} -D -p -m 0750 jetbrains/rubymine.sh %{buildroot}%{_sbindir}/install-rubymine
%{__install} -D -p -m 0750 jetbrains/datagrip.sh %{buildroot}%{_sbindir}/install-datagrip

%post
exit 0

%postun
exit 0

%files
%defattr(0750,root,root)
%{_sbindir}/install-clion
%{_sbindir}/install-phpstorm
%{_sbindir}/install-rubymine
%{_sbindir}/install-datagrip

%changelog
* Fri Jul 22 2016 Marcin Morawski <marcin@morawskim.pl>
-  update to 4d4b96a0d1c78fd2b79aa689010ae78aa833c7f2

* Wed Jul 13 2016 Marcin Morawski <marcin@morawskim.pl>
-  update to a64843be48b61b81fbea1d307033b0e66172fdcc

* Sat Jun 25 2016 Marcin Morawski <marcin@morawskim.pl>
-  update to d361cc9deb81995b67d118f168c48a818aebd9ca
-  add script to install datagrip
