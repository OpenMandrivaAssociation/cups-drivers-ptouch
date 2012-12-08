%define rname ptouch

Summary:	CUPS/foomatic driver for Brother P-touch label printers
Name:		cups-drivers-%{rname}
Version:	1.3
Release:	%mkrel 8
License:	GPL
Group:		System/Printing
URL:		http://www.diku.dk/~panic/P-touch/
Source0:	http://www.diku.dk/~panic/P-touch/%{rname}-driver-%{version}.tar.gz
Requires:	cups
BuildRequires:	cups
BuildRequires:	cups-devel
BuildRequires:	ghostscript
Conflicts:	cups-drivers = 2007
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
Conflicts:	foomatic-db < 1:3.0.2-1.20070820.1mdv2008.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The ptouch-driver consists of a CUPS raster filter for driving the family of
Brother P-touch label printers.

This package contains CUPS foomatic drivers for the following printers:

%prep
%setup -q -n %{rname}-driver-%{version}

%build

%configure2_5x \
    --libdir=%{_prefix}/lib

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/cups/model/%{rname}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(0755,root,root) %{_prefix}/lib/cups/filter/rastertoptch
%attr(0644,root,root) %{_datadir}/foomatic/db/source/printer/*.xml
%attr(0644,root,root) %{_datadir}/foomatic/db/source/driver/*.xml
%attr(0644,root,root) %{_datadir}/foomatic/db/source/opt/*.xml
%attr(0755,root,root) %dir %{_datadir}/cups/model/%{rname}


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3-5mdv2011.0
+ Revision: 663446
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-4mdv2011.0
+ Revision: 603878
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-3mdv2010.1
+ Revision: 518901
- fix deps
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3-2mdv2010.0
+ Revision: 413294
- rebuild

* Sun Mar 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.3-1mdv2009.1
+ Revision: 360184
- Updated to version 1.3
- Dropped ptouch-driver-gcc43_fix.diff (merged)

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2-8mdv2009.1
+ Revision: 318081
- rebuild

* Wed Jul 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2-7mdv2009.0
+ Revision: 230683
- added a gcc43 patch (P0)
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.2-5mdv2008.1
+ Revision: 149156
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.2-4mdv2008.0
+ Revision: 76079
- Added conflicts to foomatic-db < 1:3.0.2-1.20070820.1mdv2008.0

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2-3mdv2008.0
+ Revision: 75335
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2-2mdv2008.0
+ Revision: 64156
- use the new System/Printing RPM GROUP

* Tue Aug 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2-1mdv2008.0
+ Revision: 63010
- Import cups-drivers-ptouch



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2-1mdv2008.0
- initial Mandriva package
