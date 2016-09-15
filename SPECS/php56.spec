#
# spec file for package php56
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


# _without_ make_test by default
# use build-test.sh for testing!
%bcond_with make_test

Name:           php56
%global apiver      20131106
%global zendver     20131226
%define pkg_name php5
%define with_spell 1
%define php_dir_name %{name}

BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  enchant-devel
%if 0%{suse_version} > 1110
# firebird first added in 11.2; libfbclient2-devel pkg split in 12.2
%define with_firebird 1
BuildRequires:  firebird-devel
%if 0%{suse_version} > 1210
BuildRequires:  libfbclient2-devel
%endif
%else
# <= 11.1 or SLES 11
%define with_firebird 0
%endif
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  imap-devel
BuildRequires:  krb5-devel
BuildRequires:  libbz2-devel
BuildRequires:  libevent-devel
BuildRequires:  libicu-devel
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
BuildRequires:  pkgconfig
BuildRequires:  postfix
BuildRequires:  postgresql-devel
BuildRequires:  tcpd-devel
BuildRequires:  unixODBC-devel
BuildRequires:  update-alternatives
BuildRequires:  xz
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xpm)
%if 0%{suse_version} > 1110
BuildRequires:  freetds-devel
%endif
%if %{with_spell}
BuildRequires:  aspell-devel
%endif
# I would like this to become a hard dependency, as PHP is
# documented to have this modules by default (no addtional libs are needed)
Recommends:     php56-ctype php56-dom php56-iconv php56-sqlite php56-tokenizer
Recommends:     php56-xmlreader php56-xmlwriter php56-json
# other highly reccommended extensions
Suggests:       php56-mbstring php56-gd php56-pear php56-gettext php56-mysql
BuildRequires:  libedit-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pcre-devel
BuildRequires:  re2c
BuildRequires:  sqlite3-devel
#10.3 does not install sendmail binary with the minimal system
Requires:       smtp_daemon

%define base_dir		  /opt/php/%{php_dir_name}
%define php_datadir		  %{base_dir}%{_datadir}/%{pkg_name}
%define extension_dir     %{base_dir}%{_libdir}/%{pkg_name}/extensions
%define peardir           %{php_datadir}/PEAR
%define php_sysconf       %{base_dir}%{_sysconfdir}/%{pkg_name}
%define _x11prefix %(pkg-config --variable=prefix xft)
%define need_libxml2_hack  %(if [ -e %{_includedir}/libxml/parser.h ]; then if grep -q XML_PARSE_OLDSAX %{_includedir}/libxml/parser.h;then echo 1; else echo 0; fi; else echo 0; fi)
Version:        5.6.16
Release:        3
Provides:       php56
Provides:       php56-api = %{apiver}
Provides:       php56-date
Provides:       php56-filter
Provides:       php56-hash
Provides:       php56-pcre
Provides:       php56-reflection
Provides:       php56-session
Provides:       php56-simplexml
Provides:       php56-spl
Provides:       php56-xml
Provides:       php56-zend-abi = %{zendver}
Provides:       php56(api) = %{apiver}
Provides:       php56(zend-abi) = %{zendver}
Source0:        http://us2.php.net/distributions/php-%{version}.tar.xz
Source1:        php5-fpm.service.template

Patch0:         php56-phpize.patch
Patch2:         php56-php-config.patch
Patch10:        php56-mbstring-missing-return.patch
Patch11:        php56-BNC-457056.patch

# following patch is to fix configure tests for crypt; the aim is to have php
# built against glibc's crypt; problem is, that our glibc doesn't support extended
# DES, so as soon as upstream fixes this, don't forgot to remove extended DES
# from their checking as I indicated in crypt-tests.patch yet, or php will
# silently use his own implementation again
Patch14:        php56-crypt-tests.patch
# related to previous patch; !(defined(_REENTRANT) || defined(_THREAD_SAFE))
Patch15:        php56-no-reentrant-crypt.patch
Patch16:        php56-format-string-issues.patch
#https://github.com/php/php-src/commit/6a813634052710f3f4bf6e2e03ca1b6c7be3bcee
#Patch19:        php56-crypto-checks.patch
Url:            http://www.php.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        PHP56 Core Files
License:        PHP-3.01
Requires:       timezone

%description
This package contains the PHP56 core files, including PHP binary (CLI)
and PHP configuration (php.ini). This package must be installed in
order to use PHP. Additionally, extension modules and server modules
(e.g. for Apache) may be installed.

Additional documentation is available in package php-doc.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package devel
Provides:       pecl
Provides:       php56-devel
Summary:        Include files of PHP56
Group:          Development/Languages/C and C++
#this is required by the installed  development headers
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libxml2-devel
#this is needed for "pecl" functionality
Requires:       autoconf
Requires:       automake
Requires:       libtool
Requires:       pcre-devel
Conflicts:      php4-devel
Provides:       php56-macros = 2.0
Obsoletes:      php56-macros < 2.0

%description devel
PHP is a server-side, cross-platform, HTML embedded scripting language.
If you are completely new to PHP and want to get some idea of how it
works, have a look at the Introductory Tutorial.  Once you get beyond
that have a look at the example archive sites and some of the other
resources available in the Links section. PHP5 is the latest version.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package pear
Provides:       php56-pear
Summary:        PHP Extension and Application Repository
Group:          Development/Libraries/PHP
Requires:       %{name}-zlib = %{version}
# php5-pear-Archive_Tar provides Tar.php, which is provided
# by pear package itself; php5-pear-Archive_Tar was dropped
# on version 1.3.10, install-pear-nozlib.phar
# provides 1.3.11 currently
Provides:       php5-pear-Archive_Tar = 1.3.11
Obsoletes:      php5-pear-Archive_Tar < 1.3.11
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description pear
PEAR is a code repository for PHP extensions and PHP library code
similar to TeX's CTAN and Perl's CPAN. This package provides an access
to the repository.

See http://pear.php.net/manual/ for more details.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

	
%package fpm
Summary:        FastCGI Process Manager PHP5 Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
PreReq:         %insserv_prereq
Provides:       php56-date
Provides:       php56-filter
Provides:       php56-fpm
Provides:       php56-pcre
Provides:       php56-reflection
Provides:       php56-session
Provides:       php56-simplexml
Provides:       php56-spl
Provides:       php56-xml
%if 0%{suse_version} > 1130
%define with_systemd 1
%{systemd_requires}
BuildRequires:  pkgconfig(libsystemd-daemon)
%else
# <= 11.3 or SLES 11
%define with_systemd 0
%endif

%description fpm
  PHP is a server-side, cross-platform HTML embedded scripting language.
  If you are completely new to PHP and want to get some idea of how it
  works, have a look at the Introductory tutorial. Once you get beyond
  that have a look at the example archive sites and some of the other
  resources available in the links section.

  Please refer to /usr/share/doc/packages/php5/README.FastCGI for
  information on how to use this module.


{>
(>Authors:
  --------
      The PHP Group
      See http://www.php.net/credits.php for more details

%package bcmath
Provides:       php56-bcmath
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description bcmath
Binary Calculator which supports numbers of any size and precision,
represented as strings.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package bz2
Provides:       php56-bz2
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description bz2
PHP functions to read and write bzip2 (.bz2) compressed files.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package calendar
Provides:       php56-calendar
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description calendar
PHP functions for converting between different calendar formats.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package ctype
Provides:       php56-ctype
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description ctype
PHP functions for checking whether a character or string falls into a
certain character class according to the current locale.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package curl
Provides:       php56-curl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description curl
PHP interface to libcurl that allows you to connect to and communicate
with servers of many different types, using protocols of many different
types.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package dba
Provides:       php56-dba
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description dba
This is a general abstraction layer for several file-based databases.
As such, functionality is limited to a common subset of features
supported by modern databases such as Sleepycat Software's DB2. (This
is not to be confused with IBM's DB2 software, which is supported
through the ODBC functions.)



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package dom
Provides:       php56-dom
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description dom
This module adds DOM support.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package enchant
Provides:       php56-enchant
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description enchant
Enchant is the PHP binding for the Enchant library. Enchant steps in to provide uniformity and conformity on top of all spelling libraries, and implements certain features that may be lacking in any individual provider library. Everything should "just work" for any and every definition of "just working."


Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package exif
Provides:       php56-exif
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-mbstring = %{version}

%description exif
PHP functions for extracting EXIF (metadata from images) information
stored in headers of JPEG and TIFF images.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package fileinfo
Provides:       php56-fileinfo
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description fileinfo
The functions in this module try to guess the content type and encoding of a file by looking for certain magic byte sequences at specific positions within the file. While this is not a bullet proof approach the heuristics used do a very good job.


Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package ftp
Provides:       php56-ftp
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-openssl = %{version}

%description ftp
PHP functions for access to file servers speaking the File Transfer
Protocol (FTP) as defined in rfc959.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package gd
Provides:       php56-gd
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description gd
PHP functions to create and manipulate image files in a variety of
different image formats, including GIF, PNG, JPEG, WBMP, and XPM. Even
more convenient: PHP can output image streams directly to a browser.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package gettext
Provides:       php56-gettext
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description gettext
PHP functions that implement an NLS (Native Language Support) API which
can be used to internationalize your PHP applications.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package gmp
Provides:       php56-gmp
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description gmp
PHP functions for work with arbitrary-length integers using the GNU MP
library.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details


%package iconv
Provides:       php56-iconv
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description iconv
PHP interface to iconv character set conversion facility.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package imap
Provides:       php56-imap
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description imap
PHP functions in this extension are not limited to the IMAP protocol,
despite their name. The underlying c-client library also supports NNTP,
POP3 and local mailbox access methods.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details


%package intl
Provides:       php56-intl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description intl
Internationalization extension (further is referred as Intl) is a wrapper for ICU library, enabling PHP programmers to perform UCA-conformant collation and date/time/number/currency formatting in their scripts.


Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details



%package json
Provides:       php56-json
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description json
Support for JSON (JavaScript Object Notation) serialization.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package ldap
Provides:       php56-ldap
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-openssl = %{version}

%description ldap
PHP interface to Lightweight Directory Access Protocol (LDAP).



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package mbstring
Provides:       php56-mbstring
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description mbstring
This extension provides multi-byte character safe string functions and
other utility functions such as conversion functions.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package mcrypt
Provides:       php56-mcrypt
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description mcrypt
PHP interface to the mcrypt library, which supports a wide variety of
block algorithms.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details



%package mssql
Provides:       php56-mssql
Provides:       php_any_db
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP

%description mssql
PHP functions for access to MSSQL database servers.


%package mysql
Provides:       php56-mysql
Provides:       php56-mysqli = %{version}
Provides:       php56-pdo_mysql = %{version}
Provides:       php_any_db
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Obsoletes:      php56-mysqli < %{version}
Obsoletes:      php56-pdo_mysql < %{version}

%description mysql
PHP functions for access to MySQL database servers.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%if %{with_firebird}
%package firebird
Provides:       php56-interbase
Provides:       php56-pdo_firebird = %{version}
Provides:       php_any_db
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Obsoletes:      php56-pdo_firebird < %{version}

%description firebird
PHP functions for access to firebird database servers.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details
%endif

%package odbc
Provides:       php56-odbc
Provides:       php56-pdo_odbc
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}

%description odbc
This module adds ODBC support.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package opcache
Provides:       php56-opcache
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description opcache
The Zend OPcache provides faster PHP execution through
opcode caching and optimization.


Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package openssl
Provides:       php56-openssl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description openssl
This module adds OpenSSL support.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package pcntl
Provides:       php56-pcntl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description pcntl
This module will attempt to implement all features related to process
spawning and control (fork(), waitpid(), signal(), WIF's, etc). This is
extremley experimental, with hope to become stable on most UNIX's. I
greatly appreciate any feedback, fixes, and or suggestions on how to
improve/better implement this functionality.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package phar
Provides:       php56-phar
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description phar
The phar extension provides a way to put entire PHP applications into a
single file called a "phar" (PHP Archive) for easy distribution and installation.

Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package pdo
Provides:       php56-pdo
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description pdo
PHP Data Objects - Data Access Abstraction

- light-weight

- provides common API for common database operations

- keeps majority of PHP specific stuff in the PDO core (such as
persistent resource management); drivers should only have to worry
about getting the data and not about PHP internals.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package pgsql
Provides:       php56-pgsql
Provides:       php56-pdo_pgsql = %{version}
Provides:       php_any_db
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}
Obsoletes:      php56-pdo_pgsql < %{version}

%description pgsql
PHP functions for access to PostgreSQL database servers. It includes
both traditional pgsql and pdo_pgsql drivers.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package posix
Provides:       php56-posix
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description posix
This module allows to use POSIX-like functions in PHP.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%if %{with_spell}

%package pspell
Provides:       php56-pspell
Summary:        PHP5 pspell extension
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       aspell-en

%description pspell
PHP interface to the aspell, which provides spell checking
functionality.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%endif

%package readline
Provides:       php56-readline
Summary:        PHP5 readline extension
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description readline
PHP interface to libedit, which provides editable command line as well
as PHP interactive mode (php -a)



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package shmop
Provides:       php56-shmop
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description shmop
PHP functions to read, write, create and delete UNIX shared memory
segments.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package snmp
Provides:       php56-snmp
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description snmp
PHP functions for SNMP.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package soap
Provides:       php56-soap
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description soap
This module provides SOAP support.

SOAP extension can be used to write SOAP Servers and Clients. It
supports subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package sockets
Provides:       php56-sockets
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description sockets
A low-level interface to the socket communication functions based on
the popular BSD sockets, providing the possibility to act as a socket
server as well as a client. This extension is experimental!



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package sqlite
Provides:       php56-sqlite
Provides:       php56-sqlite3 = %{version}
Provides:       php56-pdo_sqlite = %{version}
Provides:       php56-sqlite3 = %{version}
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-pdo = %{version}

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



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package sysvmsg
Provides:       php56-sysvmsg
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description sysvmsg
This module provides System V IPC support.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package sysvsem
Provides:       php56-sysvsem
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description sysvsem
PHP interface for System V semaphores.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package sysvshm
Provides:       php56-sysvshm
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description sysvshm
PHP interface for System V shared memory.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package tidy
Provides:       php56-tidy
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description tidy
Tidy is an extension based on Libtidy (http://tidy.sf.net/) and allows
a PHP developer to clean, repair, and traverse HTML, XHTML, and XML
documents -- including ones with embedded scripting languages such as
PHP or ASP within them using OO constructs.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package tokenizer
Provides:       php56-tokenizer
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description tokenizer
The tokenizer functions provide an interface to the PHP tokenizer
embedded in the Zend Engine. Using these functions you may write your
own PHP source analyzing or modification tools without having to deal
with the language specification at the lexical level.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package wddx
Provides:       php56-wddx
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description wddx
PHP functions for Web Distributed Data Exchange.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package xmlrpc
Provides:       php56-xmlrpc
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description xmlrpc
This module adds XMLRPC-EPI support.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package xsl
Provides:       php56-xsl
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-dom = %{version}

%description xsl
This module adds new XSL support to PHP.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package xmlreader
Provides:       php56-xmlreader
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}
Requires:       %{name}-dom = %{version}

%description xmlreader
XMLReader represents a reader that provides non-cached, forward-only
access to XML data. It is based upon the xmlTextReader API from libxml.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package xmlwriter
Provides:       php56-xmlwriter
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description xmlwriter
XMLWriter wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or
files containing XML data.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package zip
Provides:       php56-zip
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description zip
Zip is an extension to create, modify and read zip files.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%package zlib
Provides:       php56-zlib
Summary:        PHP5 Extension Module
Group:          Development/Libraries/PHP
Requires:       %{name} = %{version}

%description zlib
PHP functions to read and write gzip (.gz) compressed files.



Authors:
--------
    The PHP Group
    See http://www.php.net/credits.php for more details

%prep
%setup -q -n php-%{version}
%patch0
%patch2
%patch10
%if %{need_libxml2_hack}
echo "*** APPLY LIBXML2.7 FIX ***"
%patch11
%else
echo "*** SKIPPING LIBMXL2.7 FIX ***"
%endif
%patch14
%patch15
%patch16
#%patch19
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

for parser in `find -name "*.re"`;do
    re2c --no-generation-date -gi "$parser" > ${parser%.*}.c
done

%{__rm} -r ext/pcre/pcrelib

# regenerate configure etc.
# workaround: updates timestamp of configure, confusing buildconf
%{__rm} configure
./buildconf --force
# export flags
CFLAGS="$RPM_OPT_FLAGS -O3 -fPIE -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing"
CXXFLAGS="$RPM_OPT_FLAGS -O3 -fPIE -fPIC -DPIC -D_GNU_SOURCE -fno-strict-aliasing"
%if %{with_firebird}
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
        --with-libdir=%{_lib} \
        --includedir=%{base_dir}%{_includedir} \
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
        --enable-spl \
        --enable-filter \
        --disable-debug \
        --enable-inline-optimization \
        --disable-rpath \
		--disable-static \
		--enable-shared \
		--with-pic \
		--with-gnu-ld \
		--enable-re2c-cgoto \
		--with-system-tzdata=/usr/share/zoneinfo \
        --enable-hash \
        --with-mhash \
        "$@" || cat config.log
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
    %{__make} %{?jobs:-j%jobs PHP_PEAR_PHP_BIN=%{_bindir}/php}
    popd
}
# perform all builds
Build fpm \
%if %{with_systemd}
        --with-fpm-systemd \
%endif
	--enable-fpm \
	--bindir=%{base_dir}%{_bindir} \
	--sbindir=%{base_dir}/usr/sbin  \
	--disable-cli \
	--disable-all\

# cli sapi with all shared modules
# Hack the built configure to also link ncurses together with libedit.
# this is reported upstream bug http://bugs.php.net/bug.php?id=21153
sed -i "s/-ledit/-ledit -lncurses/g" configure
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
    --with-gd=shared \
        --enable-gd-native-ttf \
        --with-xpm-dir=%{_x11prefix} \
        --with-freetype-dir=%{_usr} \
        --with-png-dir=%{_usr} \
        --with-jpeg-dir=%{_usr} \
        --with-zlib-dir=%{_usr} \
        --with-vpx-dir=%{_usr} \
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
%if %{with_firebird}
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
%if %{with_spell}
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
%if %{with_firebird}
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
# things that currently do not compile:
# extensions:
#    --with-recode=shared \ error: recode extension can not be configured together with: imap mysql yaz
#disabled extensions
#    --enable-embedded-mysqli \

%check
cd build-cli
# check if we link against system libcrypt
if [ -z "$(ldd sapi/cli/php | grep libcrypt.so)" ]; then
  echo 'php do not link against system libcrypt.'
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
builtin_modules=`./build-cli/sapi/cli/php -m | egrep -v '^(\[.*)?$' | sort | tr '\n' ' '`
# update readme
# directory for sessions
%{__install} -d %{buildroot}%{base_dir}/var/lib/%{pkg_name}
# documentation
%{__rm} -rf %{buildroot}/{.channels,.depdb*,.filemap,.lock,%{base_dir}/usr/bin/peardev}
%{__install} -d -m 0755 %{buildroot}/%{peardir}/test
# for pear XML files
%{__install} -d -m 0755 %{buildroot}%{base_dir}/var/lib/pear
#fix symlink
sed -i -e "s@$RPM_BUILD_DIR/php-%{version}/build-cli/sapi/cli/php@php@g" %{buildroot}%{base_dir}%{_bindir}/phar.phar
rm %{buildroot}%{base_dir}%{_bindir}/phar
%{__ln_s} -f %{base_dir}%{_bindir}/phar.phar %{buildroot}%{base_dir}%{_bindir}/phar
# CVE-2014-5459, bnc#893849; couldn't find a way to use PHP_PEAR_CACHE_DIR 
# (install-pear is checking if the directory is writable by current user?;
#  unfortunately ENOTIME to figure out)
%{__sed} -i 's@15:"/tmp/pear/cache"@19:"/var/cache/php-pear"@' %{buildroot}%{php_sysconf}/cli/pear.conf
grep -c '/var/cache/php-pear' %{buildroot}%{php_sysconf}/cli/pear.conf || exit 1

#delete fastcgi bin (we don't support fastcgi sapi)
%{__rm} -f %{buildroot}%{base_dir}%{_bindir}/php-cgi

%{__install} -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}-fpm.service
%{__sed} -i 's=@@VERSION@@=%{version}=g; s=@@PHP_PREFIX@@=%{base_dir}=g' %{buildroot}%{_unitdir}/%{name}-fpm.service

#Create symbolic link to php binary in bindir
%{__mkdir_p} %{buildroot}%{_bindir}
%{__ln_s} -f %{base_dir}%{_bindir}/php %{buildroot}%{_bindir}/php-%{version}

%if %{with_systemd}
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
%endif

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
%dir %{base_dir}%{_datadir}/%{pkg_name}
%attr(0755, wwwrun, root) %dir %{base_dir}/var/lib/%{pkg_name}
%attr(0755, root, root) %dir %{base_dir}/var/log

%files devel
%defattr(-, root, root)
%{base_dir}%{_includedir}/%{pkg_name}
%{base_dir}%{_bindir}/phpize
%{base_dir}%{_bindir}/php-config
%{base_dir}%{_bindir}/pecl
%{base_dir}%{_datadir}/%{pkg_name}/build

%files pear
%defattr(-, root, root)
%{base_dir}%{_bindir}/pear
%config(noreplace) %{php_sysconf}/cli/pear.conf
%{peardir}
%dir %{base_dir}/var/lib/pear

%files fpm
%defattr(-, root, root)
%{base_dir}%{_sbindir}/php-fpm
%dir %{php_sysconf}/fpm
%config %{php_sysconf}/fpm/php-fpm.conf.default
%{base_dir}%{_mandir}/man8/php-fpm.8
%dir %{base_dir}/usr/share/php5/fpm
%{base_dir}/usr/share/php5/fpm/status.html
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

%if 0%{suse_version} > 1110

%files mssql
%defattr(644,root,root,755)
%{extension_dir}/mssql.so
%config(noreplace) %{php_sysconf}/conf.d/mssql.ini
%endif

%files mysql
%defattr(644,root,root,755)
%{extension_dir}/mysql.so
%config(noreplace) %{php_sysconf}/conf.d/mysql.ini
%{extension_dir}/mysqli.so
%config(noreplace) %{php_sysconf}/conf.d/mysqli.ini
%{extension_dir}/pdo_mysql.so
%config(noreplace) %{php_sysconf}/conf.d/pdo_mysql.ini

%if %{with_firebird}
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
%if %{with_spell}

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
* Thu Sep 15 2016 Marcin Morawski <marcin@morawskim.pl>
-  add symlink to php binary in bindir

* Wed Sep 14 2016 Marcin Morawski <marcin@morawskim.pl>
-  add systemd service for php56-fpm
