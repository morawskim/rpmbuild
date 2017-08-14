#
# spec file for package password-store-import
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

%define commit  491935bd275f29ceac2b876b3a288011d1ce31e7

Name:           password-store-import
Version:        20170406
Release:        2
License:        GPL-3.0
Summary:        Password Store Import Extension
Url:            https://github.com/roddhjav/pass-import
Group:          Productivity/Security
Source:         https://github.com/roddhjav/pass-import/archive/%{commit}.tar.gz
Requires:       password-store >= 1.7
Requires:       ruby
Requires:       rubygem(json)
Requires:       rubygem(nokogiri)
Requires:       perl(warnings)
Requires:       perl(strict)
Requires:       perl(XML::Simple)
Requires:       perl(Getopt::Long)
Requires:       perl(Pod::Usage)
Requires:       python-base
Requires:       python-xml
Requires:       python3-base
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A generic importer extension for the standard unix password manager pass.

%prep
%setup -q -n pass-import-%{commit}

%build

%install
make install DESTDIR=%{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
%dir %{_libexecdir}/password-store
%dir %{_libexecdir}/password-store/extensions
%{_libexecdir}/password-store/extensions/import.bash
%{_libexecdir}/password-store/importers
%{_mandir}/man1/pass-import.1.gz

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 20170406-2
- Rebuild for openSUSE 42.3

* Wed Aug 02 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
