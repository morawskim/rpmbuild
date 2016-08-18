#
# spec file for package smtp-cli
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

Name:           smtp-cli
Version:        3.7
Release:        1
License:        GPLv3
Summary:        Command line SMTP client with SSL, STARTTLS, SMTP-AUTH and IPv6 support
Url:            http://smtp-cli.logix.cz
Group:          Productivity/Networking/Email/Utilities
Source:         https://github.com/mludvig/smtp-cli/archive/v%{version}.tar.gz
Requires:       perl-IO-Socket-SSL
Requires:       perl-Digest-HMAC
Requires:       perl-MIME-Lite
Requires:       perl-IO-Socket-INET6
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
smtp-cli is a powerful SMTP command line client with a support for advanced
features, such as STARTTLS, SMTP-AUTH, or IPv6 and with a scriptable message
composition capabilities supporting anything from simple plain-text messages
right up to building complex HTML emails with alternative plain-text part,
attachments and inline images. The MIME-Type of the attachments can either be
guessed automatically or alternatively set on the command line, separately for
each attachment if required.

It's also a convenient tool for testing and debugging SMTP servers' setups. Even
the hardcore mail admins used to typing the SMTP protocol over telnet need a
specialised tool when it comes to verifying encryption settings of their TLS
enabled server with a subsequent user authentication. Such things are pretty
hard to type into a telnet session by hand :-)

%prep
%setup -q -n %{name}-%{version}
cat > Examples.md <<EOF
Test on your localhost:
\`smtp-cli --verbose --host=localhost\`

Send an e-mail through a host which requires authentication after an encryption
takes place:
\`smtp-cli --verbose --host=relayhost.domain.top --enable-auth --user test \
--from test@domain.com --to user@another.domain.org --data message-body.txt\`
EOF

%build

%install
%__install -D -p -m 0755 smtp-cli %{buildroot}%{_bindir}/smtp-cli

%post

%postun

%files
%defattr(-,root,root)
%doc Examples.md
%attr(0755, root, root) %{_bindir}/smtp-cli

%changelog
* Thu Aug 18 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release

