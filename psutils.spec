#specfile originally created for Fedora, modified for Moblin Linux
Summary: PostScript Utilities
Name: psutils
Version: 1.17
Release: 29
License: distributable
Group: Applications/Publishing
URL: http://www.ctan.org/pkg/psutils
Source: http://www.ctan.org/tex-archive/support/psutils/psutils-p17.tar.gz
Patch0: psutils-p17-Makefile.patch
Patch1: psutils-p17-misc.patch
Patch2: psutils-p17-paper.patch
Patch3: psutils-p17-strip.patch
Patch4: psutils-manpage.patch
Patch5: psutils-psmerge.patch
BuildRoot: %{_tmppath}/psutils-root

%description
This archive contains some utilities for manipulating PostScript documents.
Page selection and rearrangement are supported, including arrangement into
signatures for booklet printing, and page merging for n-up printing.

%prep
%setup -q -n psutils
%patch0 -p1 -b .makefile
%patch1 -p1 -b .misc
%patch2 -p1 -b .paper
%patch3 -p1 -b .strip
%patch4 -p1 -b .manpage
%patch5 -p1 -b .new

%build
make -f Makefile.unix RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
 
%install
rm -rf $RPM_BUILD_ROOT

make -f Makefile.unix \
        MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
        DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, root, root, 0755)
%doc README LICENSE
%attr(0755, root, root) /usr/bin/*
%{_mandir}/*/*
/usr/lib/psutils

