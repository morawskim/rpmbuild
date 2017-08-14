#
# spec file for package php71v
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


# _without_ make_test by default
# use build-test.sh for testing!
%bcond_with make_test

# firebird first added in 11.2
%if 0%{suse_version} < 1120
%define _without_firebird 1
%endif

# systemd first added in 12.1
%if 0%{suse_version} < 1210
%define _without_systemd 1
%endif

# firebird disabled due to build errors: https://bugs.php.net/bug.php?id=70071
%bcond_with     firebird
%bcond_without  spell
%bcond_without  systemd

%global apiver            20160303
%global zendver           20160303

%define pkg_name          php7
%define php__doc_version  PHP7.1
%define php_dir_name	  %{name}
%define base_dir          /opt/php/%{php_dir_name}
%define php_datadir       %{base_dir}%{_datadir}/%{pkg_name}
%define extension_dir     %{base_dir}%{_libdir}/%{pkg_name}/extensions
%define peardir           %{php_datadir}/PEAR
%define php_sysconf       %{base_dir}%{_sysconfdir}/%{pkg_name}
%define _x11prefix        %(pkg-config --variable=prefix xft)
%define need_libxml2_hack %(if [ -e %{_includedir}/libxml/parser.h ]; then if grep -q XML_PARSE_OLDSAX %{_includedir}/libxml/parser.h; then echo 1; else echo 0; fi; else echo 0; fi)

Name:           php71v
Version:        7.1.0
Release:        3
Summary:        %{php__doc_version} Core Files
License:        PHP-3.01
Group:          Development/Languages/Other
Url:            http://www.php.net
Source0:        http://us2.php.net/distributions/php-%{version}.tar.xz
Source1:        php7-fpm.service.template

## SUSE specific patches
Patch0:         %{name}-phpize.patch
Patch2:         %{name}-php-config.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  curl
BuildRequires:  curl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  enchant-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  gmp-devel
BuildRequires:  imap-devel
BuildRequires:  krb5-devel
BuildRequires:  libapparmor-devel
BuildRequires:  libbz2-devel
BuildRequires:  libedit-devel
BuildRequires:  libevent-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmcrypt-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libpng-devel
BuildRequires:  libtidy-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libxslt-devel
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  postfix
BuildRequires:  postgresql-devel >= 9.1.0
BuildRequires:  re2c
BuildRequires:  sqlite3-devel
BuildRequires:  tcpd-devel
BuildRequires:  unixODBC-devel
BuildRequires:  update-alternatives
BuildRequires:  xz

%if 0%{suse_version} > 1110
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xpm)
%else
BuildRequires:  xorg-x11-devel
%endif

%if 0%{suse_version} > 1110
BuildRequires:  freetds-devel
%endif

%if 0%{suse_version} >= 1320
BuildRequires:  libzip-devel
%endif

%if %{with spell}
BuildRequires:  aspell-devel
%endif

%if %{with firebird}
BuildRequires:  firebird-devel
# libfbclient2-devel pkg split in 12.2
# 'on all openSUSE from 12.1 (no sle12)', sigh
%if 0%{suse_version} > 1210 && (0%{?is_opensuse} || 0%{suse_version} != 1315)
BuildRequires:  libfbclient2-devel
%endif
%endif

# 10.3 does not install sendmail binary with the minimal system
Requires:       smtp_daemon
Requires:       timezone

# I would like this to become a hard dependency, as PHP is
# documented to have this modules by default (no addtional libs are needed)
Recommends:     %{name}-ctype %{name}-dom %{name}-iconv %{name}-sqlite %{name}-tokenizer
Recommends:     %{name}-xmlreader %{name}-xmlwriter %{name}-json

# other highly reccommended extensions
Suggests:       %{name}-mbstring %{name}-gd %{name}-pear %{name}-gettext %{name}-mysql

## Provides
Provides:       %{name} = %{version}
Provides:       %{name}-api = %{apiver}
Provides:       %{name}-zend-abi = %{zendver}
Provides:       %{name}(api) = %{apiver}
Provides:       %{name}(zend-abi) = %{zendver}

# builtin extensions
Provides:       %{name}-date
Provides:       %{name}-filter
Provides:       %{name}-hash
Provides:       %{name}-pcre
Provides:       %{name}-reflection
Provides:       %{name}-session
Provides:       %{name}-simplexml
Provides:       %{name}-spl
Provides:       %{name}-xml
Provides:       zend71v

# conflicts with php5 and should replace it
Obsoletes:      %{name} < %{version}

%description
This package contains the PHP 7.1 core files, including PHP binary (CLI)
and PHP configuration (php.ini). This package must be installed in
order to use PHP. Additionally, extension modules and server modules
(e.g. for Apache) may be installed.

Additional documentation is available in package php-doc.


%package devel
Summary:        Include files of %{php__doc_version}
Group:          Development/Languages/C and C++
# this is required by the installed  development headers
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libxml2-devel
# this is needed for "pecl" functionality
Requires:       autoconf
Requires:       automake
Requires:       libtool
Requires:       pcre-devel
Provides:       pecl
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description devel
PHP is a server-side, cross-platform, HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory Tutorial.  Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the Links section. %{php__doc_version} is the latest version.


%package pear
Summary:        PHP Extension and Application Repository
Group:          Development/Libraries/PHP
BuildArch:      noarch
Requires:       %{name}-zlib = %{version}
Requires:       %{name}-pear-Archive_Tar
Provides:       %{name}-pear = %{version}
Obsoletes:      %{name}-pear < %{version}

%description pear
PEAR is a code repository for PHP extensions and PHP library code
similar to TeX's CTAN and Perl's CPAN. This package provides an access
to the repository.

See http://pear.php.net/manual/ for more details.


%package pear-Archive_Tar
Summary:        Tar file management class
Group:          Productivity/Networking/Web/Servers
BuildArch:      noarch
Requires:       %{name}-pear = %{version}
# php5-pear-Archive_Tar provides Tar.php, which is provided
# by pear package itself; php5-pear-Archive_Tar was dropped
# on version 1.3.10, install-pear-nozlib.phar
# provides 1.4.0 currently
Provides:       %{name}-pear-Archive_Tar = 1.4.0
Obsoletes:      %{name}-pear-Archive_Tar < 1.3.11

%description pear-Archive_Tar
This class provides handling of tar files in PHP.
It supports creating, listing, extracting and adding to tar files.
Gzip support is available if PHP has the zlib extension built-in orloaded. 
Bz2 compression is also supported with the bz2 extension loaded.


%package fpm
Summary:        FastCGI Process Manager %{php__doc_version} Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
PreReq:         %insserv_prereq
Provides:       %{name}-date
Provides:       %{name}-filter
Provides:       %{name}-fpm = %{version}
Provides:       %{name}-pcre
Provides:       %{name}-reflection
Provides:       %{name}-session
Provides:       %{name}-simplexml
Provides:       %{name}-spl
Provides:       %{name}-xml

%if %{with systemd}
%{systemd_requires}
BuildRequires:  pkgconfig(libsystemd-daemon)
%endif
Obsoletes:      %{name}-fpm < %{version}

%description fpm
PHP is a server-side, cross-platform HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory tutorial. Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the links section.

Please refer to /usr/share/doc/packages/php7.1/README.FastCGI for
information on how to use this module.


%package bcmath
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-bcmath = %{version}
Obsoletes:      %{name}-bcmath < %{version}

%description bcmath
Binary Calculator which supports numbers of any size and precision,
represented as strings.


%package bz2
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-bz2 = %{version}
Obsoletes:      %{name}-bz2 < %{version}

%description bz2
PHP functions to read and write bzip2 (.bz2) compressed files.



%package calendar
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-calendar = %{version}
Obsoletes:      %{name}-calendar < %{version}

%description calendar
PHP functions for converting between different calendar formats.



%package ctype
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-ctype = %{version}
Obsoletes:      %{name}-ctype < %{version}

%description ctype
PHP functions for checking whether a character or string falls into a
certain character class according to the current locale.



%package curl
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-curl = %{version}
Obsoletes:      %{name}-curl < %{version}

%description curl
PHP interface to libcurl that allows you to connect to and communicate
with servers of many different types, using protocols of many different
types.



%package dba
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-dba = %{version}
Obsoletes:      %{name}-dba < %{version}

%description dba
This is a general abstraction layer for several file-based databases.
As such, functionality is limited to a common subset of features
supported by modern databases such as Sleepycat Software's DB2. (This
is not to be confused with IBM's DB2 software, which is supported
through the ODBC functions.)


%package dom
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-dom = %{version}
Obsoletes:      %{name}-dom < %{version}

%description dom
This module adds DOM support.


%package enchant
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-enchant = %{version}
Obsoletes:      %{name}-enchant < %{version}

%description enchant
Enchant is the PHP binding for the Enchant library. Enchant steps in to provide uniformity and conformity on top of all spelling libraries, and implements certain features that may be lacking in any individual provider library. Everything should "just work" for any and every definition of "just working."


%package exif
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-mbstring = %{version}
Provides:       %{name}-exif = %{version}
Obsoletes:      %{name}-exif < %{version}

%description exif
PHP functions for extracting EXIF (metadata from images) information
stored in headers of JPEG and TIFF images.


%package fileinfo
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-fileinfo = %{version}
Obsoletes:      %{name}-fileinfo < %{version}

%description fileinfo
The functions in this module try to guess the content type and encoding of a file by looking for certain magic byte sequences at specific positions within the file. While this is not a bullet proof approach the heuristics used do a very good job.


%package ftp
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-openssl = %{version}
Provides:       %{name}-ftp = %{version}
Obsoletes:      %{name}-ftp < %{version}

%description ftp
PHP functions for access to file servers speaking the File Transfer
Protocol (FTP) as defined in rfc959.


%package gd
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-gd = %{version}
Obsoletes:      %{name}-gd < %{version}

%description gd
PHP functions to create and manipulate image files in a variety of
different image formats, including GIF, PNG, JPEG, WBMP, and XPM. Even
more convenient: PHP can output image streams directly to a browser.


%package gettext
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-gettext = %{version}
Obsoletes:      %{name}-gettext < %{version}

%description gettext
PHP functions that implement an NLS (Native Language Support) API which
can be used to internationalize your PHP applications.


%package gmp
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-gmp = %{version}
Obsoletes:      %{name}-gmp < %{version}

%description gmp
PHP functions for work with arbitrary-length integers using the GNU MP
library.


%package iconv
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-iconv = %{version}
Obsoletes:      %{name}-iconv < %{version}

%description iconv
PHP interface to iconv character set conversion facility.


%package imap
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-imap = %{version}
Obsoletes:      %{name}-imap < %{version}

%description imap
PHP functions in this extension are not limited to the IMAP protocol,
despite their name. The underlying c-client library also supports NNTP,
POP3 and local mailbox access methods.


%package intl
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-intl = %{version}
Obsoletes:      %{name}-intl < %{version}

%description intl
Internationalization extension (further is referred as Intl) is a wrapper for ICU library, enabling PHP programmers to perform UCA-conformant collation and date/time/number/currency formatting in their scripts.


%package json
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-json = %{version}
Obsoletes:      %{name}-json < %{version}

%description json
Support for JSON (JavaScript Object Notation) serialization.


%package ldap
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-openssl = %{version}
Provides:       %{name}-ldap = %{version}
Obsoletes:      %{name}-ldap < %{version}

%description ldap
PHP interface to Lightweight Directory Access Protocol (LDAP).


%package mbstring
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-mbstring = %{version}
Obsoletes:      %{name}-mbstring < %{version}

%description mbstring
This extension provides multi-byte character safe string functions and
other utility functions such as conversion functions.


%package mcrypt
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-mcrypt = %{version}
Obsoletes:      %{name}-mcrypt < %{version}

%description mcrypt
PHP interface to the mcrypt library, which supports a wide variety of
block algorithms.


%package mysql
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       %{name}-mysql = %{version}
Provides:       php7_any_db = %{version}
Obsoletes:      %{name}-mysql < %{version}

%description mysql
PHP functions for access to MySQL database servers.


%if %{with firebird}
%package firebird
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       %{name}-firebird = %{version}
Provides:       php7_any_db = %{version}
Obsoletes:      %{name}-firebird < %{version}

%description firebird
PHP functions for access to firebird database servers.
%endif


%package odbc
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       %{name}-odbc = %{version}
Provides:       %{name}-pdo_odbc = %{version}
Obsoletes:      %{name}-odbc < %{version}

%description odbc
This module adds ODBC support.


%package opcache
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-opcache = %{version}
Obsoletes:      %{name}-opcache < %{version}

%description opcache
The Zend OPcache provides faster PHP execution through
opcode caching and optimization.


%package openssl
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-openssl = %{version}
Obsoletes:      %{name}-openssl < %{version}

%description openssl
This module adds OpenSSL support.



%package pcntl
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-pcntl = %{version}
Obsoletes:      %{name}-pcntl < %{version}

%description pcntl
This module will attempt to implement all features related to process
spawning and control (fork(), waitpid(), signal(), WIF's, etc). This is
extremley experimental, with hope to become stable on most UNIX's. I
greatly appreciate any feedback, fixes, and or suggestions on how to
improve/better implement this functionality.


%package phar
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-phar = %{version}
Obsoletes:      %{name}-phar < %{version}

%description phar
The phar extension provides a way to put entire PHP applications into a
single file called a "phar" (PHP Archive) for easy distribution and installation.


%package pdo
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-pdo = %{version}
Obsoletes:      %{name}-pdo < %{version}

%description pdo
PHP Data Objects - Data Access Abstraction

- light-weight
- provides common API for common database operations
- keeps majority of PHP specific stuff in the PDO core (such as
persistent resource management); drivers should only have to worry
about getting the data and not about PHP internals.


%package pgsql
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       %{name}-pgsql = %{version}
Provides:       php7_any_db = %{version}
Obsoletes:      %{name}-pgsql < %{version}

%description pgsql
PHP functions for access to PostgreSQL database servers. It includes
both traditional pgsql and pdo_pgsql drivers.


%package posix
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-posix = %{version}
Obsoletes:      %{name}-posix < %{version}

%description posix
This module allows to use POSIX-like functions in PHP.


%if %{with spell}
%package pspell
Summary:        %{php__doc_version} pspell extension
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       aspell-en
Provides:       %{name}-pspell = %{version}
Obsoletes:      %{name}-pspell < %{version}

%description pspell
PHP interface to the aspell, which provides spell checking
functionality.
%endif


%package readline
Summary:        %{php__doc_version} readline extension
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-readline = %{version}
Obsoletes:      %{name}-readline < %{version}

%description readline
PHP interface to libedit, which provides editable command line as well
as PHP interactive mode (php -a)


%package shmop
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-shmop = %{version}
Obsoletes:      %{name}-shmop < %{version}

%description shmop
PHP functions to read, write, create and delete UNIX shared memory
segments.


%package snmp
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-snmp = %{version}
Obsoletes:      %{name}-snmp < %{version}

%description snmp
PHP functions for SNMP.


%package soap
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-soap = %{version}
Obsoletes:      %{name}-soap < %{version}

%description soap
This module provides SOAP support.

SOAP extension can be used to write SOAP Servers and Clients. It
supports subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.


%package sockets
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-sockets = %{version}
Obsoletes:      %{name}-sockets < %{version}

%description sockets
A low-level interface to the socket communication functions based on
the popular BSD sockets, providing the possibility to act as a socket
server as well as a client. This extension is experimental!


%package sqlite
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Provides:       %{name}-sqlite = %{version}
Obsoletes:      %{name}-sqlite < %{version}

%description sqlite
This is an extension for the SQLite Embeddable SQL Database Engine.
http://www.sqlite.org/

SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

This package includes sqlite and pdo_sqlite modules for sqlite version
2 and 3 respectively.

%package sysvmsg
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-sysvmsg = %{version}
Obsoletes:      %{name}-sysvmsg < %{version}

%description sysvmsg
This module provides System V IPC support.


%package sysvsem
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-sysvsem = %{version}
Obsoletes:      %{name}-sysvsem < %{version}

%description sysvsem
PHP interface for System V semaphores.


%package sysvshm
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-sysvshm = %{version}
Obsoletes:      %{name}-sysvshm < %{version}

%description sysvshm
PHP interface for System V shared memory.



%package tidy
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-tidy = %{version}
Obsoletes:      %{name}-tidy < %{version}

%description tidy
Tidy is an extension based on Libtidy (http://tidy.sf.net/) and allows
a PHP developer to clean, repair, and traverse HTML, XHTML, and XML
documents -- including ones with embedded scripting languages such as
PHP or ASP within them using OO constructs.



%package tokenizer
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-tokenizer = %{version}
Obsoletes:      %{name}-tokenizer < %{version}

%description tokenizer
The tokenizer functions provide an interface to the PHP tokenizer
embedded in the Zend Engine. Using these functions you may write your
own PHP source analyzing or modification tools without having to deal
with the language specification at the lexical level.


%package wddx
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-wddx = %{version}
Obsoletes:      %{name}-wddx < %{version}

%description wddx
PHP functions for Web Distributed Data Exchange.


%package xmlrpc
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-xmlrpc = %{version}
Obsoletes:      %{name}-xmlrpc < %{version}

%description xmlrpc
This module adds XMLRPC-EPI support.


%package xsl
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-dom = %{version}
Provides:       %{name}-xsl = %{version}
Obsoletes:      %{name}-xsl < %{version}

%description xsl
This module adds new XSL support to PHP.


%package xmlreader
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-dom = %{version}
Provides:       %{name}-xmlreader = %{version}
Obsoletes:      %{name}-xmlreader < %{version}

%description xmlreader
XMLReader represents a reader that provides non-cached, forward-only
access to XML data. It is based upon the xmlTextReader API from libxml.


%package xmlwriter
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-xmlwriter = %{version}
Obsoletes:      %{name}-xmlwriter < %{version}

%description xmlwriter
XMLWriter wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or
files containing XML data.


%package zip
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-zip = %{version}
Obsoletes:      %{name}-zip < %{version}

%description zip
Zip is an extension to create, modify and read zip files.


%package zlib
Summary:        %{php__doc_version} Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Provides:       %{name}-zlib = %{version}
Obsoletes:      %{name}-zlib < %{version}

%description zlib
PHP functions to read and write gzip (.gz) compressed files.


%prep
%setup -q -n php-%{version}

%patch0
%patch2

# Safety check for API version change.
vapi=`sed -n '/#define PHP_API_VERSION/{s/.* //;p}' main/php.h`
if test "x${vapi}" != "x%{apiver}"; then
    : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
    : Update the apiver macro and rebuild.
    exit 1
fi
vzend=`sed -n '/#define ZEND_MODULE_API_NO/{s/^[^0-9]*//;p;}' Zend/zend_modules.h`
if test "x${vzend}" != "x%{zendver}"; then
    : Error: Upstream Zend ABI version is now ${vzend}, expecting %{zendver}.
    : Update the zendver macro and rebuild.
    exit 1
fi

%build
chmod 644 README.namespaces UPGRADING
# aclocal workaround - to be improved
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >>aclocal.m4

# Force use of system libtool:
libtoolize --force --copy
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4

# Regenerate configure scripts (patches change config.m4's)
touch configure.in
# we build three SAPI
%{__mkdir_p} build-fpm
%{__mkdir_p} build-cli

#for parser in `find -name "*.re"`;do
#    re2c -c --no-generation-date -gi "$parser" > ${parser%.*}.c
#done

%{__rm} -r ext/pcre/pcrelib

# regenerate configure etc.
%{__rm} configure
./buildconf --force

# export flags
CFLAGS="$RPM_OPT_FLAGS -O3 -fPIE -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing -O0"
CXXFLAGS="$RPM_OPT_FLAGS -O3 -fPIE -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing -O0"
%if %{with firebird}
CFLAGS="$CFLAGS -I/usr/include/firebird"
CXXFLAGS="$CXXFLAGS -I/usr/include/firebird"
%endif
export CFLAGS
export CXXFLAGS
export LDFLAGS="-pie"
export NO_INTERACTION=true
# where to install extensions
EXTENSION_DIR=%{extension_dir}
export EXTENSION_DIR
export PHP_MYSQLND_ENABLED=yes
export PHP_MYSQLND_COMPRESSION_SUPPORT=yes
# fix build-cli: libc-client.so needs -lssl
export IMAP_SHARED_LIBADD='-lssl'

# build function
##--mandir=%{_mandir} \
#--bindir=%{_bindir} \
#--includedir=%{_includedir} \
Build()
{
    sapi=$1
    pushd build-$1
    shift
    ../configure \
        --prefix=%{base_dir} \
        --datadir=%{php_datadir} \
		--mandir=%{base_dir}%{_mandir} \
		--bindir=%{base_dir}%{_bindir} \
		--includedir=%{base_dir}%{_includedir} \
        --with-libdir=%{_lib} \
        --sysconfdir=%{php_sysconf}/$sapi \
        --with-config-file-path=%{php_sysconf}/$sapi \
        --with-config-file-scan-dir=%{php_sysconf}/conf.d \
        --enable-libxml \
        --enable-session \
%if 0%{?suse_version} > 1010
        --with-pcre-regex=%{_usr} \
%else
        --with-pcre-regex \
%endif
        --enable-xml \
        --enable-simplexml \
        --enable-filter \
        --disable-debug \
        --enable-inline-optimization \
        --disable-rpath \
        --disable-static \
        --enable-shared \
        --with-pic \
        --with-gnu-ld \
        --enable-re2c-cgoto \
        --with-system-tzdata=%{_datadir}/zoneinfo \
        --enable-hash \
        --with-mhash \
        --enable-phpdbg=no \
%if 0%{suse_version} >= 1320
        --with-libzip \
%endif
        "$@" || { cat config.log; exit 1; }
    # Some modules are builtin, reasons:
    #  - libxml can not be shared (and is needed by PEAR)
    #  - spl doesn't build shared
    #  - simplexml is needed by spl
    #  - session need to be builtin, otherwise sqlite and other session engines fail
    #  - pcre is needed for PEAR
    #  - filter is builtin due security reasons
    # We have still have harcoded RPATH in some modules
    %{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
    %{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=LIBTOOL_IS_BROKED|g' libtool
    %{__make} %{?jobs:-j%jobs PHP_PEAR_PHP_BIN=%{base_dir}%{_bindir}/php}
    popd
}

# perform all builds
Build fpm \
%if %{with systemd}
    --with-fpm-systemd \
%endif
    --enable-fpm \
	--bindir=%{base_dir}%{_bindir} \
	--sbindir=%{base_dir}/usr/sbin  \
    --disable-cli \
    --disable-all \
    --localstatedir=%{base_dir}/var

Build cli \
    --enable-cli \
    --with-pear=%{peardir} \
    --enable-bcmath=shared \
    --enable-calendar=shared \
    --enable-ctype=shared \
    --enable-dom=shared \
    --enable-exif=shared \
    --enable-ftp=shared \
    --enable-mbstring=shared \
    --enable-mbregex \
    --enable-pcntl=shared \
    --enable-posix=shared \
    --enable-shmop=shared \
    --enable-soap=shared \
    --enable-sockets=shared \
    --enable-sysvmsg=shared \
    --enable-sysvsem=shared \
    --enable-sysvshm=shared \
    --enable-tokenizer=shared \
    --enable-wddx=shared \
    --enable-fileinfo=shared \
    --with-zlib=shared \
    --with-bz2=shared \
    --with-curl=shared \
%if 0%{suse_version} >= 1320
    --with-gd=shared,%{_usr} \
%else
    --with-gd=shared \
%endif
    --enable-gd-native-ttf \
    --with-xpm-dir=%{_x11prefix} \
    --with-freetype-dir=%{_usr} \
    --with-png-dir=%{_usr} \
    --with-jpeg-dir=%{_usr} \
    --with-zlib-dir=%{_usr} \
%if 0%{suse_version} > 1110
    --with-vpx-dir=%{_usr} \
%endif
    --with-gettext=shared \
    --with-gmp=shared \
    --with-iconv=shared \
    --with-imap=shared \
    --with-kerberos \
    --with-imap-ssl \
    --enable-json=shared \
    --with-ldap=shared \
    --with-ldap-sasl=%{_usr} \
    --with-libedit=shared,%{_usr} \
    --with-mcrypt=shared \
    --with-mysql=shared,mysqlnd \
%if %{with firebird}
    --with-interbase=shared \
%endif
%if 0%{?suse_version} > 1110
    --with-mysql-sock=/var/run/mysql/mysql.sock \
%else
    --with-mysql-sock=/var/lib/mysql/mysql.sock \
%endif
    --with-mysqli=shared,mysqlnd \
    --with-unixODBC=shared,%{_usr} \
    --with-openssl=shared \
    --with-pgsql=shared,%{_usr} \
    --enable-phar=shared \
%if %{with spell}
    --with-pspell=shared \
    --with-enchant=shared,%{_usr} \
%endif
    --with-snmp=shared \
    --with-xmlrpc=shared \
    --enable-xmlreader=shared \
    --enable-xmlwriter=shared \
    --with-xsl=shared \
    --with-tidy=shared,%{_usr} \
    --enable-dba=shared \
    --with-db4=%{_usr} \
    --without-gdbm \
    --with-cdb \
    --with-inifile \
    --with-flatfile \
    --enable-pdo=shared \
    --with-pdo_sqlite=shared,%{_usr} \
    --with-sqlite3=shared,%{_usr} \
    --enable-sqlite-utf8 \
    --with-pdo-mysql=shared,mysqlnd \
%if %{with firebird}
    --with-pdo-firebird=shared \
%endif
    --with-pdo-pgsql=shared,%{_usr} \
    --with-pdo-odbc=shared,unixODBC,%{_usr} \
    --enable-zip=shared \
    --enable-intl=shared,%{_usr} \
%if 0%{suse_version} > 1110
    --with-mssql=shared,%{_usr} \
%endif
    --disable-cgi

%check
cd build-cli
# check if we link against system libcrypt
if [ -z "$(ldd sapi/cli/php | grep libcrypt.so)" ]; then
    echo 'php does not link against system libcrypt.'
    exit 1
fi

# Run tests, using the CLI SAPI
%if %{with make_test}
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 LANG=POSIX LC_ALL=POSIX
unset TZ
%{__make} test || true
set +x
for f in `find .. -name "*.diff" -type f -print`; do
    echo "TEST FAILURE: $f --"
    cat "$f"
    echo "-- $f result ends."
done
set -x
unset NO_INTERACTION REPORT_EXIT_STATUS
%endif

%install

#create opt dir
%{__mkdir} -p %{buildroot}%{base_dir}

#create log dir
%{__mkdir} -p %{buildroot}%{base_dir}/var/log

#copy docs
%{__mkdir} -p %{buildroot}%{base_dir}/usr/share/doc/packages/%{name}
%{__cp} README* \
	CODING_STANDARDS \
	CREDITS \
	EXTENSIONS \
	LICENSE \
	NEWS \
	UPGRADING \
	%{buildroot}%{base_dir}/usr/share/doc/packages/%{name}

# install function
Install()
{
    pushd build-$1
    %{__make} install INSTALL_ROOT=%{buildroot} PHP_PEAR_PHP_BIN=%{base_dir}%{_bindir}/php
    popd
}

# do the actual installation
Install cli
Install fpm

# generate php.ini from php.ini-production:
%{__install} -d -m 755 %{buildroot}/%{php_sysconf}/conf.d
%{__install} -d -m 755 %{buildroot}/%{php_sysconf}/cli
%{__install} -d -m 755 %{buildroot}/%{php_sysconf}/fpm
%{__sed} "s=@extdir@=%{extension_dir}=" php.ini-production \
    | %{__sed} -r 's/^(html_errors|implicit_flush|max_execution_time|register_argc_argv)/;\1/' \
    > %{buildroot}/%{php_sysconf}/cli/php.ini

# prepare configuration files for each extension
extern_modules=""
for f in %{buildroot}%{extension_dir}/*; do
    if test ${f##*.} = a; then
        %{__rm} $f
        continue
    fi
    if test ${f##*.} = so; then
        f=${f%.so}
    fi
    ext=${f##*/}
    extern_modules="$extern_modules $ext"
    echo "; comment out next line to disable $ext extension in php" > %{buildroot}/%{php_sysconf}/conf.d/$ext.ini
    zend_=''
    if [ $ext == "opcache" ]; then
      # http://php.net/manual/en/opcache.installation.php
      zend_='zend_'
    fi
    echo "${zend_}extension=$ext.so" >> %{buildroot}/%{php_sysconf}/conf.d/$ext.ini
done
# list of builtin modules
builtin_modules=`./build-cli/sapi/cli/php -m | grep -E -v '^(\[.*)?$' | sort | tr '\n' ' '`
# directory for sessions
%{__install} -d %{buildroot}%{base_dir}/var/lib/%{pkg_name}
# documentation
%{__rm} -rf %{buildroot}/{.channels,.depdb*,.filemap,.lock,%{base_dir}/usr/bin/peardev}
%{__install} -d -m 0755 %{buildroot}/%{peardir}/test
# for pear XML files
%{__install} -d -m 0755 %{buildroot}%{base_dir}/var/lib/pear
#fix symlink
sed -i -e "s@$RPM_BUILD_DIR/php-%{rversion}/build-cli/sapi/cli/php@php@g" %{buildroot}%{base_dir}%{_bindir}/phar.phar
rm %{buildroot}%{base_dir}%{_bindir}/phar
%{__ln_s} -f %{base_dir}/%{_bindir}/phar.phar %{buildroot}%{base_dir}%{_bindir}/phar

# CVE-2014-5459, bnc#893849; couldn't find a way to use PHP_PEAR_CACHE_DIR 
# (install-pear is checking if the directory is writable by current user?;
#  unfortunately ENOTIME to figure out)
%{__sed} -i 's@15:"/tmp/pear/cache"@19:"/var/cache/php-pear"@' %{buildroot}%{php_sysconf}/cli/pear.conf
grep -c '/var/cache/php-pear' %{buildroot}%{php_sysconf}/cli/pear.conf || exit 1
# after the update for php 5.6.15 landed in Tumbleweed, almost all PEAR
# packages building against broke. The metadata generated when building
# the PEAR package gets written to /.<meta> instead of
# /usr/share/php7/PEAR/.<meta>, probably caused by the new PEAR option
# "metadata_dir" that was added in PEAR 1.10.0. Our specs suspect the data
# to be in the peardir (where is normally belongs).
# This option is not set in the current php7 package, but maybe providing
# a default value for this would resolve the issue for the +100 packages.
pd=%{peardir}
%{__sed} -i "s@\"metadata_dir\";s:0:\"\"@\"metadata_dir\";s:${#pd}:\"${pd}\"@" %{buildroot}%{php_sysconf}/cli/pear.conf
grep -c "\"metadata_dir\";s:${#pd}:\"${pd}\""  %{buildroot}%{php_sysconf}/cli/pear.conf || exit 1

#delete fastcgi bin (we don't support fastcgi sapi)
%{__rm} -f %{buildroot}%{base_dir}%{_bindir}/php-cgi

%{__install} -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}-fpm.service
%{__sed} -i 's=@@VERSION@@=%{version}=g; s=@@PHP_PREFIX@@=%{base_dir}=g' %{buildroot}%{_unitdir}/%{name}-fpm.service

#Create symbolic link to php binary in bindir
%{__mkdir_p} %{buildroot}%{_bindir}
%{__ln_s} -f %{base_dir}%{_bindir}/php %{buildroot}%{_bindir}/php-%{version}

%pre fpm
%service_add_pre %{name}-fpm.service

%postun fpm
%service_del_postun %{name}-fpm.service
%restart_on_update %{name}-fpm
%insserv_cleanup

%preun fpm
%service_del_preun %{name}-fpm.service
%stop_on_removal %{name}-fpm

%post fpm
%service_add_post %{name}-fpm.service
%{fillup_and_insserv -f %{name}-fpm}

%files
%defattr(-, root, root)
%doc %{base_dir}/usr/share/doc/packages/%{name}/*
%doc %{base_dir}%{_mandir}/man1/*
%dir %{php_sysconf}
%dir %{php_sysconf}/conf.d
%dir %{php_sysconf}/cli
%config(noreplace) %{php_sysconf}/cli/php.ini
%{base_dir}%{_bindir}/php
%{_bindir}/php-%{version}
%dir %{base_dir}%{_libdir}/%{pkg_name}
%dir %{extension_dir}
%dir %{php_datadir}
%attr(0755, wwwrun, root) %dir %{base_dir}/var/lib/%{pkg_name}
%attr(0755, root, root) %dir %{base_dir}/var/log

%files devel
%defattr(-, root, root)
%{base_dir}%{_includedir}/%{pkg_name}
%{base_dir}%{_bindir}/phpize
%{base_dir}%{_bindir}/php-config
%{base_dir}%{_bindir}/pecl
%{php_datadir}/build

%files pear
%defattr(-, root, root)
%{base_dir}%{_bindir}/pear
%config(noreplace) %{php_sysconf}/cli/pear.conf
%{peardir}
%exclude %{peardir}/Archive/Tar.php
%exclude %{peardir}/doc/Archive_Tar
%dir %{base_dir}/var/lib/pear

%files pear-Archive_Tar
%defattr(-, root, root)
%dir %{peardir}/Archive
%{peardir}/Archive/Tar.php
%{peardir}/doc/Archive_Tar

%files fpm
%defattr(-, root, root)
%{base_dir}%{_sbindir}/php-fpm
%dir %{php_sysconf}/fpm
%config %{php_sysconf}/fpm/php-fpm.conf.default
%dir %{php_sysconf}/fpm/php-fpm.d
%config %{php_sysconf}/fpm/php-fpm.d/www.conf.default
%{base_dir}%{_mandir}/man8/php-fpm.8
%dir %{php_datadir}/fpm
%{php_datadir}/fpm/status.html
%{_unitdir}/%{name}-fpm.service

%files bcmath
%defattr(644,root,root,755)
%{extension_dir}/bcmath.so
%config(noreplace) %{php_sysconf}/conf.d/bcmath.ini

%files bz2
%defattr(644,root,root,755)
%{extension_dir}/bz2.so
%config(noreplace) %{php_sysconf}/conf.d/bz2.ini

%files calendar
%defattr(644,root,root,755)
%{extension_dir}/calendar.so
%config(noreplace) %{php_sysconf}/conf.d/calendar.ini

%files ctype
%defattr(644,root,root,755)
%{extension_dir}/ctype.so
%config(noreplace) %{php_sysconf}/conf.d/ctype.ini

%files curl
%defattr(644,root,root,755)
%{extension_dir}/curl.so
%config(noreplace) %{php_sysconf}/conf.d/curl.ini

%files dba
%defattr(644,root,root,755)
%{extension_dir}/dba.so
%config(noreplace) %{php_sysconf}/conf.d/dba.ini

%files dom
%defattr(644,root,root,755)
%{extension_dir}/dom.so
%config(noreplace) %{php_sysconf}/conf.d/dom.ini

%files enchant
%defattr(644,root,root,755)
%{extension_dir}/enchant.so
%config(noreplace) %{php_sysconf}/conf.d/enchant.ini

%files exif
%defattr(644,root,root,755)
%{extension_dir}/exif.so
%config(noreplace) %{php_sysconf}/conf.d/exif.ini

%files fileinfo
%defattr(644,root,root,755)
%{extension_dir}/fileinfo.so
%config(noreplace) %{php_sysconf}/conf.d/fileinfo.ini

%files ftp
%defattr(644,root,root,755)
%{extension_dir}/ftp.so
%config(noreplace) %{php_sysconf}/conf.d/ftp.ini

%files gd
%defattr(644,root,root,755)
%{extension_dir}/gd.so
%config(noreplace) %{php_sysconf}/conf.d/gd.ini

%files gettext
%defattr(644,root,root,755)
%{extension_dir}/gettext.so
%config(noreplace) %{php_sysconf}/conf.d/gettext.ini

%files gmp
%defattr(644,root,root,755)
%{extension_dir}/gmp.so
%config(noreplace) %{php_sysconf}/conf.d/gmp.ini

%files iconv
%defattr(644,root,root,755)
%{extension_dir}/iconv.so
%config(noreplace) %{php_sysconf}/conf.d/iconv.ini

%files imap
%defattr(644,root,root,755)
%{extension_dir}/imap.so
%config(noreplace) %{php_sysconf}/conf.d/imap.ini

%files intl
%defattr(644,root,root,755)
%{extension_dir}/intl.so
%config(noreplace) %{php_sysconf}/conf.d/intl.ini

%files json
%defattr(644,root,root,755)
%{extension_dir}/json.so
%config(noreplace) %{php_sysconf}/conf.d/json.ini

%files ldap
%defattr(644,root,root,755)
%{extension_dir}/ldap.so
%config(noreplace) %{php_sysconf}/conf.d/ldap.ini

%files mbstring
%defattr(644,root,root,755)
%{extension_dir}/mbstring.so
%config(noreplace) %{php_sysconf}/conf.d/mbstring.ini

%files mcrypt
%defattr(644,root,root,755)
%{extension_dir}/mcrypt.so
%config(noreplace) %{php_sysconf}/conf.d/mcrypt.ini

%files mysql
%defattr(644,root,root,755)
%{extension_dir}/mysqli.so
%config(noreplace) %{php_sysconf}/conf.d/mysqli.ini
%{extension_dir}/pdo_mysql.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_mysql.ini

%if %{with firebird}
%files firebird
%defattr(644,root,root,755)
%{extension_dir}/interbase.so
%config(noreplace) %{php_sysconf}/conf.d/interbase.ini
%{extension_dir}/pdo_firebird.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_firebird.ini
%endif

%files odbc
%defattr(644,root,root,755)
%{extension_dir}/odbc.so
%config(noreplace) %{php_sysconf}/conf.d/odbc.ini
%{extension_dir}/pdo_odbc.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_odbc.ini

%files opcache
%defattr(644,root,root,755)
%{extension_dir}/opcache.so
%config(noreplace) %{php_sysconf}/conf.d/opcache.ini

%files openssl
%defattr(644,root,root,755)
%{extension_dir}/openssl.so
%config(noreplace) %{php_sysconf}/conf.d/openssl.ini

%files phar
%defattr(644,root,root,755)
%{extension_dir}/phar.so
%config(noreplace) %{php_sysconf}/conf.d/phar.ini
%{base_dir}%{_bindir}/phar
%{base_dir}%{_bindir}/phar.phar

%files pcntl
%defattr(644,root,root,755)
%{extension_dir}/pcntl.so
%config(noreplace) %{php_sysconf}/conf.d/pcntl.ini

%files pdo
%defattr(644,root,root,755)
%{extension_dir}/pdo.so
%config(noreplace) %{php_sysconf}/conf.d/pdo.ini

%files pgsql
%defattr(644,root,root,755)
%{extension_dir}/pgsql.so
%config(noreplace) %{php_sysconf}/conf.d/pgsql.ini
%{extension_dir}/pdo_pgsql.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_pgsql.ini

%files posix
%defattr(644,root,root,755)
%{extension_dir}/posix.so
%config(noreplace) %{php_sysconf}/conf.d/posix.ini

%if %{with spell}
%files pspell
%defattr(644,root,root,755)
%{extension_dir}/pspell.so
%config(noreplace) %{php_sysconf}/conf.d/pspell.ini
%endif

%files readline
%defattr(644,root,root,755)
%{extension_dir}/readline.so
%config(noreplace) %{php_sysconf}/conf.d/readline.ini

%files shmop
%defattr(644,root,root,755)
%{extension_dir}/shmop.so
%config(noreplace) %{php_sysconf}/conf.d/shmop.ini

%files snmp
%defattr(644,root,root,755)
%{extension_dir}/snmp.so
%config(noreplace) %{php_sysconf}/conf.d/snmp.ini

%files soap
%defattr(644,root,root,755)
%{extension_dir}/soap.so
%config(noreplace) %{php_sysconf}/conf.d/soap.ini

%files sockets
%defattr(644,root,root,755)
%{extension_dir}/sockets.so
%config(noreplace) %{php_sysconf}/conf.d/sockets.ini

%files sqlite
%defattr(644,root,root,755)
%{extension_dir}/pdo_sqlite.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_sqlite.ini
%{extension_dir}/sqlite3.so
%config(noreplace) %{php_sysconf}/conf.d/sqlite3.ini

%files sysvmsg
%defattr(644,root,root,755)
%{extension_dir}/sysvmsg.so
%config(noreplace) %{php_sysconf}/conf.d/sysvmsg.ini

%files sysvsem
%defattr(644,root,root,755)
%{extension_dir}/sysvsem.so
%config(noreplace) %{php_sysconf}/conf.d/sysvsem.ini

%files sysvshm
%defattr(644,root,root,755)
%{extension_dir}/sysvshm.so
%config(noreplace) %{php_sysconf}/conf.d/sysvshm.ini

%files tidy
%defattr(644,root,root,755)
%{extension_dir}/tidy.so
%config(noreplace) %{php_sysconf}/conf.d/tidy.ini

%files tokenizer
%defattr(644,root,root,755)
%{extension_dir}/tokenizer.so
%config(noreplace) %{php_sysconf}/conf.d/tokenizer.ini

%files wddx
%defattr(644,root,root,755)
%{extension_dir}/wddx.so
%config(noreplace) %{php_sysconf}/conf.d/wddx.ini

%files xmlrpc
%defattr(644,root,root,755)
%{extension_dir}/xmlrpc.so
%config(noreplace) %{php_sysconf}/conf.d/xmlrpc.ini

%files xmlreader
%defattr(644,root,root,755)
%{extension_dir}/xmlreader.so
%config(noreplace) %{php_sysconf}/conf.d/xmlreader.ini

%files xmlwriter
%defattr(644,root,root,755)
%{extension_dir}/xmlwriter.so
%config(noreplace) %{php_sysconf}/conf.d/xmlwriter.ini

%files xsl
%defattr(644,root,root,755)
%{extension_dir}/xsl.so
%config(noreplace) %{php_sysconf}/conf.d/xsl.ini

%files zip
%defattr(644,root,root,755)
%{extension_dir}/zip.so
%config(noreplace) %{php_sysconf}/conf.d/zip.ini

%files zlib
%defattr(644,root,root,755)
%{extension_dir}/zlib.so
%config(noreplace) %{php_sysconf}/conf.d/zlib.ini

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 7.1.0-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sun Apr 09 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
