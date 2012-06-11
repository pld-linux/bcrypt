Summary:	File encryption utility
Name:		bcrypt
Version:	1.1
Release:	1
License:	BSD
Group:		Applications/File
URL:		http://bcrypt.sourceforge.net/
Source0:	http://downloads.sourceforge.net/bcrypt/%{name}-%{version}.tar.gz
# Source0-md5:	8ce2873836ccd433329c8df0e37e298c
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bcrypt is a cross platform file encryption utility. Encrypted files
are portable across all supported operating systems and processors.
Passphrases must be between 8 and 56 characters and are hashed
internally to a 448 bit key. However, all characters supplied are
significant. The stronger your passphrase, the more secure your data.

In addition to encrypting your data, bcrypt will by default overwrite
the original input file with random garbage three times before
deleting it in order to thwart data recovery attempts by persons who
may gain access to your computer. Bcrypt uses the blowfish encryption
algorithm published by Bruce Schneier in 1993.

%prep
%setup -q

%{__sed} -i -e 's|\${PREFIX}/man/man1|\${PREFIX}/share/man/man1|g' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/bcrypt
%{_mandir}/man1/bcrypt.1*
