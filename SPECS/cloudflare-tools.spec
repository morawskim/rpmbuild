#
# spec file for package cloudflare-tools
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

%global commit0 8bea6e24bae7966ec9214c708110aa496d699396
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           cloudflare-tools
Version:        20171023
Release:        1
License:        BSD
Summary:        Cloudflare Blog code samples
Url:            https://github.com/cloudflare/cloudflare-blog
Group:          Applications/Productivity
Source:         https://github.com/cloudflare/cloudflare-blog/archive/%{shortcommit0}.tar.gz
Provides:       mmhistogram
Provides:       mmsum
Provides:       mmwatch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cloudflare Blog code samples

%prep
%setup -qn cloudflare-blog-%{commit0}

%build

%install
%{__install} -Dp -m 755 2017-06-29-ssdp/mmhistogram %{buildroot}%{_bindir}/mmhistogram
%{__install} -Dp -m 755 2017-06-29-ssdp/mmsum %{buildroot}%{_bindir}/mmsum
%{__install} -Dp -m 755 2017-06-29-ssdp/mmwatch %{buildroot}%{_bindir}/mmwatch

%post

%postun

%files
%defattr(-,root,root)
%doc 2017-06-29-ssdp/README.md
%_bindir/mmhistogram
%_bindir/mmsum
%_bindir/mmwatch

%changelog
* Wed Nov 01 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release

