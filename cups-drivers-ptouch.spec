%define rname ptouch

Summary:	CUPS/foomatic driver for Brother P-touch label printers
Name:		cups-drivers-%{rname}
Version:	1.2
Release:	%mkrel 2
License:	GPL
Group:		System/Printing
URL:		http://www.diku.dk/~panic/P-touch/
Source0:	http://www.diku.dk/~panic/P-touch/%{rname}-driver-%{version}.tar.gz
Requires:	cups
BuildRequires:	cupsddk
BuildRequires:	cups-devel
BuildRequires:	ghostscript
Conflicts:	cups-drivers-2006 cups-drivers-2007
Conflicts:	printer-utils-2006 printer-utils-2007
Conflicts:	printer-filters-2006 printer-filters-2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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