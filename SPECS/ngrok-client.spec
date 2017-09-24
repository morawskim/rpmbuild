#
# spec file for package ngrok-client
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

Name:           ngrok-client
Version:        2.2.8
Release:        1
License:        Commercial
Summary:        Secure tunnels to localhost
Url:            https://ngrok.com
Group:          Productivity/Networking/Other
Source:         https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
Provides:       ngrok
BuildArch:      x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ngrok creates a tunnel from the public internet to a port on your local
machine. You can give this URL to anyone to allow them to try out a web site
you're developing without doing any deployment.

It captures all traffic through the tunnel. It displays information
about the HTTP traffic for your inspection. Raw request/response bytes, parsed
headers and form data, JSON/XML syntax checking and more are included. It can
also replay requests.

By default, ngrok will use ngrok.com as a third-party relay. This
service is provided at no-cost and without registration but it is possible to
get additional features by signing up in the service (which is pay-as-you-want
kind). However, it is possible to setup and use its own server.

This package installs the client part of ngrok. It can be used
directly with ngrok.com service or with your own server if you install the
ngrok-server package.

%prep
%setup -qc

%build

%install
%__install -D -p -m 0755 ngrok %{buildroot}%{_bindir}/ngrok

%post

%postun

%files
%defattr(-,root,root)
%{_bindir}/ngrok

%changelog
* Sun Sep 24 2017 Marcin Morawski <marcin@morawskim.pl>
-  Update to 2.2.8

* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 2.1.18-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Wed Dec 21 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release

