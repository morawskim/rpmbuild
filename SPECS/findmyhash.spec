#
# spec file for package findmyhash
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

%global commit0 aa60beaeba5f5fee337e233a1a90d5e656b5607f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           findmyhash
Version:        20140430
Release:        3
License:        GPLv3
Summary:        Hash cracker
Url:            https://github.com/Talanor/findmyhash
Group:          Productivity/Security
Source0:        https://github.com/Talanor/findmyhash/archive/%{commit0}.tar.gz
Source1:        %{name}.bash_completion
Patch0:         %{name}-add_shebang.patch
Requires:       python-httplib2
Requires:       python-libxml2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
findmyhash try to crack different types of hashes using free online services.

%prep
%setup -q -n %{name}-%{commit0}
%patch0

%build

%install
%{__install} -D -p -m 0755 findmyhash.py %{buildroot}%{_bindir}/%{name}
%{__install} -D -m 0644 %{S:1} %{buildroot}/%{_sysconfdir}/bash_completion.d/%{name}.sh

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/bash_completion.d/%{name}.sh

%changelog
* Wed Aug 30 2017 Marcin Morawski <marcin@morawskim.pl>
-  Add python-libxml2 to Requires
-  Add bash completion

* Tue Aug 29 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
