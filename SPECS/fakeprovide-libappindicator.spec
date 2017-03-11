#
# spec file for package fakeprovide-libappindicator
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

Name:          fakeprovide-libappindicator
Version:       20160909205128
Release:       1
Summary:       libappindicator fakeprovide for slack
Group:         Fake
License:       GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Source:        %{name}.README
Provides:      libappindicator
Requires:      libappindicator3-1
BuildArch:     x86_64

%description
%{summary}

%prep
%setup -c -T

%build
cp %{SOURCE0} .


%install

%files
%defattr(-,root,root,-)
%doc %{name}.README

%changelog
* Sat Mar 11 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release

