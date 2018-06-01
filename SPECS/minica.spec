#
# spec file for package minica
#
# Copyright (c) 2018 Marcin Morawski <marcin@morawskim.pl>.
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

%global commit0 3a621c05b61fa1c24bcb42fbde4b261db504a74f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           minica
Version:        20161105.%{shortcommit0}
Release:        1
License:        ?
Summary:        minica is a small, simple CA
Url:            https://github.com/jsha/minica
Group:          Productivity/Networking/Security
Source:         https://github.com/jsha/minica/archive/%{commit0}.tar.gz
BuildRequires:  go
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Minica is a simple CA intended for use in situations where the CA operator also
operates each host where a certificate will be used. It automatically generates
both a key and a certificate when asked to produce a certificate. It does not
offer OCSP or CRL services. Minica is appropriate, for instance, for generating
certificates for RPC systems or microservices.

On first run, minica will generate a keypair and a root certificate in the
current directory, and will reuse that same keypair and root certificate unless
they are deleted.

On each run, minica will generate a new keypair and sign an end-entity (leaf)
certificate for that keypair. The certificate will contain a list of DNS names
and/or IP addresses from the command line flags. The key and certificate are
placed in a new directory whose name is chosen as the first domain name from
the certificate, or the first IP address if no domain names are present. It
will not overwrite existing keys or certificates.

%prep
%setup -qn %{name}-%{commit0}

%build
local_go=$PWD/go
export GOPATH="$local_go:$GOPATH"
mkdir -p $local_go/src/github.com/jsha
ln -s $PWD $local_go/src/github.com/jsha/minica

pushd $local_go/src/github.com/jsha/minica
go build
popd

%install
%{__install} -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/%{name}

%changelog
* Mon Apr 16 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release
