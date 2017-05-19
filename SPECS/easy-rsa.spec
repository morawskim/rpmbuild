#
# spec file for package easy-rsa
#
# Copyright (c) 2016 Marcin Morawski
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           easy-rsa
Version:        3.0.1
Release:        2
License:        GPL-2
Summary:        CLI utility to build and manage a PKI CA
Url:            https://github.com/OpenVPN/easy-rsa
Group:          Productivity/Networking/Security
Source:         https://github.com/OpenVPN/easy-rsa/archive/%{version}.zip
Patch0:         easyrsa.packaging.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
easy-rsa is a CLI utility to build and manage a PKI CA. In laymen's terms,
this means to create a root certificate authority, and request and sign 
certificates, including sub-CAs and certificate revokation lists (CRL).

%prep
%setup -q
%patch0 -p0
sed -i 's;#\(set_var EASYRSA    \)"$PWD";\1"/etc/easy-rsa";' easyrsa3/vars.example
mv README.quickstart.md README.quickstart
for f in doc/*.md; do
   mv $f ${f%.md}
done

%build
exit 0

%install
install -dm0700 %{buildroot}/%{_sysconfdir}/easy-rsa/
install -dm0755 %{buildroot}/%{_sysconfdir}/easy-rsa/x509-types
install -Dm0644 easyrsa3/vars.example %{buildroot}/%{_sysconfdir}/easy-rsa/vars
install -Dm0644 easyrsa3/openssl-1.0.cnf %{buildroot}/%{_sysconfdir}/easy-rsa/openssl-1.0.cnf
install -Dm0644 easyrsa3/x509-types/* %{buildroot}/%{_sysconfdir}/easy-rsa/x509-types/
install -Dm0755 easyrsa3/easyrsa %{buildroot}/%{_bindir}/easyrsa

%files
%defattr(-,root,root)
%doc KNOWN_ISSUES README README.quickstart COPYING
%doc doc/*
%{_bindir}/easyrsa
%config(noreplace) %{_sysconfdir}/easy-rsa

